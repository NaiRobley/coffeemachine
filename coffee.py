"""Make Coffee"""
# My cup of coffee
def coffee(milk=False, hot_water=False):
	print("Took a cup")
	print("Poured coffee")
	print("Added sugar")
	if milk is True and hot_water is True:
		print("Poured in milk")
		print("Poured in hot water")
		print("Stirr")
		print("Your coffee is ready")
		print("")
		new_coffee = "A tasty cup of coffee with milk and hot water"
		return new_coffee

	elif milk is True:
		print("Poured in milk")
		print("Stirr")
		print("Your coffee is ready")
		print("")
		new_coffee = "A tasty cup of coffee with milk"
		return new_coffee
	elif hot_water is True:
		print("Poured in hot water")
		print("Stirr")
		print("Your coffee is ready")
		print("")
		new_coffee = "A tasty cup of coffee with hot water"
		return new_coffee

def serve(person_name, milk=False, hot_water=False):
	person_coffee = coffee(milk, hot_water)
	result = "{0} for {1}".format(person_coffee, person_name)
	print(result)
	print("")
	return result

serve("Madge", milk=True)
serve("Robley", hot_water=True)