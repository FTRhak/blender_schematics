from mathutils import Vector
from typing import Type

class BMFace():
    edges: any
    hide: bool
    index: int
    is_valid: bool
    loops: any
    material_index: int
    normal: Vector
    select: bool
    smooth: bool
    tag: bool
    verts: any

    def calc_area(self) -> float:
        pass

    def calc_center_bounds(self) -> Vector:
        pass

    def calc_center_median(self) -> Vector:
        pass

    def calc_center_median_weighted(self) -> Vector:
        pass

    def calc_perimeter(self) -> float:
        pass

    def calc_tangent_edge(self) -> Vector:
        pass

    def calc_tangent_edge_diagonal(self) -> Vector:
        pass

    def calc_tangent_edge_pair(self) -> Vector:
        pass

    def calc_tangent_vert_diagonal(self) -> Vector:
        pass

    def copy(self, verts=True, edges=True) -> Type['BMFace']:
        pass

    def copy_from(self, other):
        pass

    def copy_from_face_interp(self, face: Type['BMFace'], vert=True):
        pass

    def hide_set(self, hide: bool):
        pass

    def normal_flip(self):
        pass

    def normal_update(self):
        pass

    def select_set(self, select: bool):
        pass

