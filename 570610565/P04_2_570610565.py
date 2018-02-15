#เปรียบเทียบสินค้ำ LAB04 570610565

price_A = int(input("Enter A's price : "))
quality_A = int(input("Enter A's quality (0 - 4) : "))

price_B = int(input("Enter B's price : "))
quality_B = int(input("Enter B's quality (0 - 4) : "))

output_String = "Not sure..."

if price_A == price_B and quality_A == quality_B :
    output_String = "Both are equally good"
else:
    if price_A <= price_B and quality_A >= quality_B :
        output_String = "Pick A"
    elif price_B <= price_A and quality_B >= quality_A:
        output_String = "Pick B"

print(output_String)            