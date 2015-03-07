width=input("please input width:")

price_width=10
item_width=int(width) -  price_width

header = '%-*s%-*s'
item = '%-*s%*.2f'

print ('='*width)
print (header % (item_width, 'Item', price_width, 'Price'))
print ('-'*width)
print (item % (item_width,"Apple", price_width, 12.45))
print (item % (item_width, "tomato", price_width, 2342.123))
print ('='*width)
