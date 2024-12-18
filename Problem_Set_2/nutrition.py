def main():

    user_input = input("Item: ").lower().strip()
    calories(user_input)

def calories(item):

    poster = {

        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "Honeydew Melon": 50,
        "Kiwifruit (2 medium)": 90,
        "Lemon (1 medium)": 15,
        "Lime": 20,
        "Pear": 100,
        "Nectarine (1 medium)": 60,
        "Orange (1 medium)": 80,
        "Sweet Cherries 21 Cherries; 1 cup": 100

    }

    for fruit in poster:
        if item in fruit.lower():
            print(poster[fruit], end="")
        else:
            None

main()
