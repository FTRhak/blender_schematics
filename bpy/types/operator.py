from bpy.types.bpy_struct import bpy_struct
from bpy.types.ui_layout import UILayout

# https://docs.blender.org/api/current/bpy.types.Operator.html

class Operator(bpy_struct):
    bl_cursor_pending: any
    bl_idname: str
    bl_label: str
    bl_description: str
    bl_options: set[str]
    bl_translation_context: any
    bl_undo_group: any
    has_reports: bool
    layout: UILayout
    macros: any
    name: str
    options: any
    properties: any
    bl_property: any


    def report(self, type: str, message: str):
        pass

    def is_repeat(self) -> any:
        pass

    def execute(self, context: any) -> any:
        pass

    def check(self, context: any) -> bool:
        pass

    def invoke(self, context: any, event: any) -> any:
        pass

    def modal(self, context: any, event: any) -> any:
        pass

    def draw(self, context: any):
        pass

    def cancel(self, context: any):
        pass

    @classmethod
    def poll(context: any) -> bool:
        pass

    @classmethod
    def description(context: any, properties: any) -> str:
        pass

    def as_keywords(self, ignore: set[str] = set()) -> dict:
        pass

    @classmethod
    def bl_rna_get_subclass(id: str, default=None):
        pass

    @classmethod
    def bl_rna_get_subclass_py(id: str, default=None):
        pass

    @classmethod
    def poll_message_set(message: str, *args):
        pass
