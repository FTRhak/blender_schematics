from bm_vert import BMVert
from bm_face import BMFace

# https://docs.blender.org/api/current/bmesh.types.html#bmesh.types.BMFaceSeq

class BMFaceSeq():
    active: BMFace
    layers: any

    def ensure_lookup_table(self):
        pass

    def get(self, verts: BMVert, fallback=None) -> BMFace:
        pass

    def index_update(self):
        pass

    def new(self, verts: list[BMVert], example=None) -> BMFace:
        pass

    def remove(self, face):
        pass

    def sort(self, key=None, reverse=False):
        pass