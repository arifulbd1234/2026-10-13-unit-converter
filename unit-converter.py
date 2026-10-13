"""
Day 7 - 2026-10-13
Tool: Unit Converter
What it does: Converts everyday units - temperature (Celsius/Fahrenheit),
length (metre, kilometre, foot, inch, mile) and weight (kilogram, gram,
pound) - from one unit to another.
Who it helps: Students, cooks following foreign recipes, travellers, and
anyone who sees a measurement in a unit they do not normally use.
"""


def celsius_to_fahrenheit(celsius):
    return round(celsius * 9 / 5 + 32, 2)


def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5 / 9, 2)


# Length factors are metres per unit; weight factors are kilograms per unit.
_LENGTH_IN_METRES = {
    "metre": 1.0,
    "kilometre": 1000.0,
    "centimetre": 0.01,
    "foot": 0.3048,
    "inch": 0.0254,
    "mile": 1609.344,
}

_WEIGHT_IN_KG = {
    "kilogram": 1.0,
    "gram": 0.001,
    "pound": 0.45359237,
    "ounce": 0.028349523125,
}


def _convert(value, from_unit, to_unit, table, kind):
    if from_unit not in table or to_unit not in table:
        raise ValueError(f"Unknown {kind} unit: {from_unit!r} or {to_unit!r}. "
                         f"Supported: {', '.join(sorted(table))}")
    return round(value * table[from_unit] / table[to_unit], 4)


def convert_length(value, from_unit, to_unit):
    """Convert a length, e.g. convert_length(5, 'foot', 'metre')."""
    return _convert(value, from_unit, to_unit, _LENGTH_IN_METRES, "length")


def convert_weight(value, from_unit, to_unit):
    """Convert a weight, e.g. convert_weight(10, 'kilogram', 'pound')."""
    return _convert(value, from_unit, to_unit, _WEIGHT_IN_KG, "weight")


if __name__ == "__main__":
    # Example 1: Dhaka summer temperature for a friend abroad
    print("38 C in Fahrenheit:", celsius_to_fahrenheit(38))

    # Example 2: a person's height, 5 foot 6 inches, in metres
    height_m = convert_length(5, "foot", "metre") + convert_length(6, "inch", "metre")
    print("5 ft 6 in in metres:", round(height_m, 2))

    # Example 3: body weight from a foreign scale, 154 pounds, in kilograms
    print("154 pounds in kilograms:", convert_weight(154, "pound", "kilogram"))
