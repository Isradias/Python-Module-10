from typing import Callable, Any
from functools import reduce, partial, lru_cache
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) == 0:
        return 0
    if operation not in ('add', 'multiply', 'max', 'min'):
        raise ValueError(f"Operation '{operation}' is unknown")
    if operation == "add":
        return reduce(add, spells)
    if operation == "multiply":
        return reduce(mul, spells)
    if operation == "max":
        return reduce(max, spells)
    if operation == "min":
        return reduce(min, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, element = "fire", power = 50),
        "water": partial(base_enchantment, element = "water", power = 50),
        "wind": partial(base_enchantment, element = "wind", power = 50)
    }


def memoized_fibonacci(n: int) -> int:



#def spell_dispatcher() -> Callable[[Any], str]:


def spell(target: str, element: str, power: int) -> str:
    return f"Attack {target} using {element} dealing {power} damage"


def test_spell_reducer():
    spell_powers: list[int] = [1, 2, 3, 4, 5]
    operations: list[str] = ['add', 'multiply', 'max', 'min', 'sqrt']
    print("=== Testing spell reducer ===")
    print(f"Spell powers: {spell_powers}")
    for operation in operations:
        try:
            print(f"{operation}: {spell_reducer(spell_powers, operation)}")
        except ValueError as e:
            print(e)
    print()

def test_partial_enchanter():
    print("=== Testing parcial enchanter ===")
    spells: dict[str, Callable] = partial_enchanter(spell)
    print(spells['fire']('Knight'))
    print(spells['water']('Wizard'))
    print(spells['wind']('Goblin'))
    print()

if __name__ == "__main__":
#fibonacci_tests = [14, 9, 16]
    #test_spell_reducer()
    test_partial_enchanter()