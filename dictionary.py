fruit_store = [
{
    "name":"Apples",
    "price": 4.59,
    "desc":"Fresh Apples Sourced Locally Organically"
},
{
    "name":"Pears",
    "price": 4.69,
    "desc":"Fresh Pears Sourced Locally Organically"
},
{
    "name":"Oranges",
    "price": 4.99,
    "desc":"Fresh Oranges Sourced Locally Organically"
},
{
    "name":"Watermelon",
    "price": 7.99,
    "desc":"Fresh Watermelon Sourced Locally Organically"
},
]
for index, item in enumerate(fruit_store):
    print(index, ":", item["name"], ",", item["price"], ",", item["desc"])

cart=[]
recipt=[]
def shoppin():
    shopping=input("Shopping?")
    while shopping=="yes":
        purchase = int(input("Chose a product in the fruit store by typing its index number"))
        print(fruit_store[purchase]["name"])
        cart.append(fruit_store[purchase]["name"])
        recipt.append(fruit_store[purchase]["price"])
        shopping=input("Still Shopping?")
    print(cart)
    print(recipt)
    total=sum(recipt)*1.04
    print(total)
    print("*Includes Tax")
    print("*Round to the Nearest Cent During Payment")
shoppin()