from typing import Literal
from bpy.types.bpy_struct import bpy_struct
from spline_point import SplinePoint

# https://docs.blender.org/api/current/bpy.types.Spline.html

class Spline(bpy_struct):
    bezier_points: any
    character_index: int
    hide: bool
    material_index: int
    order_u: int
    order_v: int
    point_count_u: int
    point_count_v: int
    points: list[SplinePoint]
    radius_interpolation: Literal['LINEAR', 'CARDINAL', 'BSPLINE', 'EASE']
    resolution_u: int
    resolution_v: int
    tilt_interpolation: Literal['LINEAR', 'CARDINAL', 'BSPLINE', 'EASE']
    type: Literal['POLY', 'BEZIER', 'NURBS']
    use_bezier_u: bool
    use_bezier_v: bool
    use_cyclic_u: bool
    use_cyclic_v: bool
    use_endpoint_u: bool
    use_endpoint_v: bool
    use_smooth: bool

    def calc_length(self, resolution: int=0) -> float:
        pass

    def valid_message(self, direction: int) -> str:
        pass