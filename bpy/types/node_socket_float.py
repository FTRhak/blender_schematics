from  node_socket_standard import NodeSocketStandard

# https://docs.blender.org/api/current/bpy.types.NodeSocketFloat.html

class NodeSocketFloat(NodeSocketStandard):
    default_value: float
    links: any

    @classmethod
    def bl_rna_get_subclass(id: str, default=None):
        pass

    @classmethod
    def bl_rna_get_subclass_py(id: str, default=None):
        pass