print("==============================================")
print("             DATA CONVERSION UTILITY")
print("==============================================")

product_name = input("Enter Product Name : ")
price = float(input("Enter Price       : "))
quantity = int(input("Enter Quantity    : "))

total_price = price * quantity

amount_str = str(total_price)

print("\n------------------------------------------------")
print("             TYPE CASTING SUMMARY")
print("------------------------------------------------")
print(f"{'Variable':<15}{'Value':<20}{'Python Type'}")
print("------------------------------------------------")
print(f"{'product_name':<15}{product_name:<20}{type(product_name)}")
print(f"{'price':<15}{price:<20}{type(price)}")
print(f"{'quantity':<15}{quantity:<20}{type(quantity)}")
print(f"{'total_price':<15}{total_price:<20}{type(total_price)}")
print(f"{'amount_str':<15}{amount_str:<20}{type(amount_str)}")
print("------------------------------------------------")

print("\n------------------------------------------------")
print("                  TAX INVOICE")
print("------------------------------------------------")
print(f"Product Name  : {product_name}")
print(f"Price per Unit: Rs. {price:.2f}")
print(f"Quantity      : {quantity}")
print("------------------------------------------------")
print(f"Invoice Total : Rs. {amount_str}")
print("==============================================")
