dict = {}

dict["hot"] = 100
dict["cold"] = 0
dict["med"] = 50
dict["apple"] = 75

for element in dict:
    if dict[element] > 0:
        print(element)

for index, element in enumerate(dict):
    print(str(index) + " " + element)