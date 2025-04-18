# Taking user input
price = float(input("Input price: "))
discount_input= input("Input percentage discount: ").strip()

# Checking for null input
if discount_input == "":
    print(f"No discount applied: {price}")
    
else:
    # typecasting the discount_input to float discount_percent
    discount_percent = float(discount_input)
    # creating function and returning the final price
    def calculate_discount(price, discount_percent):
        return price * (100-discount_percent)/100
    
    if discount_percent >= 20:
        print(f"The discount is {price * discount_percent/100} \n final price is: {calculate_discount(price, discount_percent)}")
    
    
        
    else:
        print(f"Discount applies from 20% !!! | No Discount Applied \n{price}")