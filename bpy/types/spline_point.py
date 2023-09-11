from bpy.types.bpy_struct import bpy_struct
from mathutils import Vector

# https://docs.blender.org/api/current/bpy.types.SplinePoint.html

class SplinePoint(bpy_struct):
    co: Vector
    hide: bool
    radius: float
    select: bool
    tilt: float
    weight: float
    weight_softbody: float
