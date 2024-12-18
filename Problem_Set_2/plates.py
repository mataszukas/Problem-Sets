def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    is_numeric = []
    if 2 <= len(s) <= 6 and s.isalnum():
        if s.isalpha():
            return True
        elif s[-1].isnumeric() and s[:2].isalpha():
            for index, c in enumerate(s):
                if c.isnumeric():
                    is_numeric.append(index)
            if s[is_numeric[0]] == "0":
                return False
            for j in range(len(is_numeric)-1):
                if is_numeric[j+1]-is_numeric[j] != 1:
                    return False
            return True
        else:
            return False
    else:
        return False

main()
