import warnings
from typing import List, Union

import nibabel as nib
import numpy as np

from nimesh import AffineTransform, CoordinateSystem, Mesh, Segmentation
from nimesh import Label
from nimesh.core import VertexData


def load(filename: str) -> Mesh:
    """Loads a mesh from a GIfTI file

    Loads the vertices and triangles of a mesh in the GIfTI file format. If
    a transform or segmentation is contained in the file, they will also be
    loaded.

    Args:
        filename: The name of the GIfTI file to load.

    Returns:
        mesh: The mesh loaded from the supplied file.

    Raises:
        ValueError: If the file does not contains a vertex and triangle array.

    Warnings:
        RuntimeWarning: If the file contains more than one vertex or
            triangle array.

    """

    gii = nib.load(filename)

    # Get the vertices array. If there is more than one, warn the user and
    # use the first one.
    vertex_arrays = gii.get_arrays_from_intent('NIFTI_INTENT_POINTSET')

    if len(vertex_arrays) == 0:
        raise ValueError('The file {} does not contain any vertex data.'
                         .format(filename))

    elif len(vertex_arrays) > 1:
        warnings.warn('The file {} contains more than one vertex array. The '
                      'first one was used. Proceed with caution.'
                      .format(filename),
                      RuntimeWarning)
    vertex_array = vertex_arrays[0]
    vertices = vertex_array.data

    # Get the coordinate system from the metadata.
    if 'cs' in vertex_array.metadata:
        coordinate_system = CoordinateSystem(int(vertex_array.metadata['cs']))
    else:
        coordinate_system = _convert_nifti_code_to_coord_sys(
            vertex_array.coordsys.dataspace)

    # Get the triangles array. If there is more than one, warn the user and
    # use the first one.
    triangle_arrays = gii.get_arrays_from_intent('NIFTI_INTENT_TRIANGLE')

    if len(triangle_arrays) == 0:
        raise ValueError('The file {} does not contain any triangles.'
                         .format(filename))

    elif len(triangle_arrays) > 1:
        warnings.warn('The file {} contains more than one triangle array. '
                      'The first one was used. Proceed with caution.'
                      .format(filename),
                      RuntimeWarning)

    triangles = triangle_arrays[0].data

    # Get the normals array if it exists.
    normals_arrays = gii.get_arrays_from_intent('NIFTI_INTENT_VECTOR')
    if len(normals_arrays) > 0:
        if len(normals_arrays) != 1:
            warnings.warn('The file {} contains more than one vector array. '
                          'The first one was interpreted as mesh normals. '
                          'Proceed with caution.'.format(filename))

        normals = normals_arrays[0].data

    else:
        normals = None

    # Create the mesh.
    mesh = Mesh(vertices, triangles, coordinate_system, normals)

    # Add the transform if one was saved.
    transform = _get_transform_from_vertex_array(vertex_array)
    if transform is not None:
        mesh.add_transform(transform)

    # Add the segmentation if one was saved.
    segmentation = _get_segmentation_from_gii(gii)
    if segmentation is not None:
        mesh.add_segmentation(segmentation)

    # Add the vertex data if any was saved.
    for vertex_data in _get_vertex_data_from_gii(gii):
        mesh.add_vertex_data(vertex_data)

    return mesh


def load_segmentation(filename: str) -> Segmentation:
    """Loads a segmentation from a GIfTI file.

    Loads the segmentation of a mesh from a GIfTI file without loading the
    mesh data.

    Args:
        filename: The name of the file from which to load the segmentation.

    Returns:
        segmentation: The segmentation loaded from the GIfTI file.

    Raises:
        ValueError: If the file does not contain a segmentation.

    """

    gii = nib.load(filename)

    segmentation = _get_segmentation_from_gii(gii)

    if segmentation is None:
        raise ValueError('The file {} does not contain any segmentation data.'
                         .format(filename))

    return segmentation


