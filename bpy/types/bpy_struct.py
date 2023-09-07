class bpy_struct():

    id_data: any
    
    def as_pointer(self):
        pass

    def driver_add(self, path: str, index=-1):
        pass

    def driver_remove(self, path: str, index=-1):
        pass

    def get(self, key: str, default=None):
        pass

    def id_properties_clear(self):
        pass

    def id_properties_ensure(self):
        pass

    def id_properties_ui(self, key):
        pass

    def is_property_hidden(self, property):
        pass

    def is_property_overridable_library(self, property):
        pass

    def is_property_readonly(self, property):
        pass

    def is_property_set(self, property, ghost=True):
        pass

    def items():
        pass

    def keyframe_delete(data_path, index=-1, frame=bpy.context.scene.frame_current, group=''):
        pass

    def keyframe_insert(data_path, index=-1, frame=bpy.context.scene.frame_current, group='', options=set()):
        pass

    def keys(self):
        pass

    def path_from_id(self, property=''):
        pass

    def path_resolve(self, path, coerce=True):
        pass

    def pop(self, key: str, default=None):
        pass

    def property_overridable_library_set(self, property, overridable):
        pass

    def property_unset(self, property):
        pass
    
    def type_recast(self):
        pass

    def values():
        pass