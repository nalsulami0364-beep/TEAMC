def convert_length(value,from_unit,to_unit):
    units = {"m": 1.0,"cm": 0.01,"mm": 0.001,"ft": 0.3048,"inch": 0.0254}
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit not in units or to_unit not in units:
        raise ValueError("Please use one of these units: m,cm,mm,ft,inch")
    value_in_m = value * units[from_unit]
    result = value_in_m / units[to_unit]
    return result


def convert_weight(value,from_unit,to_unit):
    units = {"kg": 1.0,"g": 0.001,"lb": 0.45359237,"oz": 0.0283495231}
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit not in units or to_unit not in units:
        raise ValueError("Please use one of these units: kg,g,lb,oz")
    value_in_kg = value * units[from_unit]
    result = value_in_kg / units[to_unit]
    return result


def convert_volume(value,from_unit,to_unit):
    units = {"l": 1.0,"ml": 0.001,"gal": 3.78541,"oz": 0.0295735}
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit not in units or to_unit not in units:
        raise ValueError("Please use one of these units: l,ml,gal,oz")
    value_in_l = value * units[from_unit]
    result = value_in_l / units[to_unit]
    return result


def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit == to_unit:
        return value

    if from_unit == "c":
        c = value
    elif from_unit == "f":
        c = (value - 32) * 5/9
    elif from_unit == "k":
        c = value - 273.15
    else:
        raise ValueError("Please use one of these units: C,F,K")

    if to_unit == "c":
        return c
    elif to_unit == "f":
        return c * 9/5 + 32
    elif to_unit == "k":
        return c + 273.15
    else:
        raise ValueError("Please use one of these units: C,F,K")


def converter_menu():
    print("Converter Mode")
    print("Category: length, weight, volume, temperature")
    category = input("Choose category: ").lower()
    from_unit = input("From unit: ")
    to_unit = input("To unit: ")
    value = float(input("Value: "))

    if value < 0 and category in ["length", "weight", "volume"]:
        print("The negative numbers is not allowed")

    try:
        if category == "length":
            result = convert_length(value,from_unit,to_unit)
        elif category == "weight":
            result = convert_weight(value,from_unit,to_unit)
        elif category == "volume":
            result = convert_volume(value,from_unit,to_unit)
        elif category == "temperature":
            result = convert_temperature(value,from_unit,to_unit)
        else:
            print("Choose one from the mentioned categories")
            return

        print(f"The result is: {result:.2f}")

    except ValueError as e:
        print("Error:", e)
if __name__ == "__main__":
    converter_menu()
