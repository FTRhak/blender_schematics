bl_info = {
    "name": "Name add-on geometry node",
    "author": "author",
    "version": (0, 0, 1),
    "blender": (3, 6, 2),
    "location": "",
    "description": "",
    "warning": "",
    "doc_url": "",
    "category": "Node",
}


import bpy

class MyCustomNode(bpy.types.GeometryNodeCustomGroup):
    '''This is a custom node that multiplies two inputs and outputs the result.'''

    bl_idname = 'MyCustomNode' # Unique identifier for your node type
    bl_label = 'My custom node' # Display name for your node


    @classmethod
    def poll(cls, context): #mandatory with geonode
        return True

    def init(self, context):
        ng: bpy.types.GeometryNodeTree = bpy.data.node_groups.new(name='group_name', type="GeometryNodeTree")
        in_node = ng.nodes.new("NodeGroupInput")
        in_node.location.x -= 200
        out_node = ng.nodes.new("NodeGroupOutput")
        out_node.location.x += 200

        self.__createInputFields(ng)
        self.__createOutputFields(ng)
        
        self.node_tree = ng

    
    def update(self):
        """generic update function"""

        self.node_tree.nodes["Group Output"].inputs[0].default_value = 30

        # TODO read from input geometry - transform - put in output geometry

        return None
    

    def __createInputFields(self, ng: bpy.types.GeometryNodeTree):
        nm = self.__createInputFiled(ng, 'NodeSocketInt', 'Name of input field')
        self.__setupField(nm, 0, 100, 50)
        self.__createInputFiled(ng, 'NodeSocketGeometry', 'Geometry input field')

    
    def __createOutputFields(self, ng: bpy.types.GeometryNodeTree):
        self.__createOutputFiled(ng, 'NodeSocketInt', 'Name of output field')
        self.__createOutputFiled(ng, 'NodeSocketGeometry', 'Geometry output field')

    def __createInputFiled(self, ng: bpy.types.GeometryNodeTree, filedType: str, filedName: str):
        return ng.inputs.new(filedType, filedName)
    
    def __createOutputFiled(self, ng: bpy.types.GeometryNodeTree, filedType: str, filedName: str):
        return ng.outputs.new(filedType, filedName)
    
    def __setupField(self, field, min, max, default):
        field.min_value = min
        field.max_value = max
        field.default_value = default

class NODE_MT_Menu(bpy.types.Menu):

    bl_idname = "NODE_MT_Menu"
    bl_label = "Genetic Mesh"

    #@classmethod
    #def poll(cls, context):
    #    return (bpy.context.space_data.tree_type == "GeometryNodeTree")

    def draw(self, context):
        layout = self.layout
        op = layout.operator(operator="node.add_node", text="Menu item action name",)
        # set name of class
        op.type = "MyCustomNode"
        op.use_transform = True



def extra_geonode_menu(self, context):
    tnode = context.space_data

    # IF the window space type is Geometry Nodes
    if tnode.tree_type == 'GeometryNodeTree':
        self.layout.separator()
        self.layout.menu('NODE_MT_Menu', text="Name of menu item",)
    
    
        

# Register your node type with Blender

classes = (
    MyCustomNode,
    NODE_MT_Menu,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.NODE_MT_add.append(extra_geonode_menu)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    bpy.types.NODE_MT_add.remove(extra_geonode_menu)

if __name__ == "__main__":
    register()