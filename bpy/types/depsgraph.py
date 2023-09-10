from bpy.types.bpy_struct import bpy_struct
from typing import Literal
from view_layer import ViewLayer

# https://docs.blender.org/api/current/bpy.types.Depsgraph.html

class Depsgraph(bpy_struct):
    ids: any
    mode: Literal['VIEWPORT', 'RENDER']
    object_instances: any
    objects: any
    scene: any
    scene_eval: any
    updates: any
    view_layer: ViewLayer
    view_layer_eval: ViewLayer

    def debug_relations_graphviz(self, filename: str):
        pass

    # TODO not completed
