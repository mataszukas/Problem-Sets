def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    remove_dollar_symbol = d.removeprefix("$")
    return float(remove_dollar_symbol)

def percent_to_float(p):
    # TODO
    remove_percent = p.removesuffix("%")
    float_percent = float(remove_percent)
    tip_amount = float_percent/100
    return tip_amount


main()
