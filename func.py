def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Example:
original_price = 100
discount = 25

final_price = calculate_discount(original_price, discount)
print(f"The final price after discount is: {final_price:.2f}")

