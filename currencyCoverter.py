from forex_python.converter import CurrencyRates


def convert_currency(from_currency, to_currency, amount):
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    return converted_amount

if __name__ == "__main__":
    from_currency = input("Enter the currency code you want to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency code you want to convert to (e.g., EUR): ").upper()
    amount = float(input("Enter the amount you want to convert: "))

    converted_amount = convert_currency(from_currency, to_currency, amount)
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    
