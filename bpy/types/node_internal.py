
from bpy.types.node import Node

class NodeInternal(Node):

    @classmethod
    def poll(node_tree):
        pass

    def poll_instance(self, node_tree):
        pass

    def update(self):
        pass

    def draw_buttons(self, context, layout):
        pass

    def draw_buttons_ext(self, context, layout):
        pass

    @classmethod
    def bl_rna_get_subclass(id, default=None):
        pass

    @classmethod
    def bl_rna_get_subclass_py(id, default=None):
        pass
