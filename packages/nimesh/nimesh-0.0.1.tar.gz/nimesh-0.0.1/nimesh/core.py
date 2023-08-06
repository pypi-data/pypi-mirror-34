import numpy as np
from enum import IntEnum
from typing import List, Sequence, Union

from scipy.sparse import csr_matrix

from nimesh.asarray import adjacency_matrix
from nimesh.mixins import Named, ListOfNamed


class AffineTransform(object):

    def __init__(self, transform_coord_sys: 'CoordinateSystem',
                 affine: Sequence):
        """Affine transformation from one coordinate system to another.

        The AffineTransform represents an affine transformation to a new
        stereotaxic space.

        Args:
            transform_coord_sys: The coordinate system of the data after the
                application of the affine transformation.
            affine: The affine transform as a numpy array with a shape of
                (4, 4).

        Raises:
            TypeError: If the affine is none or not convertible to a a numpy
                array of floats.
            ValueError: If the affine does not have a shape of (4, 4).

        Examples:

            Create an affine transform to scanner space.

            >>> import numpy as np
            >>> from nimesh import AffineTransform, CoordinateSystem
            >>> affine = np.eye(4)
            >>> transform = AffineTransform(CoordinateSystem.SCANNER, affine)

        """

        # The affine must be convertible to a numpy array with a shape of
        # (4, 4).
        if affine is None:
            raise TypeError('\'affine\' cannot be None.')

        try:
            affine = np.array(affine, dtype=np.float64)
        except Exception:
            raise TypeError('\'affine\' must be convertible to a numpy array '
                            'of floats.')

        if affine.ndim != 2 or affine.shape != (4, 4):
            raise ValueError('\'affine\' must have a shape of (4, 4), '
                             'not {}.'.format(affine.shape))

        self._affine = affine
        self._transform_coord_sys = transform_coord_sys

    @property
    def affine(self) -> np.array:
        """Returns the affine transform as a numpy array."""
        return self._affine.copy()

    @property
    def transform_coord_sys(self) -> 'CoordinateSystem':
        """Returns the coord. system after the application of the affine."""
        return self._transform_coord_sys


class CoordinateSystem(IntEnum):
    """The possible coordinate systems of meshes."""
    UNKNOWN = 0
    SCANNER = 1
    RAS = 2
    LPS = 3
    VOXEL = 4
    MNI = 5
    TALAIRACH = 6


class Label(Named):

    def __init__(self, name: str, color: Sequence[int] = (0, 0, 0, 0)):
        """One label of a segmentation.

        The Label class represents the data of one label of a segmentation.
        Within a segmentation, each label and each vertex are assigned a
        key creating a mapping between vertices and label data.

        Args:
            name: The name of the label, for example: left superior frontal.
        """

        super().__init__(name)

        self._color = tuple(color)

    @property
    def color(self):
        """Returns the color of the label."""
        return self._color


