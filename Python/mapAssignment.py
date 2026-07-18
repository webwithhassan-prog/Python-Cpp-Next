employees = [
    {"name": "Hassan", "role": "HR"},
    {"name": "Afzal", "role": "Staff"},
    {"name": "Ali", "role": "Manager"},
    {"name": "Asad", "role": "Staff"},
]


# Map --------
print("All Users Data")
allData = list(map(lambda x: x, employees))
print(allData)
print("\n")




# Filter -------
print("Filtered Staff Data")
filteredData = list(filter(lambda x: x["role"] == "Staff", employees))
print(filteredData)