def load_vertex_data(filename: str) -> VertexData:
    """Loads per vertex data

    Loads per vertex data from a GIfTI file without loading any other
    mesh information.

    Args:
         filename: The name of the file from which to load the data.

    Returns:
        The vertex data contained in the file.

    """

    gii = nib.load(filename)
    vertex_data_list = _get_vertex_data_from_gii(gii)

    if len(vertex_data_list) == 0:
        raise ValueError('The file {} does not contain any vertex data.'
                         .format(filename))
    elif len(vertex_data_list) > 1:
        warnings.warn('The file {} contains more than one vertex data. Only '
                      'the first was loaded. Proceed with caution.'
                      .format(filename))

    return vertex_data_list[0]


def save(filename: str, mesh: Mesh):
    """Save a mesh to a GIfTI file.

    Saves the mesh and its metadata to a GIfTI file.

    Args:
        filename: The name of the file were the mesh will be saved. If it
            exists, it will be overwritten.
        mesh: The mesh to save.
        anatomical_structure_primary (optional): The tag of the primary
            anatomical structure for workbench.
        anatomical_structure_secondary (optional): The tag of the secondary
            anatomical structure for workbench.
        geometric_type (optional): The geometric type for workbench.

    """

    gii = nib.gifti.GiftiImage()

    # The GIfTI file format only allows saving one segmentation. If the mesh
    # contains more that one, warn the user and save only the first one.
    segmentations = mesh.segmentations
    if len(segmentations) > 1:
        warnings.warn('The mesh has more that one segmentation, but GIfTI '
                      'only supports one segmentation per file. Only the '
                      'first segmentation will be saved.')

    if len(segmentations) != 0:
        _add_segmentation_to_gii(segmentations[0], gii)

    # Add the vertices and triangles to the mesh.
    _add_mesh_to_gii(mesh, gii)

    # Save the normals if they exist.
    if mesh.normals is not None:
        normals_array = nib.gifti.GiftiDataArray(
            mesh.normals.astype('f4'),
            intent='NIFTI_INTENT_VECTOR',
            datatype='NIFTI_TYPE_FLOAT32')
        gii.add_gifti_data_array(normals_array)

    # Save the vertex data if there is any.
    for vertex_data in mesh.vertex_data:
        _add_vertex_data_to_gii(vertex_data, gii)

    nib.save(gii, filename)


def save_mesh(filename: str, mesh: Mesh):
    """Saves a mesh into a GIfTI file

    Saves the vertices and triangles of a mesh into a GIfTI file without
    adding any other information. This is useful to save files compatible
    with Connectome Workbench which expects meshes, segmentations,
    and vertex data in separate files.

    Args:
        filename: The name of the file where the segmentation is saved. If
            it already exists, it will be overwritten.
        mesh: The mesh to save to the file.

    """

    # Create a bare bone GIfTI with only the mesh vertices and triangles and
    # save it.
    gii = nib.gifti.GiftiImage()
    _add_mesh_to_gii(mesh, gii)
    nib.save(gii, filename)


def save_segmentation(filename: str,
                      segmentation: Segmentation,
                      anatomical_structure_primary: str = 'Cortex',
                      anatomical_structure_secondary: str = 'GrayWhite',
                      geometric_type: str = 'Anatomical'):
    """Save a segmentation to a GIfTI image.

    Save a the segmentation of a mesh into a GIfTI file without saving the
    mesh itself.

    Args:
        filename: The name of the file where the segmentation is saved. If
            it exists, it will be overwritten.
        segmentation: The segmentation to save.
        anatomical_structure_primary: The name of the primary anatomical
            structure the segmentation refers to. For workbench.
        anatomical_structure_secondary: The name of the secondary anatomical
            structure the segmentation refers to. For workbench.
        geometric_type: The geometric type of the structure. For workbench.

    """

    gii = nib.gifti.GiftiImage()

    # In a label file, the meta data of the structure is in the
    # meta of the file.
    gii.meta.data.append(
        nib.gifti.GiftiNVPairs('AnatomicalStructurePrimary',
                               anatomical_structure_primary))
    gii.meta.data.append(
        nib.gifti.GiftiNVPairs('AnatomicalStructureSecondary',
                               anatomical_structure_secondary))
    gii.meta.data.append(
        nib.gifti.GiftiNVPairs('GeometricType',
                               geometric_type))

    _add_segmentation_to_gii(segmentation, gii)

    nib.save(gii, filename)


