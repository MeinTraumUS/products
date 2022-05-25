import os #operating system


products = []
if os.path.isfile('products.csv'):  #相對路徑
	print("yeah! 找到檔案了!")
	# 讀取檔案
	with open('products.csv', 'r', encoding="utf-8") as f:  
	for line in f:
		if "商品,價格" in line:
			continue #繼續 跳到下一迴的意思
		name, price = line.strip().split(',') #先把換行符號去掉，再用逗點當切割的標準
		
		products.append([name, price])              #把切好的東西放到name,price裡 (切完是清單)
	print(products)
else:
	print("找不到檔案.......")


#讓使用者輸入
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


#印出所有購買紀錄
for p in products:
	print(p[0],'的價格是', p[1])

# "abc" +"123" = "abc123"
# "abc" * 3 = "abcabcabc"


#
with open('products.csv', "w", encoding="utf-8") as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + "," + p[1] + '\n')	