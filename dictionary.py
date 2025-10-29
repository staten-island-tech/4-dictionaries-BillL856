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
{
    "name": "Strawberries",
    "price": 5.49,
    "desc": "Sweet and Juicy Strawberries Grown Without Pesticides"
},
{
    "name": "Avocado",
    "price": 2.25,
    "desc": "Creamy Hass Avocado Perfect for Toast or Salads"
},
{
    "name": "Blueberries",
    "price": 4.99,
    "desc": "Handpicked Blueberries Packed with Antioxidants"
},
{
    "name": "Mango",
    "price": 3.75,
    "desc": "Ripe Tropical Mangoes with a Sweet, Juicy Flavor"
},
{
    "name": "Pineapple",
    "price": 6.50,
    "desc": "Fresh Golden Pineapple, Perfect for Juices or Desserts"
},
{
    "name": "Cantaloupe",
    "price": 5.25,
    "desc": "Fragrant Cantaloupe Melon with a Soft, Sweet Texture"
}
]
for index, item in enumerate(fruit_store):
    print((index+1), ":", item["name"], ",", item["price"], ",", item["desc"])

cart=[]
recipt=[]
def shoppin():
    shopping=input("Shopping?")
    while shopping =="yes":
        purchase=int(input("Chose a product in the fruit store by typing its index number"))
        print(fruit_store[purchase-1]["name"])
        cart.append(fruit_store[purchase-1]["name"])
        recipt.append(fruit_store[purchase-1]["price"])
        shopping=input("Still Shopping?")
    print(cart)
    print(recipt)
    total=sum(recipt)*1.04
    print(total)
    print("*Includes Tax")
    print("*Round to the Nearest Cent During Payment")
shoppin()