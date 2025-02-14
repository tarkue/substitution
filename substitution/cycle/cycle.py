from typing import List

from substitution.base import BaseCycle


class Cycle(BaseCycle): 
    def __init__(self, cycle: List[int]) -> None:
        self.__cycle = cycle

    def __iter__(self):
        return iter(self.__cycle)
    
    def __getitem__(self, key: int) -> int:
        return self.__cycle[key]
    
    def __len__(self):
        return len(self.__cycle)
    
    def __eq__(self, value):
        return self.__cycle.__eq__(value)

    def __repr__(self):
        elements = map(str, self.__cycle)
        return " → ".join(elements)
    