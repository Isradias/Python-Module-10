from typing import Any
from collections.abc import Callable


def mage_counter() -> Callable:
    nb_calls: int = 0

    def counter() -> int:
        nonlocal nb_calls
        nb_calls += 1
        return nb_calls

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    current_power: int = initial_power

    def increase(to_add: int) -> int:
        nonlocal current_power
        current_power += to_add
        return current_power

    return increase


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant_weapon(weapon: str) -> str:
        return " ".join((enchantment_type, weapon))

    return enchant_weapon


def memory_vault() -> dict[str, Callable]:
    memory: list[dict] = []

    def store(key_: Any, value_: Any) -> str:
        nonlocal memory
        if any(key_ in dict_ for dict_ in memory):
            raise ValueError("Key already exists")
        memory += [{key_: value_}]
        return f"Storing -> {key_}: {value_}"

    def recall(key_: Any) -> Any:
        for dict_ in memory:
            if key_ in dict_:
                return f"Recall -> {key_}: {dict_[key_]}"
        return f"Recall -> {key_}: Memory not found"

    return {
        'store': store,
        'recall': recall
    }


def test_counter() -> None:
    counter_a: Callable = mage_counter()
    counter_b: Callable = mage_counter()
    print("=== Testing Mage Counter ===")
    print(f"Counter_a: {counter_a()}")
    print(f"Counter_a: {counter_a()}\n")

    print(f"Counter_b: {counter_b()}")
    print(f"Counter_b: {counter_b()}")
    print(f"Counter_b: {counter_b()}\n")

    print(f"Counter_a: {counter_a()}")
    print(f"Counter_a: {counter_a()}")
    print(f"Counter_a: {counter_a()}\n")

    print(f"Counter_b: {counter_b()}")
    print(f"Counter_b: {counter_b()}")
    print()


def test_accumulator(base: int, addition) -> None:
    print("=== Testing Spell Accumulator ===")
    accumulator: Callable = spell_accumulator(base)
    print(f"Base: {base}, accumulated: {accumulator(addition)}")
    print(f"Base: {base}, accumulated: {accumulator(addition)}")
    print(f"Base: {base}, accumulated: {accumulator(addition)}")
    print()


def test_factory():
    print("=== Testing Enchantment Factory ===")
    enchant_shocking = enchantment_factory("Shocking")
    enchant_windy = enchantment_factory("Windy")
    enchant_flowing = enchantment_factory("Flowing")

    print(enchant_shocking("Sword"))
    print(enchant_shocking("Cloack"))
    print(enchant_windy("Shield"))
    print(enchant_flowing("Ring"))
    print()


def test_memory():
    print("=== Testing Memory Vault ===")
    memory = memory_vault()
    print(memory['store']("A", "Pass"))
    print(memory['store']("B", "Pass2"))
    print()
    print(memory['recall']("A"))
    print(memory['recall']("B"))
    print(memory['recall']("C"))


if __name__ == "__main__":
    test_counter()
    test_accumulator(100, 10)
    test_factory()
    test_memory()
