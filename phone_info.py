import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def get_phone_number_details():
    try:
        # Prompt the user to enter their phone number with country code
        phonenumber = input("Enter your mobile number along with the country code (e.g., +14155552671): ")
        contact_number = phonenumbers.parse(phonenumber)

        # Check if the number is valid
        if not phonenumbers.is_valid_number(contact_number):
            print("The phone number you entered is not valid.")
            return

        # Print the area description
        print(f"Area: {geocoder.description_for_number(contact_number, 'en')}")

        # Print the carrier name
        print(f"Carrier: {carrier.name_for_number(contact_number, 'en')}")

        # Print the timezone(s)
        print(f"Timezone: {', '.join(timezone.time_zones_for_number(contact_number))}")

    except phonenumbers.NumberParseException:
        print("The phone number you entered is not in a valid format. Please check and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to get phone number details
get_phone_number_details()
