from bpy.types.bpy_struct import bpy_struct
from mesh import Mesh
from object import Object
from depsgraph import Depsgraph

# https://docs.blender.org/api/current/bpy.types.BlendDataMeshes.html

class BlendDataMeshes(bpy_struct):
    def new(self, name: str) -> Mesh:
        pass
    
    def new_from_object(self, object: Object, preserve_all_data_layers=False, depsgraph: Depsgraph = None) -> Mesh:
        pass

    def remove(self, mesh: Mesh, do_unlink=True, do_id_user=True, do_ui_user=True):
        pass

    def tag(self, value: bool):
        pass
