fruit_store = [
{
    "name":"Apples",
    "price": 4.59,
    "descriptiion":"Fresh Apples Sourced Locally Organically"
},
{
    "name":"Pears",
    "price": 4.59,
    "descriptiion":"Fresh Pears Sourced Locally Organically"
},
{
    "name":"Oranges",
    "price": 4.99,
    "descriptiion":"Fresh Oranges Sourced Locally Organically"
},
]
for index, item in enumerate(fruit_store):
    print(index, ":", item["name"])

shopping=input("Shopping? Yes or No")

cart=[]

while shopping=="Yes":
    purchase = int(input("Chose a product in the fruit store by typing an integer between 0 and 3"))
    print(fruit_store[purchase]["name"])
    cart.append(fruit_store[purchase]["name"])
    
    



