products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = int(input('請輸入商品價格'))
	products.append([name, price])

for product in products:
	print(product)