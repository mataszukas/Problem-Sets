def main():

    amount_due = 50
    calculation(amount_due)

def calculation(amount_due):

    print("Amount Due:", amount_due)

    while amount_due > 0:
        coin = int(input("Insert Coin: "))
        if coin in [5, 10, 25]:
            amount_due -= coin
        if amount_due <= 0:
            print ("Change Owed:", amount_due*(-1))
            break
        else:
            print("Amount Due:", amount_due)

main()
 