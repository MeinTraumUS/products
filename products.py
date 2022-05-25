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

for p in products:
	print(p[0],'的價格是', p[1])

# "abc" +"123" = "abc123"
# "abc" * 3 = "abcabcabc"

with open('products.csv', "w", encoding="utf-8") as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + "," + p[1] + '\n')	