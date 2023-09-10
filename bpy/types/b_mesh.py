from mesh import Mesh
from object import Object
from bm_vert import BMVert
from bm_face_seq import BMFaceSeq
from mathutils import Matrix

# https://docs.blender.org/api/current/bmesh.types.html

class BMesh():
    edges: any
    faces: BMFaceSeq
    is_valid: bool
    is_wrapped: bool
    loops: any
    select_history: any
    select_mode: set
    verts: BMVert

    def calc_loop_triangles(self) -> any:
        pass

    def calc_volume(self, signed=False) -> float:
        pass

    def clear(self):
        pass

    def copy(self) -> any:
        pass

    def free(self):
        pass

    def from_mesh(self, mesh: Mesh, face_normals=True, vertex_normals=True, use_shape_key=False, shape_key_index=0):
        pass

    def from_object(self, object: Object, depsgraph, cage=False, face_normals=True, vertex_normals=True):
        pass

    def normal_update(self):
        pass

    def select_flush(self, elect: bool):
        pass

    def select_flush_mode(self):
        pass

    def to_mesh(self, mesh: Mesh):
        pass

    def transform(self, matrix: Matrix, filter: set=None):
        pass