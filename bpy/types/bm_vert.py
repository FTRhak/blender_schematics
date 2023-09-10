from mathutils import Vector
from typing import Type

# https://docs.blender.org/api/current/bmesh.types.html#bmesh.types.BMVert

class BMVert():
    co: Vector
    hide: bool
    index: int
    is_boundary: bool
    is_manifold: bool
    is_valid: bool
    is_wire: bool
    link_edges: any
    link_faces: any
    link_loops: any
    normal: Vector
    select: bool
    tag: bool
    
    def new(self, vertex: any) -> Type['BMVert'] :
        pass

    def calc_edge_angle(self, fallback=None) -> float:
        pass

    def calc_shell_factor(self) -> float:
        pass

    def copy_from(self, other):
        pass

    def copy_from_face_interp(self, face: any):
        pass

    def copy_from_vert_interp(self, vert_pair, fac):
        pass

    def hide_set(self, hide: bool):
        pass

    def normal_update(self):
        pass

    def select_set(self, select: bool):
        pass