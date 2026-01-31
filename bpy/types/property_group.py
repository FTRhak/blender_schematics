from bpy.types.bpy_struct import bpy_struct

# https://docs.blender.org/api/current/bpy.types.PropertyGroup.html

class PropertyGroup(bpy_struct):
    name: str

    def bl_system_properties_get(self, do_create: bool = False) -> any:
        pass

    @classmethod
    def bl_rna_get_subclass(id: str, default=None):
        pass

    @classmethod
    def bl_rna_get_subclass_py(id: str, default=None):
        pass