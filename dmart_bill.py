 
name=("Enter the name :")

lists= '''
Rice       Rs 10/kg
Sugar      Rs 8/kg
Oil        Rs 30/liter
Salt       Rs 25/kg
Paneer     Rs 40/kg
Maggie     Rs 12/pack
Boost      Rs 200/bottle
'''
price = 0
pricelist = []
totalprice = 0
Finalprice = 0
ilist = []
qlist = []
plist = []

items = {'rice': 10,
         'sugar': 8, 'oil': 30, 'salt': 25, 'paneer': 40, 'maggie': 12, 'boost': 200}
while True:
    option=input("select 1 for lists or 2 to exit :")
    if option=='2':
        print("Thank you for shopping" )
        break
    elif option=='1':
        print(lists)    
        while True:
            inp1=input("To buy press 1 or 2 to exit :")
            if inp1=='2':
                print("Thanks for shopping")
                break
            elif inp1=='1':
                item=input("choose your items to buy :").lower()
                while True:
                    quantity_input=input("Enter how many kilograms required :")
                    if quantity_input.isdigit():
                        quantity=int(quantity_input)
                        break
                    else:
                        print("Enter valid quantity")
                    
                if item in items:
                    price=quantity*items[item]
                    pricelist.append((item,quantity,items[item],price))
                    totalprice+=price
                    qlist.append(quantity)
                    plist.append(price)
                    ilist.append(item)
                else:
                    print("Item not found")

        
        if totalprice>0:
            tax=(totalprice*12)/100
            finalamount=tax+totalprice

            print(25 * "=", "Pythonlife Supermarket", 25 * "=")
            print(28 * " ", "Hyderabad")
            print("Name:", name, 30 * " ")
            print(75 * "-")
            print("sno", 10 * " ", 'items', 8 * " ", 'quantity', 8 * " ", 'price')

            
            for i in range(len(pricelist)):
                print(i, 13 * " ", ilist[i], 8 * " ", qlist[i], 8 * " ", plist[i])
                print(75 * "-")
                print("Tax amount", 50 * " ", 'Rs', tax)
                print(75 * "-") 
                print(50 * " ", 'Final amount:', 'Rs', finalamount)
                print(75 * "-")
                print(20 * " ", "Thank you & Visit again")
                print(75 * "-")



                
                    

                
                
                

            
            

