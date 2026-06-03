from functools import wraps
from typing import Callable, Any
from time import perf_counter, sleep


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start: float = perf_counter()
        result: Any = func(*args, **kwargs)
        end: float = perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")

        return result

    return inner


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def inner(self, spell_name: str, power: int) -> Any:
            if power < min_power:
                return "Insufficient power for this spell"
            return func(self, spell_name, power)
        return inner

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args, **kwargs) -> str:
            attempt: int = 1
            while attempt <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying... "
                          f"({attempt}/{max_attempts})")
                    attempt += 1
            return f"Spell casting failed after {max_attempts} attempts"
        return inner

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        if not all(
            char.isalpha() or char.isspace()
            for char in name
        ):
            return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        if power < 0:
            raise ValueError("Invalid power")
        return f"Successfully cast {spell_name} with {power} power"


@retry_spell(3)
def fireball(power: int) -> str:
    if power < 0:
        raise ValueError("Invalid power")
    return f"Successfully cast Fireball with {power} power"


@spell_timer
def test_spell_timer() -> None:
    def count(n: int) -> int:
        if n > 0:
            sleep(1)
            print(n)
            return count(n - 1)
        print(0)
        return n

    count(10)


if __name__ == "__main__":
    print(f"=== Testing {test_spell_timer.__name__} ===")
    test_spell_timer()
    print()

    print(f"=== Testing {MageGuild.validate_mage_name.__name__} ===")
    print(f"{MageGuild.validate_mage_name('as')}")
    print()

    print("=== Testing Power Validator ===")
    strange = MageGuild()
    print(strange.cast_spell('Fireball', 20))
    print(strange.cast_spell('Waterball', 5))
    print()

    print("=== Testing Retry Validator")
    print(fireball(10))
    print(fireball(-10))
