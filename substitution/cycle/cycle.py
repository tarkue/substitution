from typing import Iterable, Iterator

from substitution.base import BaseCycle


class Cycle(BaseCycle): 
    def __init__(self, cycle: Iterable[int]) -> None:
        self.__cycle = tuple(cycle)


    def __iter__(self) -> Iterator[int]:
        return iter(self.__cycle)
    

    def __getitem__(self, key: int) -> int:
        return self.__cycle[key]
    

    def __len__(self) -> int:
        return len(self.__cycle)
    

    def __eq__(self, value: object) -> bool:
        return self.__cycle == value


    def __repr__(self) -> str:
        elements = map(str, self.__cycle)
        return " → ".join(elements)
    