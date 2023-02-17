import requests

what = input('What would you like to convert? (Enter exchange code eg.: USD): ').upper()
to_what = input('To what would you like to exchange?: ').upper()
amount = float(input('How much?: '))
response = requests.get(f'https://v6.exchangerate-api.com/v6/8fae216879bf6a34001dba55/pair/{what}/{to_what}/{amount}')

if response.status_code == 200:
    data = response.json()
else:
    print('Could not connect to the page.')
    exit()
    
print(f"Conversion rate is: {data['conversion_rate']}")
print(f"By converting {amount} {what} into {to_what} you get {data['conversion_result']}.")