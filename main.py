import receipt_functions
import apiaccess
import sys

""
	

""
def main():
	running_nutrient_list = {"Vitamin D (D2 + D3)": 0.0, "Water": 0.0, "Energy": 0.0, "Protein": 0.0, "Fatty acids, total monounsaturated": 0.0, "Fatty acids, total polyunsaturated": 0.0, "Total lipid (fat)": 0.0, "Carbohydrate, by difference": 0.0, "Fiber, total dietary": 0.0, "Sugars, total": 0.0, "Calcium, Ca": 0.0, "Iron, Fe": 0.0, "Sodium, Na": 0.0, "Vitamin C": 0.0, "Vitamin C, total ascorbic acid": 0.0, "Vitamin A, IU": 0.0, "Fatty acids, total saturated": 0.0, "Fatty acids, total trans": 0.0, "Cholesterol": 0.0, "Magnesium, Mg": 0.0, "Phosphorus, P": 0.0, "Potassium, K": 0.0, "Zinc, Zn": 0.0, "Thiamin": 0.0, "Riboflavin": 0.0, "Niacin": 0.0, "Vitamin B-6": 0.0, "Folate, DFE": 0.0, "Vitamin B-12": 0.0, "Vitamin A, RAE": 0.0, "Vitamin E (alpha-tocopherol)": 0.0, "Vitamin D": 0.0, "Vitamin K (phylloquinone)": 0.0, "Caffeine": 0.0}
	if sys.argv[1] == 'add':
		file_name = sys.argv[2]
		r1 = receipt_functions.read_in_receipt(file_name)
		receipt_functions.print_receipt(r1)
	else:
		print('invalid argument(s).')
	item_list = receipt_functions.return_receipt(r1)
	print(item_list)
	for item_temp in item_list:	
		print ("Search database for "  + item_temp + "\n")
		helper = apiaccess.search_product(item_temp)
		obj = helper.json()
		try:
			list_obj = obj['list']
		except KeyError:
			print("no search results")
			continue
		items = list_obj['item']
		best_pick = items[0]
		print(best_pick['name'])
		check = input("Good choice? (y/n)")
		if (check == 'y'):
			best_pick_code = (best_pick['ndbno'])
			str_code = str (best_pick_code)
			new_helper = apiaccess.search_code(str_code)
			if new_helper.status_code != 200:
				print("couldnt find code")
				continue	
			obj1 = new_helper.json()
			report = obj1['report']
			food_data = report['food']
			nutrient_list = food_data['nutrients']
			for individual_nutrient in nutrient_list:
				temp_val = float(individual_nutrient['value']) 
				multiplier_new = item_list[item_temp]
				price = multiplier_new[0]
				mass = multiplier_new[1]
				multiplier = ((float(mass))/100.0)
				print("swag",multiplier)
				print(temp_val)
				temp_val *= multiplier
				running_nutrient_list[individual_nutrient['name']] = temp_val
		else:
			continue	
	for value in running_nutrient_list:
		print(value)
		print(running_nutrient_list[value])

main()