##A man goes for shopping. he buy 5 products .Accept the price of all products and display the total bill after adding 18% GST.
p1 = int(input("Enter price of product 1:"))
p2 = int(input("Enter price of product 2:"))
p3 = int(input("Enter price of product 3:"))
p4 = int(input("Enter price of product 4:"))
p5 = int(input("Enter price of product 5:"))

total = p1 + p2 + p3 + p4 + p5

if (total > 0):
    gst = total * 0.18   #18% GST
    final_bill = total + gst
    print("Total bill before GST:",total)
    print("GST (18%) = Rs.",gst)
    print("Final bill after gst:",final_bill)
else:
    print("Invalid input")
