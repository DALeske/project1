#The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+         The Coffee Shop       +")
print("+              Welcome          +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees:")
print(" > Espresso      $2.50")
print(" > Americano     $3.00")
print(" > Latte         $2.50")
print(" > Cappuccino    $3.00")
print(" > Macchiato     $2.50")
print(" > Mocha         $3.50")
print(" > Flat White    $2.50")
print("----------------------------")

price = 0
coffee = input("What type of coffee would you like?").title()
if coffee=="Espresso":
   price = price + 2.50
elif coffee=="Americano":
   price = price + 3
elif coffee=="Latte":
   price = price + 2.50
elif coffee=="Cappuccino":
   price = price + 3
elif coffee=="Macchiato":
   price = price + 2.50
elif coffee=="Mocha":
   price = price + 3.50
elif coffee=="Flat White":
   price = price + 2.50
print("----------------------------")
print("           SIZES")
print("----------------------------")
print ("Medium")
print("Large        add $1.00")
print("Extra Large  add $1.50")
print("----------------------------")
price2 = 0
cup = input("What size of coffee would you like?").title()
if cup=="Medium":
   price2 = price2 + 0
elif cup=="Large":
   price2 = price2 + 1.00
elif cup=="Extra Large":
   price2 = price2 + 1.50
print("----------------------------")
print("Here     no extra")
print("Go       add $1.00")
print("----------------------------")
price3 = 0
eat_loc = input("For here or to go?").title()
if eat_loc == "Here":
   price3 = price3 + 0 
elif eat_loc == "Go":
   price3 = price3 + 1

total_price = price+price2+price3

print("----------------------------")
#print(price)
#print(price2)
#print(price3)
print("Total Cost: $" + str(total_price))