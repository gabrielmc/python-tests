# normal class

class User:
    def __ini__(self, name: str, age: int, code: int):
        self.name = name
        self.age = age
        self.code = code

    def __repr__(self):
        return f'User (name={self.name}, age={self.age}, code={self.code})'


# intancia
#gabriel = User('Gabriel', 27, 12345)
#print(gabriel.name)

# ---------------------------------------------------------------------------
# class with dataclass

from dataclasses import dataclass

@dataclass
class UserDt:
    name: str
    age: int
    code: int


# intancia
gab = UserDt('Gabriel Muniz', 67, 654289)
print(gab)
