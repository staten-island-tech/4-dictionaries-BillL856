fruit_store = [
{
    "name": "Apples",
    "price": 3.99,
    "desc": "Crisp and Sweet Apples Perfect for Snacking or Baking"
},
{
    "name": "Pears",
    "price": 4.29,
    "desc": "Juicy and Smooth Pears with a Delicate Natural Sweetness"
},
{
    "name": "Oranges",
    "price": 4.79,
    "desc": "Bright and Tangy Oranges Packed with Fresh Citrus Flavor"
},
{
    "name": "Watermelon",
    "price": 6.99,
    "desc": "Sweet and Refreshing Watermelon Perfect for Hot Summer Days"
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
def shoppin():
    shopping=input("Shopping?")
    cost=0
    while shopping =="yes":
        purchase=int(input("Chose a product in the fruit store by typing its index number"))
        print(fruit_store[purchase-1]["name"])
        cart.append(fruit_store[purchase-1]["name"])
        cost+=fruit_store[purchase-1]["price"]
        shopping=input("Still Shopping?")
    print(cart)
    print(cost)
shoppin()

