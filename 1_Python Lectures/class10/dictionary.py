# json format
dict = {"name":"mas", "number":3}

# print(dict["number"])
# print(len(dict))
# print(dict.keys())
# dict.pop("name")
# dict.popitem()
# dict.clear()
# print(dict)

# for k in dict:
#     print(k)

# for v in dict.values():
#     print(v)

for k, v in dict.items():
    print(f'{k}: {v}')