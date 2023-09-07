from bpy.types.bpy_struct import bpy_struct

# https://docs.blender.org/api/current/bpy.types.ID.html
class ID(bpy_struct):
    asset_data: any
    is_embedded_data: bool
    is_evaluated: bool
    is_library_indirect: bool
    is_missing: bool
    is_runtime_data: bool
    library: any
    library_weak_reference: any
    name: str
    name_full: str
    original: any
    override_library: any
    preview: any
    tag: bool
    use_extra_user: bool
    use_fake_user: bool
    users: int

    def evaluated_get(self, depsgraph: any):
        pass

    def copy(self) -> any:
        pass

    def asset_mark(self):
        pass

    def asset_clear(self):
        pass

    def asset_generate_preview(self):
        pass

    def override_create(self, remap_local_usages=False) -> any:
        pass

    def override_hierarchy_create(self, scene, view_layer, reference=None, do_fully_editable=False) -> any:
        pass

    def override_template_create(self):
        pass

    def user_clear(self):
        pass

    def user_remap(self, new_id: any):
        pass

    def make_local(self, clear_proxy=True) -> any:
        pass

    def user_of_id(self, id: any) -> int:
        pass

    def animation_data_create(self) -> any:
        pass

    def animation_data_clear(self):
        pass

    def update_tag(refresh: any={}):
        pass

    def preview_ensure() -> any:
        pass

    @classmethod
    def bl_rna_get_subclass(id: str, default=None):
        pass

    @classmethod
    def bl_rna_get_subclass_py(id: str, default=None):
        pass