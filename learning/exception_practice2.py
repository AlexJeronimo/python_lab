def discounted(price, discount, max_discount=20, name=""):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
    except (ValueError, TypeError) as e:
        return(f"Error: Invalid argument type - {e}")

    if max_discount > 99:
        raise ValueError("Too big max discount!")
    if discount >= max_discount or "iphone" in name.lower() or not name:
        return price
    else:
        return price - (price * discount / 100)


#print(discounted('hundred', 89.3, 12.3, "Xperia"))