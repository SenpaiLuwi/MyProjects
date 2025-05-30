import random
import re


def generate_otp():
    return str(random.randint(100000, 999999))


def is_valid_otp(otp):
    pattern = re.compile(r'^\d{6}$')
    return bool(pattern.match(otp))


def main():
    while True:
        user_input = input("Type 'Next' for a new OTP (or 'Exit' to quit): ")
        if user_input.lower() == "exit":
            break
        elif user_input.lower() == "next":
            otp = generate_otp()
            print("Generated OTP:", otp)
            while True:
                user_input = input("Enter OTP: ")
                if is_valid_otp(user_input):
                    if user_input == otp:
                        print("OTP Verified!")
                        break
                    else:
                        print("Incorrect OTP. Try again.")
                else:
                    print("Invalid OTP format. OTP should be a 6-digit number.")
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
