amazon_cart = [
    'notebooks',
    'sunglasses',
    'grapes',
    'toys'
]
# This updates the 0 index position hence replacing the variable notebooks with laptop
amazon_cart[0] = 'Laptops'
print(amazon_cart)

new_cart = amazon_cart[:]  # Copying the entire card
new_cart[0] = 'Gum'
print(new_cart)
print()

ultra_new = new_cart[:]
ultra_new[0] = 'French Fries'
ultra_new[1] = 'Poppies'
print(ultra_new)
