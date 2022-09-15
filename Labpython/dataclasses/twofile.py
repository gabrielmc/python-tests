from dataclasses import dataclass

@dataclass
class PageDimensions:
    width: int
    height: int


# --------------------------------------------------------------------------------------
from typing import NamedTuple

# define os atributos da classe com a tipagem de cada um.
PageDimensions = NamedTuple('PageDimensions', [('width', int), ('height', int)])


# --------------------------------------------------------------------------------------
from collections import namedtuple

# define os atributos da classe sem tipagem e separados por espaçamento.
PageDimensions = namedtuple('PageDimensions', 'width height')
