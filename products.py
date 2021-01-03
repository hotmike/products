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

####################寫入檔案###################
#逗點是分開用的
#\n是換行的意思
#csv 是存成excel模式
#with 是自動close
#encoding 是編碼的意思
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f. write('product,price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')#f.write 才是真正寫入
