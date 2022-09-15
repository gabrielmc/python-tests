from dataclasses import dataclass

@dataclass
class User:
	name: str
	age: int
	code: int

	# with used of dataclass is envelope the __init__ and __repr__.

	#new thunder
	def __post_init__(self):
		self.test = f'{self.name} {self.age} {self.code}'

	# def test(self):
	# return f'{self.name} {self.age}'


# without use of thunder
# gab = User('Gabriel Muniz', 67, 654289)
# print(gab.test())


# with use of thunder
gab = User('Gabriel Muniz', 67, 654289)
print(gab)
print(gab.test)
