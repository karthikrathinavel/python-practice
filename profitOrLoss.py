original_cost = float(input("Enter the original cost of the product:"))
sale_amount = float(input("Enter the sales amount:"))

if(original_cost > sale_amount):
    amount = original_cost - sale_amount
    print("Loss Amount = {0}".format(amount))
    percentage = (amount/original_cost)*100;
    print("Loss percentage:%.2f percent"%percentage)
elif(sale_amount > original_cost):
    amount = sale_amount - original_cost
    print("Profit = {0}".format(amount))
    percentage = (amount/original_cost)*100;
    print("Profit percentage:%.2f percent"%percentage)
else:
    print("No Profit and No Loss")
