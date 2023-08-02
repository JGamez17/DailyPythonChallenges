bill = 47.28  # Assign "bill" variable with bill amount
tip = bill * 0.15  # Multiply by stated tip rate
print(tip)
total = bill + int(tip)  # Sum the "total" of the "bill" and "tip"
share = total/2  # Divide "total" by number of friends dining
print("Each person needs to pay: " + str(share))
