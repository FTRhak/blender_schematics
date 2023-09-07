from bpy.types.bpy_struct import bpy_struct
from bpy.types.node import Node

class NodeSocket(bpy_struct):
    bl_idname: str
    bl_label: str
    bl_subtype_label: str
    description: str
    display_shape: any
    enabled: bool
    hide: bool
    hide_value: bool
    identifier: str
    is_linked: bool
    is_multi_input: bool
    is_output: bool
    is_unavailable: bool
    label: str
    link_limit: int
    name: str
    node: Node
    show_expanded: bool
    type: any
    links: list[Node]

    def draw(self, context, layout, node: Node, text: str):
        pass

    def draw_color(self, context, node):
        pass

    @classmethod
    def bl_rna_get_subclass(id, default=None):
        pass

    @classmethod
    def bl_rna_get_subclass_py(id, default=None):
        pass