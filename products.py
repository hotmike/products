products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	#p=[]    #小清單
	#p = [name, price]
	#p.append(name)
	#p.append(price)
	#products.append(p) #小清單放在大清單裡面
	products.append([name, price]) #最簡潔寫法
print(products)


#for loop 把清單中的東西一個個拿出來
for p in products:
	print(p[0],'的價格是', p[1])