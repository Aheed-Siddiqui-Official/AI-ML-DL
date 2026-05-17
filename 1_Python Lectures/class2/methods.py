name = "Muhammad Aheed Siddiqui"
name2 = "Atiq Ahmed Siddiqui"

print(name[12])
print(name[-13])

upperName = name.upper()
lowerName = name.lower()
capsName = name.capitalize()

print(upperName)
print(lowerName)
print(capsName)

# Slicing
print(name[0:12])

# Stride
print(name[0:12:4])

# Length of String
length = len(name)
print(length)

# Reversing String
reverse = name[23::-1]
print(reverse)

# Escape Sequences
print(f"My name is \n {name}")
print(f"My name is \t {name}")
print(f"My name is \b {name}")
print(f"My name is \\ {name}")

# Comparison & Membership
print(name == name2)
print("Siddiqui" in name)
print("Siddiqui" not in name)

# Only finds the first occurence
print(name.find("Aheed"))
print(name.find("a"))

# Replace
print(name.replace(name, "MAS"))
print(name)

# Split
split = name.split('1')
print(split)

# Formatting except f
print("Big Data %s - Python %d" % ('Analytics', 3))