class Mesh(object):

    def __init__(
            self, vertices: Sequence, triangles: Sequence,
            coordinate_system: CoordinateSystem = CoordinateSystem.UNKNOWN,
            normals: Sequence = None):
        """Triangle mesh of the cortical surface.

        The Mesh class represents a polygon mesh of the cortical surface
        defined by vertices and triangles.

        Args:
            vertices: The vertices of the mesh. Must a sequence that can be
                converted to a numpy array of floats with a shape of (N, 3)
                where N is the number of vertices.
            triangles: The triangles of the mesh. Must be a sequence that
                can be converted to a numpy array of integers with a shape of
                (M, 3) where M is the number of triangles.
            coordinate_system (optional): The coordinate system of the
                vertices (see CoordinateSystem). Defaults to VOXEL.
            normals (optional): The normals of the vertices. Must be a sequence
                that can be converted to a numpy array of floats with a
                shape of (N, 3) where N is the number of vertices.

        Raises:
            TypeError: If vertices or triangles cannot be converted to numpy
                arrays.
            TypeError: If coordinate_system is not a CoordinateSystem member
                value.
            ValueError: If vertices or triangles do not have a shape of (N, 3)
                and (M, 3), respectively.

        Examples:
            Create a mesh with a single triangle.

            >>> from nimesh import Mesh
            >>> vertices = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            >>> triangles = [[0, 1, 2]]
            >>> mesh = Mesh(vertices, triangles)
            >>> print(mesh)
            Mesh: 3 vertices, 1 triangles

        """

        self._vertices = None

        # Special case of vertices or triangles set to None.
        if triangles is None:
            raise TypeError('\'triangles\' cannot be None')

        try:
            triangles = np.array(triangles, dtype=np.int64)
        except Exception:
            raise TypeError('\'triangles\' must be convertible to a numpy '
                            'array of integers.')

        if triangles.ndim != 2 or triangles.shape[1] != 3:
            raise ValueError('\'triangles\' must have a shape of (M, 3) not '
                             '{}.'.format(triangles.shape))

        if not isinstance(coordinate_system, CoordinateSystem):
            raise TypeError('\'coordinate_system\' must be a member value of '
                            'CoordinateSystem, not a {}.'
                            .format(type(coordinate_system)))

        self.vertices = vertices
        self._triangles = triangles
        self._coordinate_system = coordinate_system

        self._transforms = []
        self._segmentations = ListOfNamed()

        self._normals = None
        self.normals = normals

        self._vertex_data = ListOfNamed()

    def __repr__(self) -> str:
        return 'Mesh: {} vertices, {} triangles'.format(self.nb_vertices,
                                                        self.nb_triangles)

    @property
    def adjacency_matrix(self) -> csr_matrix:
        """Returns the adjacency matrix of the mesh

        Returns a boolean scipy.sparse.csr_matrix with a shape of (N, N) where
        N is the number of vertices of the mesh. The element (i, j) is True
        if the vertices i and j share a triangle and False elsewhere. To
        transform the matrix to a dense numpy array, use the `todense`
        method of the returned matrix.

        """

        return adjacency_matrix(self.triangles, self.nb_vertices)

    @property
    def coordinate_system(self) -> CoordinateSystem:
        """Returns the coordinate system of the mesh."""
        return self._coordinate_system

    @coordinate_system.setter
    def coordinate_system(self, coordinate_system):
        """Sets the coordinate system of the mesh"""

        if len(self._transforms) != 0:
            raise ValueError('The mesh contains transforms. The coordinate '
                             'system cannot be changed.')

        if not isinstance(coordinate_system, CoordinateSystem):
            raise TypeError('The coordinate system must be an instance of '
                            '{}, not {}.'
                            .format(CoordinateSystem, type(coordinate_system)))

        self._coordinate_system = coordinate_system

    @property
    def nb_triangles(self) -> int:
        """Returns the number of triangles of the mesh."""
        return len(self._triangles)

    @property
    def nb_vertices(self) -> int:
        """Returns the number of vertices of the mesh."""
        return len(self._vertices)

    @property
    def normals(self) -> Union[np.ndarray, None]:
        """Returns the normals of the mesh or None."""

        if self._normals is None:
            return None

        return self._normals.copy()

    @normals.setter
    def normals(self, normals: Sequence):
        """Sets the normals of the mesh."""

        if normals is None:
            self._normals = None
            return

        try:
            normals = np.array(normals, dtype=np.float64)
        except Exception:
            raise TypeError('\'normals\' must be convertible to a numpy '
                            'array of floats.')

        if normals.ndim != 2 or normals.shape[1] != 3:
            raise ValueError('\'normals\' must have a shape of (N, 3) not '
                             '{}.'.format(normals.shape))

        # The number of normals must match the number of vertices.
        if len(normals) != self.nb_vertices:
            raise ValueError('The number of normals must match the '
                             'number of vertices ({} != {}).'
                             .format(len(normals), self.nb_vertices))

        self._normals = normals

    @property
    def segmentations(self) -> ListOfNamed:
        """Returns the segmentations of the mesh."""
        return self._segmentations.copy()

    @property
    def transforms(self) -> List[AffineTransform]:
        """Returns the available transform to other coordinate systems."""
        return self._transforms.copy()

    @property
    def triangles(self) -> np.array:
        """Returns a copy of the mesh's triangles."""
        return self._triangles.copy()

    @property
    def vertex_data(self) -> ListOfNamed:
        """Returns the vertex data of the mesh"""
        return self._vertex_data.copy()

    @property
    def vertices(self) -> np.array:
        """Returns a copy of the mesh's vertices."""
        return self._vertices.copy()

    @vertices.setter
    def vertices(self, vertices):
        """Sets the vertices of the mesh"""

        if vertices is None:
            raise TypeError('\'vertices\' cannot be None')

        # Try to convert the vertices and triangles to numpy arrays.
        try:
            vertices = np.array(vertices, dtype=np.float64)
        except Exception:
            raise TypeError('\'vertices\' must be convertible to a numpy '
                            'array of floats.')

        # The shape of vertices and triangles must be (?, 3).
        if vertices.ndim != 2 or vertices.shape[1] != 3:
            raise ValueError('\'vertices\' must have a shape of (N, 3) not '
                             '{}.'.format(vertices.shape))

        # The number of new vertices must match the old number of vertices.
        if self._vertices is not None and len(vertices) != self.nb_vertices:
            raise ValueError('Changing the number of vertices is not '
                             'permitted ({} != {}).'
                             .format(len(vertices), self.nb_vertices))

        self._vertices = vertices.copy()

    def add_segmentation(self, segmentation: 'Segmentation'):
        """Adds a segmentation to the mesh.

        Args:
            segmentation: The segmentation of the mesh to add.

        Raises:
            TypeError: If segmentation is not an instance of Segmentation.
            ValueError: If a segmentation with the same name already exists.

        """

        if not isinstance(segmentation, Segmentation):
            raise TypeError('\'segmentation\' must be an instance of '
                            'Segmentation, not {}.'
                            .format(type(segmentation)))

        if segmentation.name in [s.name for s in self._segmentations]:
            raise ValueError('A segmentation with the name {} already exists '
                             'in the mesh.'
                             .format(segmentation.name))

        self._segmentations.append(segmentation)

    def add_transform(self, transform: AffineTransform):
        """Adds a transform to a new coordinate system.

        Adds a new transform to the mesh that takes it from its current
        coordinate system to another.

        Args:
            transform: The affine transform from the current coordinate system
                to a new one.

        Raises:
            TypeError: If the transform is not an AffineTransform.
            ValueError: If a transform to the new coordinate system already
                exists or if the transform is to the current coordinate system.

        """

        if not isinstance(transform, AffineTransform):
            raise TypeError('\'transform\' must be an instance of '
                            'AffineTransform, not {}.'
                            .format(type(transform)))

        # Verify if the transform is to a new coordinate system.
        if transform.transform_coord_sys == self.coordinate_system:
            raise ValueError('A transform to the current coordinate system '
                             'cannot be added.')

        # Verify if there is already a transform to this coordiante system.
        targets = [t.transform_coord_sys for t in self._transforms]
        if transform.transform_coord_sys in targets:
            raise ValueError('A transform to {} already exists.'
                             .format(transform.transform_coord_sys))

        self._transforms.append(transform)

    def add_vertex_data(self, vertex_data: 'VertexData'):
        """Adds vertex data to the mesh

        Args:
            vertex_data: The vertex data to add. The name of this data must
                be distinct from the data already associated with the mesh. The
                length of the data must also match the number of vertices of
                the mesh.

        Raises:
            TypeError if vertex_data is not an instance of VertexData.
            ValueError if the mesh already has vertex data with the same name.
            ValueError if the length of the data does not match the number
                of vertices of the mesh.

        """

        if not isinstance(vertex_data, VertexData):
            raise TypeError('\'vertex_data\' must be an instance of '
                            'VertexData, not {}.'.format(type(vertex_data)))

        if vertex_data.name in [vd.name for vd in self._vertex_data]:
            raise ValueError('The mesh already contains vertex data with the '
                             'name {}.'.format(vertex_data.name))

        if vertex_data.nb_vertices != self.nb_vertices:
            raise ValueError('The number of vertices of the mesh does not '
                             'match the number of vertices of the data '
                             '({} != {}).'.format(vertex_data.nb_vertices,
                                                  self.nb_vertices))

        self._vertex_data.append(vertex_data)

    def transform_to(self, coordinate_system: CoordinateSystem):
        """Transforms the mesh to a another coordinate system.

        Transforms the mesh from its current coordinate system to another. A
        transform to the new coordinate system must have been added to the
        mesh with `add_transform`.

        Args:
             coordinate_system: The target coordinate system.

        Raises:
            ValueError: If no transform to the requested coordinate system
                exits.
        """

        # If we are already in this coordinate system, do nothing.
        if coordinate_system == self.coordinate_system:
            return

        # Get the requested transform.
        transform = next((t for t in self._transforms
                          if t.transform_coord_sys == coordinate_system), None)

        if transform is None:
            raise ValueError('No transform is available to transform to {}.'
                             .format(coordinate_system))

        # Apply the transform to the vertices.
        homogeneous_vertices = np.hstack((self._vertices,
                                          np.ones((self.nb_vertices, 1))))
        new_vertices = np.dot(transform.affine, homogeneous_vertices.T)
        self._vertices = new_vertices[:3, :].T

        # Remove the transform form the list because it is no longer valid.
        self._transforms.remove(transform)

        # Apply inverse of the transform to the other transform so they still
        # project to the correct coordinate system.
        inv = np.linalg.inv(transform.affine)

        def project_transform(t):
            return AffineTransform(t.transform_coord_sys,
                                   np.dot(inv, t.affine))
        self._transforms = [project_transform(t) for t in self._transforms]

        # Add the inverse of the transform to go back to the original
        # coordinate system and the change the current coordinate system.
        new_transform = AffineTransform(self.coordinate_system, inv)
        self._coordinate_system = coordinate_system
        self.add_transform(new_transform)


