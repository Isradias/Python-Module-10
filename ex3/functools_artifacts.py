from typing import Any
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from collections.abc import Callable


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
    return -1


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, element="fire", power=50),
        "water": partial(base_enchantment, element="water", power=50),
        "wind": partial(base_enchantment, element="wind", power=50)
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be positive")

    if n < 2:
        return n

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatcher(value: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register
    def damage_spell(value: int) -> str:
        return f"Damage spell deals {value} damage"

    @dispatcher.register
    def enchantment_spell(value: str) -> str:
        return f"Enchantment cast: {value}"

    @dispatcher.register
    def multicast_spell(value: list) -> str:
        return f"Multi-cast spell with {len(value)} effects"

    return dispatcher


def spell(target: str, element: str, power: int) -> str:
    return f"Attack {target} using {element} dealing {power} damage"


def test_spell_reducer() -> None:
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


def test_partial_enchanter() -> None:
    print("=== Testing parcial enchanter ===")
    spells: dict[str, Callable] = partial_enchanter(spell)
    print(spells['fire']('Knight'))
    print(spells['water']('Wizard'))
    print(spells['wind']('Goblin'))
    print()


def test_memoized_fibonacci() -> None:
    print("=== Testing memoized fibonacci ===")
    print(f"n = 0: {memoized_fibonacci(0)}")
    print(f"n = 1: {memoized_fibonacci(1)}")
    print(f"n = 10: {memoized_fibonacci(10)}")
    print(f"n = 15: {memoized_fibonacci(15)}")
    print(memoized_fibonacci.cache_info())
    memoized_fibonacci.cache_clear()
    print()


def test_spell_dispatcher() -> None:
    magic = spell_dispatcher()

    print("=== Testing spell dispatcher ===")
    print(magic(10))
    print(magic("Shield"))
    print(magic(["Fire", "Ice"]))
    print(magic(magic))
    print()


if __name__ == "__main__":
    test_spell_reducer()
    test_partial_enchanter()
    test_memoized_fibonacci()
    test_spell_dispatcher()
