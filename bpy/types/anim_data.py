from bpy.types.bpy_struct import bpy_struct

# https://docs.blender.org/api/current/bpy.types.AnimData.html

class AnimData(bpy_struct):
    action: any
    action_blend_type: any
    action_extrapolation: any
    action_influence: float
    action_tweak_storage: any
    drivers: any
    nla_tracks: any
    use_nla: bool
    use_pin: bool
    use_tweak_mode: bool

    def nla_tweak_strip_time_to_scene(self, frame, invert=False) -> float:
        pass

    @classmethod
    def bl_rna_get_subclass(id: str, default=None):
        pass

    @classmethod
    def bl_rna_get_subclass_py(id: str, default=None):
        pass

