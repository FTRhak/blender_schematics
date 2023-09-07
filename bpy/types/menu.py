from bpy.types.bpy_struct import bpy_struct
from bpy.types.ui_layout import UILayout

class Menu(bpy_struct):
    bl_description: str
    bl_idname: str
    bl_label: str
    bl_owner_id: str
    bl_translation_context: str
    layout: UILayout

    @classmethod
    def poll(node_tree):
        pass

    def draw(self, context):
        pass

    def draw_preset(self, context):
        pass

    def path_menu(searchpaths, operator, *, props_default=None, prop_filepath='filepath', filter_ext=None, filter_path=None, display_name=None, add_operator=None):
        pass

    @classmethod
    def bl_rna_get_subclass(id, default=None):
        pass

    @classmethod
    def bl_rna_get_subclass_py(id, default=None):
        pass
