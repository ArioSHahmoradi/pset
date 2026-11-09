def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    precent = precent_to_float(input("What precentage would you like to tip? "))

    tip = dollars * precent

    print(f"Leave ${tip:.2f}")

def dollars_to_float(d:str):
    d = d.replace("$","")
    return float(d)

def precent_to_float(p:str):
    p = p.replace("%","")
    return float(p) / 100

main()