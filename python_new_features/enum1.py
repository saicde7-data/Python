from enum1 import Enum, auto

# Define an enumeration class
class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

# Accessing enumeration members
print(Color.RED)
print(Color.GREEN)
print(Color.BLUE)

# Iterating over enumeration members
for color in Color:
    print(color)

# Comparison and identity checks
print(Color.RED == Color.RED)  # True
print(Color.RED is Color.RED)  # True

# Enum members have both name and value attributes
print(Color.RED.name)   # 'RED'
print(Color.RED.value)  # 1 (auto-assigned by default)
