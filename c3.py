import random
import string

def generate_password(length):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    
    # Combine all characters
    all_characters = letters + digits + special_chars
    
    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    
    while True:
        try:
            # Prompt the user for the password length
            length = int(input("Enter the desired length of the password: "))
            
            # Validate the length
            if length <= 0:
                print("Length should be a positive integer.")
                continue

            # Generate and display the password
            password = generate_password(length)
            print(f"Generated password: {password}")
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
