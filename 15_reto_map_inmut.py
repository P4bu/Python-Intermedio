items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pantalon',
        'price': 300
    },
        {
        'product': 'cinturon',
        'price': 50
    }
]

prices = list(map(lambda item: item['price'], items))
print(prices)

def add_taxes(item):
    new_item = item.copy() # con esto copio el dict y no nodificara el original 
    new_item['taxes'] = new_item['price'] * .19
    return new_item

new_items = list(map(add_taxes, items))
print('new_list')
print(new_items)
print('old_list')
print(items)

