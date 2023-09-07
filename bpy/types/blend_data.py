from bpy.types.bpy_struct import bpy_struct
from blend_data_curves import BlendDataCurves

# https://docs.blender.org/api/current/bpy.types.BlendData.html
class BlendData(bpy_struct):
    actions: any
    armatures: any
    brushes: any
    cache_files: any
    cameras: any
    collections: any
    curves: BlendDataCurves
    filepath: str
    fonts: any
    grease_pencils: any
    hair_curves: any
    images: any
    is_dirty: bool
    is_saved: bool
    lattices: any
    libraries: any
    lightprobes: any
    lights: any
    linestyles: any
    masks: any
    materials: any
    meshes: any
    metaballs: any
    movieclips: any
    node_groups: any
    objects: any
    paint_curves: any
    palettes: any
    particles: any
    scenes: any
    screens: any
    shape_keys: any
    sounds: any
    speakers: any
    texts: any
    textures: any
    use_autopack: bool
    version: any
    volumes: any
    window_managers: any
    workspaces: any
    worlds: any

    def batch_remove(ids):
        pass

    @classmethod
    def bl_rna_get_subclass(id: str, default=None):
        pass

    @classmethod
    def bl_rna_get_subclass_py(id: str, default=None):
        pass

    def orphans_purge(self) -> int:
        pass

    def temp_data(self, filepath=None) -> any:
        pass

    def user_map(self, subset, key_types, value_types) -> dict:
        pass



