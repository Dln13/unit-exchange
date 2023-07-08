unit_factors = {
        'm': 1.0,       # meter
        'km': 1000.0,   # kilometer
        'ft': 0.3048,   # foot
        'mi': 1609.34,  # mile
        'kg': 1.0,      # kilogram
        'lb': 0.453592  # pound
}

def convert_units(value, from_unit, to_unit):
    base_value = value * unit_factors[from_unit]
    target_value = base_value / unit_factors[to_unit]    
    return target_value

value = float(input("Enter the value to convert: "))
from_unit = input(f"Enter the unit to convert from ({' '.join([item for item in unit_factors.keys()])}):")
to_unit = input(f"Enter the unit to convert to ({' '.join([item for item in unit_factors.keys()])}):")

converted_value = convert_units(value, from_unit, to_unit)
print(f"{value} {from_unit} is equal to {converted_value} {to_unit}")
