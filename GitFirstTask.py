shopping_list={"bakery_store": ["bread","donut","bread_roll"],
               "grocery_store": ["carrot","celery","arugula"]
}
print("Shopping list") 

for store_name in shopping_list:
	shopping_list[store_name]=[product.upper() for product in shopping_list[store_name]]
	print("I'm going to",store_name.upper(),"i'm buying",shopping_list.get(store_name))
    