import sys as sys

product_dict = {"whey_protein" : 8.99,
				"protein_bar" :1.50,
                "workout_leggings" : 42.00,
                "mp_t_shirt" : 15.00,
                "multivitamin_tablets" : 7.99,
                "cycling_shorts" : 19.99,
                "shaker" : 5.00,
                "pre_workout" : 39.99,
                "sugar_free_syrup" : 6.49, 
                "sugar_free_syrup" : 6.49,
                "protein_spread" : 6.99,
                }
product_list = list(product_dict)
cart = {}
cart_total = 0
err = 0

TGREEN =  '\033[32m'
TRED =  '\033[91m'
TBLACK = "\033[30m"


while True:
	print(TBLACK+'\n**************************\n')
	print('Product List : \n')
	serial_no = 1
	for key in product_dict:
		print(str(serial_no) + ". "+ key +" : " +str(product_dict.get(key)))
		serial_no +=1
	print('\n**************************\n')
	print("F : Checkout")
	print("C : Cancel\n")
	print(TRED+ "Basket : ", end="")
	if(len(cart)>0):
		for value in cart:
			print("("+str(cart.get(value)) +") "+ value, end=", ")
	else:
		print(" No items added")
	print()
	print("Cart total : GBP " + str(round(cart_total,2))+'\n')
	if(err==1):
		print("That was an invalid input")
		err = 0
	item_chosen = input(TGREEN+"Choose an item from the list above: \n"+TBLACK)
	try:
		item_chosen = item_chosen.strip()
		if(item_chosen == "f" or item_chosen == "F"):
			break
		if(item_chosen == "c" or item_chosen == "C"):
			sys.exit()
		product_name = product_list[int(item_chosen)-1]
		if product_name in cart.keys():
			cart[product_name] += 1
		else:
			cart[product_name] = 1
		cart_total += product_dict.get(product_list[int(item_chosen)-1])
	except SystemExit:
		sys.exit()
	except:
		print(TBLACK+"**********  Invalid Input **********")
		err = 1
		continue
	print(TBLACK+"Item chosen : "+ product_list[int(item_chosen)-1])


if cart_total >0 :
	cart_final = cart_total - (15/100)*cart_total
	print('\n**********************************************************************\n')
	print("Final Basket : ", end="")
	for value in cart:
		print("("+str(cart.get(value)) +") "+ value, end=", ")
	print()
	print("Discount applied : "+TRED+"15%"+TBLACK)
	print("Please pay "+TRED+"GBP "+ str(round(cart_final,2))+TBLACK+" to the cashier. Thanks for shopping")
	print('\n**********************************************************************\n')
else:
	print('\n**********************************************************************')
	print(TRED+"\n No Items Selected. Please run the order forum again\n"+TBLACK)
	print('**********************************************************************\n')