class Segmentation(Named):

    def __init__(self, name: str, keys: Sequence[int]):
        """Segmentation of a mesh using labels.

        A segmentation of a mesh represented using a list of integers,
        one for each vertex.

        Args:
            name: The name of the segmentation.
            keys: The array of labels of the segmentation, one for each
                voxel. Must be a sequence convertible to a numpy array of
                integers with a shape of (N,).

        Raises:
            TypeError: If the labels cannot be converted to an array of
                integers.
            ValueError: If the labels cannot be converted to an array with a
                shape of (N,).
        """

        super().__init__(name)

        # The keys must be convertible to a numpy array of integers.
        try:
            keys = np.array(keys, np.int32)
        except Exception:
            raise TypeError('\'keys\' must be convertible to a numpy array '
                            'of integers.')

        # The shape of the keys must be (N,).
        if keys.ndim != 1:
            raise ValueError('\'keys\' must have a shape of (N,), not {}.'
                             .format(keys.shape))

        self._keys = keys
        self._labels = {}

    @property
    def keys(self) -> np.array:
        """Returns the key of each vertex of the segmentation."""
        return self._keys.copy()

    @property
    def labels(self) -> dict:
        """Returns a dict of labels."""
        return self._labels.copy()

    def add_label(self, key: int, label: Label):
        """Adds a label to the segmentation.

        Adds a label to the segmentation by associating it with a key.
        Because each vertex is also assigned a key, this creates a mapping
        between vertices and labels.

        Args:
            key: The key of the label.
            label: The label data of the label.

        """

        self._labels[key] = label


