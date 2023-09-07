from typing import TypeVar, Generic, List, Optional

# https://docs.blender.org/api/current/bpy.types.bpy_prop_collection.html

ListItem = TypeVar('ListItem')

class bpy_prop_collection(Generic[ListItem]):

    def find(self, key: str) -> int:
        pass

    def foreach_get(self, attr, seq):
        pass

    def foreach_set(self, attr, seq):
        pass

    def get(self, key: str, default=None) -> ListItem:
        pass

    def items(self) -> list[ListItem]:
        pass

    def keys(self) -> list[str]:
        pass

    def values(self) -> list:
        pass