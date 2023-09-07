from node_socket_interface_standard import NodeSocketInterfaceStandard

class NodeSocketInterfaceFloat(NodeSocketInterfaceStandard):
    default_value: float
    max_value: float
    min_value: float

    @classmethod
    def bl_rna_get_subclass(id: str, default=None):
        pass

    @classmethod
    def bl_rna_get_subclass_py(id: str, default=None):
        pass