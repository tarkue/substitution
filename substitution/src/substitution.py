from typing import Dict, Tuple, Iterator, Union

from substitution.utils.lcm import lcm_multiple
from substitution.utils.find_cycles import find_all_cycles

from substitution.base import BaseSubstitution, BaseCycle


class Substitution(BaseSubstitution):
    def __init__(self, substition: Dict[int, int]) -> None:
        self.__substition = substition


    def __iter__(self) -> Iterator[int]:
        return iter(self.__substition)


    def __getitem__(self, key: int) -> int:
        return self.__substition[key]
    

    def __setitem__(self, key: int, value: int) -> None:
        self.__substition[key] = value


    def __mul__(self, other: 'Substitution') -> 'Substitution':
        new_substition = self.__class__({})

        for key in self:
            index = self[key]
            new_substition[key] = other[index]

        return new_substition
    

    def __pow__(self, c: int) -> 'Substitution':
        if c < 2:
            return self
        
        if c % 2 == 0:
            r = self ** (c // 2)
            return r * r
        
        return self * (self ** (c - 1))
    

    def __repr__(self) -> str:
        return repr(self.__substition)


    def __len__(self) -> int:
        return len(self.__substition)
    

    def __eq__(self, value: Union['Substitution', Dict[int, int]]) -> bool:
        if isinstance(value, Substitution):
            return self.__substition == value.__substition
        return self.__substition == value
    

    @property
    def cycles(self) -> Tuple[BaseCycle]:
        return find_all_cycles(self)


    @property
    def order(self) -> int:
        lengths = map(len, self.cycles)
        return lcm_multiple(lengths)