def save_vertex_data(filename: str, vertex_data: VertexData):
    """Saves per vertex data

    Saves per vertex data to a GIfTI file without any other mesh
    information. This is useful to generate maps used by workbench.

    Args:
        filename: The name of the file where the vertex data will be saved.
            To be compatible with workbench, the file name should end with
            .func.gii.
        vertex_data: The vertex data to save.

    """

    gii = nib.gifti.GiftiImage()
    _add_vertex_data_to_gii(vertex_data, gii)
    nib.save(gii, filename)


def _add_mesh_to_gii(mesh: Mesh, gii: nib.gifti.GiftiImage):
    """Adds a mesh to a nibabel GIfTI object

    Adds the vertices and triangles of a mesh to a GIfTI object by adding
    two new data arrays.

    Args:
        mesh: The mesh that contains the vertices and triangles to add.
        gii: The GIfTI object where the segmentation is added.

    """

    # The coordinate system is saved in the metadata of the vertex array.
    # Because it is possible to save the coordinate system of the points
    # without having a transform, we add it to the metadata.
    meta = {
        'cs': str(mesh.coordinate_system.value)
    }

    # For now, the GIfTI implementation of nibabel seems to support only a
    # single transform. If the mesh has more than one, warn the user and
    # save the first one.
    transforms = mesh.transforms
    if len(transforms) > 1:
        warnings.warn('The mesh has more than one transform but GIfTI only '
                      'supports a single transform. Only the first one will '
                      'be saved.')

    if len(transforms) != 0:
        transform = transforms[0]
        coordinate_system = nib.gifti.GiftiCoordSystem(
            _convert_coord_sys_to_nifti_code(mesh.coordinate_system),
            _convert_coord_sys_to_nifti_code(transform.transform_coord_sys),
            transform.affine)
        meta['tcs'] = str(transform.transform_coord_sys.value)
    else:
        coordinate_system = None

    vertices_array = nib.gifti.GiftiDataArray(
        mesh.vertices.astype('f4'),
        intent='NIFTI_INTENT_POINTSET',
        datatype='NIFTI_TYPE_FLOAT32',
        meta=meta,
        coordsys=coordinate_system
    )

    gii.add_gifti_data_array(vertices_array)

    triangles_array = nib.gifti.GiftiDataArray(
        mesh.triangles.astype('i4'),
        intent='NIFTI_INTENT_TRIANGLE',
        datatype='NIFTI_TYPE_INT32')
    gii.add_gifti_data_array(triangles_array)


def _add_segmentation_to_gii(segmentation: Segmentation,
                             gii: nib.gifti.GiftiImage):
    """Adds a segmentation to a nibabel GIfTI object.

    Add the segmentation data to a nibabel GIfTI object by adding a new data
    array.

    Args:
        segmentation: The segmentation to add to the GIfTI object.
        gii: The GIfTI object where the segmentation is added.

    """

    # Save the name of the segmentation in the metadata of the array.
    meta = nib.gifti.GiftiMetaData.from_dict({'name': segmentation.name})

    label_array = nib.gifti.GiftiDataArray(
        segmentation.keys,
        intent='NIFTI_INTENT_LABEL',
        datatype='NIFTI_TYPE_INT32',
        meta=meta)

    gii.add_gifti_data_array(label_array)

    # Add the labels of the segmentation.
    gii_label_table = nib.gifti.GiftiLabelTable()
    for key, label in segmentation.labels.items():

        # The color in a GIfTI is saved as a float.
        color = np.array(label.color) / 255

        # Create the GIfTI label. It requires both a label and a key
        # attribute to be added dynamically, although this is mentioned
        # nowhere.
        gii_label = nib.gifti.GiftiLabel(key, *color)
        gii_label.label = label.name
        gii_label.key = key
        gii_label_table.labels.append(gii_label)

    gii.labeltable = gii_label_table


def _add_vertex_data_to_gii(vertex_data: VertexData,
                            gii: nib.gifti.GiftiImage):
    """Adds per vertex data to a nibabel GIfTI object

    Args:
        vertex_data: The vertex data to add.
        gii: The GIfTI object where the segmentation is added.

    """

    vertex_data_array = nib.gifti.GiftiDataArray(
        vertex_data.data.astype('f4'),
        intent='NIFTI_INTENT_ESTIMATE',
        datatype='NIFTI_TYPE_FLOAT32',
        meta={'name': vertex_data.name})
    gii.add_gifti_data_array(vertex_data_array)


