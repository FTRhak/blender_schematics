from typing import Literal
from bpy.types.bpy_struct import bpy_struct
from curve import Curve

class BlendDataCurves(bpy_struct):
    def new(self, name: str, type: Literal['Curve', 'Surface', 'Text']) -> Curve:
        """
        :param str name
        :param sre type - enum: Curve | Surface | Text
        """
        pass