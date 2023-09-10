from bpy.types.bpy_struct import bpy_struct

# https://docs.blender.org/api/current/bpy.types.ViewLayer.html

class ViewLayer(bpy_struct):
    active_aov: any
    active_aov_index: int
    active_layer_collection: any
    active_lightgroup: any
    active_lightgroup_index: int
    # TODO not completed