def _convert_coord_sys_to_nifti_code(coord_sys: CoordinateSystem) -> int:
    """Converts coordinate systems to NIfTI xform codes"""

    convert = {
        CoordinateSystem.UNKNOWN: 0,
        CoordinateSystem.SCANNER: 1,
        CoordinateSystem.RAS: 2,
        CoordinateSystem.LPS: 2,
        CoordinateSystem.VOXEL: 0,
        CoordinateSystem.MNI: 4,
        CoordinateSystem.TALAIRACH: 3,
    }

    return convert[coord_sys]


def _convert_nifti_code_to_coord_sys(code: int) -> CoordinateSystem:
    """Converts a NIfTI xform code to a coordinate system"""

    convert = {
        0: CoordinateSystem.UNKNOWN,
        1: CoordinateSystem.SCANNER,
        2: CoordinateSystem.UNKNOWN,
        3: CoordinateSystem.TALAIRACH,
        4: CoordinateSystem.MNI,
    }

    return convert[code]


def _get_segmentation_from_gii(gii) -> Segmentation:
    """Creates a segmentation from a nibabel GIfTI object.

    Creates a new segmentation from the data array of a nibabel GIfTI
    object. If none of the data arrays have an intent of NIFTI_INTENT_LABEL,
    None is returned.

    Args:
        gii: The nibabel GIfTI object from which to create the segmentation.

    Returns:
        segmentation: The loaded segmentation or None.

    """

    # Get the labels array. If there is more than one, warn the user and
    # use the first one.
    label_arrays = gii.get_arrays_from_intent('NIFTI_INTENT_LABEL')

    if len(label_arrays) == 0:
        return None

    elif len(label_arrays) > 1:
        warnings.warn('The file contains more than one label array. The '
                      'first one was used. Proceed with caution.',
                      RuntimeWarning)
    label_array = label_arrays[0]
    labels = label_array.data

    # If a segmentation name was not saved, tell the user and give it a name.
    if 'name' in label_array.metadata:
        name = label_array.metadata['name']
    else:
        warnings.warn('The name of the segmentation was not saved. Naming '
                      'it as "unknown".')
        name = 'unknown'

    segmentation = Segmentation(name, labels)

    # Add the labels.
    for label in gii.labeltable.labels:

        # Convert the color back to integers.
        color = np.round(np.array(label.rgba) * 255).astype(int)
        segmentation.add_label(label.key, Label(label.label, color))

    return segmentation


def _get_vertex_data_from_gii(
        gii: nib.gifti.GiftiImage) -> List[VertexData]:
    """Returns the per vertex data contains in a GIfTI object"""

    vertex_datas = []

    vertex_data_arrays = gii.get_arrays_from_intent('NIFTI_INTENT_ESTIMATE')
    for vertex_data_array in vertex_data_arrays:

        if 'name' not in vertex_data_array.meta.metadata:
            warnings.warn('The file contains a vertex data array without '
                          'a name. It was ignored.')
            continue

        vertex_datas.append(VertexData(vertex_data_array.meta.metadata['name'],
                                       vertex_data_array.data))

    return vertex_datas


def _get_transform_from_vertex_array(vertex_array)\
        -> Union[AffineTransform, None]:
    """Gets the affine transform from a GIfTI vertex array"""

    # GIfTI always contain a transform.
    gifti_transform = vertex_array.coordsys

    # If the metadata of the vertex array contains the key 'tcs',
    # use it to create the transform. If is doesn't, only add the
    # transform if the dataspace and xformspace are not identical.
    if 'tcs' in vertex_array.metadata:
        transform = AffineTransform(
            CoordinateSystem(int(vertex_array.metadata['tcs'])),
            gifti_transform.xform)

    elif gifti_transform.dataspace != gifti_transform.xformspace:
        transform = AffineTransform(
            _convert_nifti_code_to_coord_sys(gifti_transform.xformspace),
            gifti_transform.xform)

    else:
        transform = None

    return transform
