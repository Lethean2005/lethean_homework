# EX10.Show product name that has maximum price
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
def sum(products):
    name= ""
    max =0
    for i in range(len(products)):
        if products[i]["price"]>max:
           max=products[i]["price"]
           name=products[i]["name"]
    return name

products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
print(sum(products))
