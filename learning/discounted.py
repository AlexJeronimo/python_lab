phone1 = {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 1200, 'discount': 25}
phone2 = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 1000, 'discount': 10}

def discounted(price, discount, max_discount=20):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))

    if max_discount > 90:
        raise ValueError("Too big max discount!")
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)

