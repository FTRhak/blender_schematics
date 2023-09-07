from id import ID
from anim_data import AnimData
from bpy.types.bpy_prop_collection import bpy_prop_collection
from nodes import Nodes
from node_tree_inputs import NodeTreeInputs
from node_tree_outputs import NodeTreeOutputs
from mathutils import Vector

# https://docs.blender.org/api/current/bpy.types.NodeTree.html

class NodeTree(ID):
    active_input: int
    active_output: int
    animation_data: AnimData
    bl_description: str
    bl_icon: any
    bl_idname: str
    bl_label: str
    grease_pencil: any
    inputs: bpy_prop_collection[NodeTreeInputs]
    links: bpy_prop_collection[any]
    nodes: Nodes
    outputs: bpy_prop_collection[NodeTreeOutputs]
    type: any
    view_center: list[Vector]

    def interface_update(self, context):
        pass

    def contains_tree(self, sub_tree: any) -> bool:
        pass

    @classmethod
    def poll(context) -> bool:
        pass

    def update(self):
        pass

    @classmethod
    def get_from_context(context) -> any:
        pass

    @classmethod
    def valid_socket_type(idname) -> bool:
        pass

    @classmethod
    def bl_rna_get_subclass(id: str, default=None):
        pass

    @classmethod
    def bl_rna_get_subclass_py(id: str, default=None):
        pass
