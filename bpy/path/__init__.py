# https://docs.blender.org/api/current/bpy.path.html
def abspath(path, *, start=None, library=None):
    pass

def basename(path) -> str:
    pass

def clean_name(name, *, replace='_') -> str:
    pass

def display_name(name, *, has_ext=True, title_case=True) -> str:
    pass

def display_name_to_filepath(name: str) -> str:
    pass

def display_name_from_filepath(name: str) -> str:
    pass

def ensure_ext(filepath: str, ext: str, *, case_sensitive=False) -> str:
    pass

def is_subdir(path, directory) -> bool:
    pass

def module_names(path, *, recursive=False) -> list[str]:
    pass

def native_pathsep(path: str) -> str:
    pass

def reduce_dirs(dirs) -> list[str]:
    pass

def relpath(path, *, start=None) -> str:
    pass

def resolve_ncase(path) -> str:
    pass