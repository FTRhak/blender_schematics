from mathutils import Color, Vector
from bpy.types.bpy_struct import bpy_struct
from bpy.types.ui_layout import UILayout
from node_outputs import NodeOutputs
from node_inputs import NodeInputs
from bpy.types.bpy_prop_collection import bpy_prop_collection

class Node(bpy_struct):
    bl_description: str
    bl_height_default: float
    bl_height_max: float
    bl_height_min: float
    bl_icon: any
    bl_idname: str
    bl_label: str
    bl_static_type: any
    bl_width_default: float
    bl_width_max: float
    bl_width_min: float
    color: Color
    dimensions: Vector
    height: float
    hide: bool
    inputs: bpy_prop_collection[NodeInputs]
    internal_links: any
    label: str
    location: Vector
    mute: bool
    name: str
    outputs: bpy_prop_collection[NodeOutputs]
    parent: any
    select: bool
    show_options: bool
    show_preview: bool
    show_texture: bool
    type: any
    use_custom_color: bool
    width: float
    width_hidden: float

    def socket_value_update(self, context):
        pass

    @classmethod
    def is_registered_node_type():
        pass
    
    @classmethod
    def poll(node_tree):
        pass

    def poll_instance(self, node_tree):
        pass

    def update(self):
        pass

    def insert_link(self, link):
        pass

    def init(self, context):
        pass

    def copy(self, node):
        pass

    def free(self):
        pass

    def draw_buttons(self, context, layout: UILayout):
        pass

    def draw_buttons_ext(self, context, layout: UILayout):
        pass

    def draw_label(self):
        pass

    @classmethod
    def bl_rna_get_subclass(id: str, default=None):
        pass

    @classmethod
    def bl_rna_get_subclass_py(id: str, default=None):
        pass