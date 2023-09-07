from bpy.types.bpy_struct import bpy_struct

# https://docs.blender.org/api/current/bpy.types.Struct.html#bpy.types.Struct
class Struct(bpy_struct):
    base: any
    description: str
    functions: any
    identifier: str
    name: str
    name_property: any
    nested: any
    properties: any
    property_tags: any
    translation_context: str

    @classmethod
    def bl_rna_get_subclass(id: str, default=None):
        pass

    @classmethod
    def bl_rna_get_subclass_py(id: str, default=None):
        pass
