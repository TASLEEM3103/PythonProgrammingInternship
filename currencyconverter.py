# Import necessary libraries
import requests
import json

# Define a function to fetch exchange rates from an API
def get_exchange_rate(api_key, base_currency, target_currency):
    # Build the API URL using provided parameters
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # Check if the response status code is 200
    if response.status_code == 200:
        # Parse the response data as JSON
        data = response.json()
        # Return the conversion rate from the JSON data
        return data["conversion_rate"]
    else:
        # Raise an exception if the API request was unsuccessful
        raise Exception(f"Failed to fetch exchange rate. Error code {response.status_code}")

# Define the main function
def main():
    # Set your API key
    api_key = "7d3aac3a7f780bbd2998ee26"
    
    # Get user input for the base and target currencies
    base_currency = input("Enter the base currency (e.g, INR, USD, EUR, GBP):").upper()
    target_currency = input("Enter the target currency (e.g, INR, USD, EUR, GBP):").upper()

    try:
        # Call the get_exchange_rate function to get the exchange rate
        exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)
        print(f"Exchange Rate: {exchange_rate}")

        # Get user input for the amount to convert
        amount = float(input("Enter the amount to convert: "))
        
        # Calculate the converted amount
        converted_amount = amount * exchange_rate
        
        # Display the result with two decimal places
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")

    except Exception as e:
        # Handle any exceptions and display an error message
        print(f"An error occurred: {e}")

# Check if the script is being run as the main program
if __name__ == "__main__":
    main()