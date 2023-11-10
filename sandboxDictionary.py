dict = {}

dict["hot"] = 100
dict["cold"] = 0
dict["med"] = 50
dict["apple"] = 75

for key, value in dict.items():
    if value > 0:
        print(f"{key}: {value}")

for index, element in enumerate(dict):
    print(f"{index} {element}")
