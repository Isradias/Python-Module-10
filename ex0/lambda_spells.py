def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda dict_: dict_['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return filter(lambda dict_: dict_['power'] >= min_power, mages)


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    total_power: int = sum(map(lambda dict_: dict_['power'], mages)) 
    avg_power: float = round((total_power / len(mages)), 2)
    return {
        'max_power': max(mages, key=lambda dict_: dict_['power']),
        'min_power': min(mages, key=lambda dict_: dict_['power']),
        'avg_power': avg_power
    }


if __name__ == "__main__":

    artifacts: list[dict] = [
        {'name': 'Lightning Rod', 'power': 70, 'type': 'relic'},
        {'name': 'Water Chalice', 'power': 65, 'type': 'armor'},
        {'name': 'Water Chalice', 'power': 86, 'type': 'relic'},
        {'name': 'Water Chalice', 'power': 102, 'type': 'armor'}]

    mages: list[dict] = [
        {'name': 'Nova', 'power': 71, 'element': 'lightning'},
        {'name': 'Casey', 'power': 62, 'element': 'earth'},
        {'name': 'Luna', 'power': 76, 'element': 'light'},
        {'name': 'Zara', 'power': 90, 'element': 'earth'},
        {'name': 'Rowan', 'power': 92, 'element': 'lightning'}]

    spells: list[str] = ['freeze', 'fireball', 'lightning', 'darkness']

    print("=== Ordered artifacts by power ===")
    for x in artifact_sorter(artifacts):
        print(x)
    print()

    print("=== Mages with power ge 75 ===")
    for x in power_filter(mages, 75):
        print(x)
    print()

    print("=== Transform spell names ===")
    print(spell_transformer(spells))
    print()

    print("===  Calculate statistics ===")
    stats: list[dict] = mage_stats(mages)
    for x in stats:
        print(f"{x}: {stats[x]}")
    print()
