from typing import Type

# https://docs.blender.org/api/current/mathutils.html#mathutils.Vector
class Vector():
    """
    vec = mathutils.Vector((0.0, 0.0, 1.0))

    # unit length vector
    vec_a = vec.normalized()
    """
    @classmethod
    def Fill(size: int, fill=0.0):
        """Create a vector of length size with all values set to fill.

        Args:
            size (int): The length of the vector to be created.
            fill (float, optional): The value used to fill the vector. Defaults to 0.0.
        """
        pass

    @classmethod
    def Linspace(start: int, stop: int, size: int):
        """Create a vector of the specified size which is filled with linearly spaced values between start and stop values.

        Args:
            start (int): The start of the range used to fill the vector.
            stop (int): The end of the range used to fill the vector.
            size (int): The size of the vector to be created.
        """
        pass

    @classmethod
    def Range(start: int, stop: int, step: int=1):
        pass

    @classmethod
    def Repeat(vector: tuple, size: int):
        pass

    def angle(self, other, fallback:any=None) -> float:
        pass

    def angle_signed(self, other, fallback: any) -> float:
        pass

    def copy(self) -> Type['Vector']:
        pass

    def cross(self, other: Type['Vector']) -> Type['Vector']:
        pass

    def dot(self, other: Type['Vector']) -> Type['Vector']:
        pass

    def freeze(self) -> any:
        pass

    def lerp(other: Type['Vector'], factor: float) -> Type['Vector']:
        pass

#TODO not completed

