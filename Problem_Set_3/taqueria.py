def main():
    menu = {

        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00

    }

    total = 0.00
    while True:
        try:
            item = input("Item: ").lower().title() #capitalize first letter of each word, lower case the rest
            if item in menu: #check if item is in menu
                total += menu[item]
                print(f"${total:.2f}") #print the price of the item in menu dictionary with 2 decimal places
            else:
                continue #if item is not in menu, continue to next iteration
        except EOFError: #ctrl + z on windows, ctrl +d on unix to exit input
            break
                        
main()