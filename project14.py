#Currency Converter
def main():
    print("This program converts Us dollars to Naira")
    print()
    
    dollars = eval(input("Enter the amount in dollars: "))
    
    naira = convert_to_naira(dollars)
    
    print("That is", naira, "Naira.")

convert_to_naira = lambda dollars: dollars * 884.64
main()






























