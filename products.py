import os #operation system 用這個作業系統來檢查檔案在不在

#讀取檔案
def read_file(filename):
	products=[]
	with open(filename, 'r', encoding='utf-8')as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip(). split(',')
			products.append([name, price])
	return products



#讓使用者輸入
def user_input(products):
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
	return products



#印出所有購買紀錄
#for loop 把清單中的東西一個個拿出來
def print_products(products):
	for p in products:
		print(p[0],'的價格是', p[1])




#寫入檔案
#逗點是分開用的
#\n是換行的意思
#csv 是存成excel模式
#with 是自動close
#encoding 是編碼的意思
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f. write('商品,價格\n')#header 欄位名稱
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')#f.write 才是真正寫入


#這邊才是開始執行程式
#寫一個main function把主要執行的程式裝起來
def main():
	filename = 'products.csv'
	if os.path.isfile(filename):#檢查檔案在不在 #path 是模組的意思 isfile是功能
		print('找到檔案了')
		products = read_file(filename)
	else:
		print('找不到檔案')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()
