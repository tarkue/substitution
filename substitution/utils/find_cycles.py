from typing import Tuple

from substitution.base import BaseSubstitution
from substitution.cycle import Cycle


def find_cycle_by_key(
    substition: BaseSubstitution, 
    key: int
) -> Cycle:
    """
    Find a cycle by key in a substitution.
    """
    cycle = [key]

    last_item = None
    while last_item != key:
        val = substition[key] if last_item is None else substition[last_item]
        cycle.append(val)
        last_item = val
        
    return Cycle(cycle)


def find_all_cycles(
    substitution: BaseSubstitution
)-> Tuple[Cycle]:
    """
    Find all cycles in a substitution.
    """
    visited = set()
    cycles = []

    for key in substitution:
        if key in visited:
            continue

        cycle = find_cycle_by_key(substitution, key)
        setted_cycle = set(cycle)

        if setted_cycle & visited:
            continue

        if len(setted_cycle) > 0:
            visited |= setted_cycle
            cycles.append(cycle)

    return tuple(cycles)