class VertexData(Named):
    def __init__(self, name: str, data: Sequence):
        """Vertex data of a mesh

        The vertex data class represents arbitrary data about the vertices
        of a mesh. The data must be convertible to an array of float with a
        shape of (N, M) where N is the number of vertices of the mesh.

        Args:
            name: The name of the vertex data.
            data: The data of each vertex.

        Raises:
            TypeError if the data cannot be converted to a numpy array of
                floats.
            ValueError if the data array does not have a shape of (N, M).

        """

        super().__init__(name)

        self._data = None
        self.data = data

    @property
    def data(self) -> np.ndarray:
        """Returns the data for each vertex"""
        return self._data

    @data.setter
    def data(self, data: Sequence):
        """Sets the data for each vertex

        Modifies the data associated with each vertex. The length of the
        data must match the length of the previous data to prevent changing
        the number of vertices.

        Args:
            data: The data of each vertex. Must be a Sequence convertible to a
                numpy array of floats.

        Raises:
            TypeError if the data cannot be converted to a numpy array of
                floats.
            ValueError if the data array does not have a shape of (N, M).
            ValueError if the length of the data does not match the length
                of the previous data.

        """

        try:
            data = np.array(data, dtype=np.float64)
        except Exception:
            raise TypeError('\'data\' must be convertible to a numpy '
                            'array of floats.')

        if data.ndim == 1:
            data = data[:, None]

        elif data.ndim != 2:
            raise ValueError('\'data\' must have two dimensions, not {}.'
                             .format(data.ndim))

        if self.data is not None and len(data) != self.nb_vertices:
            raise ValueError('The length of \'data\' does not match the '
                             'number of vertices of the previous data '
                             '({} != {}).'.format(len(data), self.nb_vertices))

        self._data = data

    @property
    def nb_vertices(self):
        """Returns the number of vertices associated with the data"""
        return len(self.data)
