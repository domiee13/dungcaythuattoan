#Problem
# Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges). For each successful withdrawal the bank charges 0.50 $US. Calculate Pooja's account balance after an attempted transaction.

# Input
# Positive integer 0 < X <= 2000 - the amount of cash which Pooja wishes to withdraw.

# Nonnegative number 0<= Y <= 2000 with two digits of precision - Pooja's initial account balance.

amount,balance = input().split()
amount = int(amount)
balance = float(balance)
if amount%5==0 and balance>=(amount+0.5):
    balance -= (amount+0.5)
print("{:.2f}".format(balance))