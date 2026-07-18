from functools import reduce

sales = [
    {"month": "Jan", "profit": 45000},
    {"month": "Feb", "profit": 5000},
    {"month": "Mar", "profit": 7000},
    {"month": "April", "profit": 3000},
]



total = reduce(lambda sum, x:  sum + x["profit"], sales ,0)
print(f"Total sales = {total}")
