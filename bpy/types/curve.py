from typing import Literal, Type
from id import ID
from object import Object
from anim_data import AnimData
from mathutils import Vector, Matrix

# https://docs.blender.org/api/current/bpy.types.Curve.html

class Curve(ID):
    animation_data: AnimData
    bevel_depth: float
    bevel_factor_end: float
    bevel_factor_mapping_end: Literal['RESOLUTION', 'SEGMENTS', 'SPLINE']
    bevel_factor_mapping_start: Literal['RESOLUTION', 'SEGMENTS', 'SPLINE']
    bevel_factor_start: float
    bevel_mode: Literal['ROUND', 'OBJECT', 'PROFILE']
    bevel_object: Object
    bevel_profile: any
    bevel_resolution: int
    cycles: any
    dimensions: Literal['2D', '3D']
    eval_time: float
    extrude: float
    fill_mode: Literal['FULL', 'BACK', 'FRONT', 'HALF']
    is_editmode: bool
    materials: any
    offset: float
    path_duration: int
    render_resolution_u: int
    render_resolution_v: int
    resolution_u: int
    resolution_v: int
    shape_keys: any
    splines: any
    taper_object: any
    taper_radius_mode: Literal['OVERRIDE', 'MULTIPLY', 'ADD']
    texspace_location:Vector
    texspace_size: Vector
    twist_mode: str
    twist_smooth: float
    use_auto_texspace: bool
    use_deform_bounds: bool
    use_fill_caps: bool
    use_map_taper: bool
    use_path: bool
    use_path_clamp: bool
    use_path_follow: bool
    use_radius: bool
    use_stretch: bool

    def transform(self, matrix: Matrix, shape_keys=False):
        pass

    def validate_material_indices(self) -> bool:
        pass

    def update_gpu_tag():
        pass
