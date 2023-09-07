def blend_paths(absolute=False, packed=False, local=False) -> list[str]:
    pass

def escape_identifier(string: str) -> str:
    pass

def flip_name(name: str, strip_digits=False) -> str:
    pass

def unescape_identifier(string: str) -> str:
    pass

def register_class(cls):
    pass

def resource_path(type, major: int = 1, minor: str = '') -> str:
    pass

def unregister_class(cls):
    pass

def keyconfig_init():
    pass

def keyconfig_set(filepath, *, report=None):
    pass

def load_scripts(*, reload_scripts=False, refresh_scripts=False):
    pass

def modules_from_path(path: str, loaded_modules: set) -> list:
    pass

def preset_find(name, preset_path, *, display_name=False, ext='.py'):
    pass

def preset_paths(subdir: str) -> list:
    pass

def refresh_script_paths():
    pass

def app_template_paths(*, path: str = None):
    pass

def register_manual_map(manual_hook):
    pass

def unregister_manual_map(manual_hook):
    pass

def register_classes_factory(classes):
    pass

def register_submodule_factory(module_name: str, submodule_names: list[str]):
    pass

def register_tool(tool_cls, *, after=None, separator=False, group=False):
    pass

def make_rna_paths(struct_name: str, prop_name: str, enum_name: str):
    pass

def manual_map():
    pass

def manual_language_code(default='en'):
    pass

def script_path_user():
    pass

def script_paths(*, subdir: str=None, user_pref=True, check_all=False, use_user=True):
    pass

def smpte_from_frame(frame, *, fps=None, fps_base=None):
    pass

def smpte_from_seconds(time, *, fps=None, fps_base=None):
    pass

def user_resource(resource_type, *, path='', create=False):
    pass

def execfile(filepath: str, *, mod=None):
    pass