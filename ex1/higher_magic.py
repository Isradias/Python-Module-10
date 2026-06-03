from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: str) -> tuple[Callable, Callable]:
        return (spell1(target, power), spell2(target, power))

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def mega_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return mega_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: str) -> str:
        if condition(power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def spell_combo(target: str, power: str) -> list[str]:
        return [spell(target, power) for spell in spells]

    return spell_combo


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"{target} casts a Fireball, dealing {power} damage"


def teleport(target: str, power: int) -> str:
    return f"{target} teleports {power} km away"


def ispowerfull_spell(power) -> bool:
    if power >= 15:
        return True
    return False


if __name__ == "__main__":
    test_values = [5, 25, 15]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    combined: Callable = spell_combiner(heal, fireball)
    print("=== Combining two spells ===")
    print(f"{combined('Knight', 25)}\n")

    mega_fireball: Callable = power_amplifier(fireball, 3)
    print("=== Amplifying spell power ===")
    print("== Normal")
    print(f"{fireball('Dragon', 25)}\n")
    print("== Mega")
    print(f"{mega_fireball('Dragon', 25)}\n")

    condition_heal: Callable = conditional_caster(ispowerfull_spell, heal)
    print("=== Casting spell conditionally ===")
    print("== Valid contition")
    print(f"{condition_heal('Goblin', 20)}\n")
    print("== Invalid contition")
    print(f"{condition_heal('Goblin', 5)}\n")

    spell_combo: Callable = spell_sequence([teleport, fireball, heal])
    print("=== Using spell sequence ===")
    print(spell_combo('Wizard', 30))
