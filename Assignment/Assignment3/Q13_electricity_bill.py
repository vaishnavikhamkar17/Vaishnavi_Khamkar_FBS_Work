## WAP ro input electricity unit charges and calculate total electricity bill according to the given condition: a. For dirst 50 units Rs.0.50/unit  b. for next 10 units Rs.0.75/unit c. for next 100 units Rs.1.20/unit d.for unit above 250 Rs.1.50/unit An additional  surcharge of 20% is added to the bill

units = int(input("Enter electricity units:"))

if(units <= 50):
    bill = units * 0.50
elif(units <= 150):
    bill = (50 * 0.50) + (units - 50) * 0.75
elif(units <= 250):
    bill = (50 * 0.50) + (100 * 0.75) + (units - 150) * 1.20
else:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + (units - 250) * 1.50

    surcharge = bill * 0.20
    total_bill = bill + surcharge

    print("Electricity bill= Rs.",total_bill)
