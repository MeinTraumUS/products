products = []
while True:
	name = input("Please type the name of products: ")
	if name == 'q' :
		break
	price = input("Please type the price of products: ")
	p = []
	p.append(name)  
	p.append(price)
	# p = [name, price]
	products.append(p)
	# 三行可改成一行 product.append([name, price])
print(products)

products[0][0]	# 列出清單中的第一個商品名稱