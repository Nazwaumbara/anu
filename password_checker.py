# --- Main ----------
def main():
    # Display welcome message
    welcomeMsg()

    while True:
        # Prompt user for a password
        passWord = input("\nPlease create a password:\n")

        # Call function for password validation
        if correctPW(passWord):
            break

    answer = input("\nDo you want to repeat the program? y for Yes n for No: ")

    if answer.lower() == "y":
        main()
    else:
        print("Thank you for using this program!")

# --- Functions ----------

# Welcome message
def welcomeMsg():
    print("\nThis program will prompt the user to enter a password with the following requirements:")
    print("\t- No less than 6 characters in length")
    print("\t- No spaces")
    print("\t- At least one numerical digit")
    print("\t- At least one alphabetical character")

# Validate password requirements
def correctPW(passWord):
    # Check for minimum character requirement
    if len(passWord) < 6:
        print("\nSorry! Your password is invalid.")
        print("It must be no less than 6 characters.")
        return False

    # Check for spaces
    if ' ' in passWord:
        print("\nSorry! Your password is invalid.")
        print("It must not contain spaces.")
        return False

    # Check for at least one numerical digit
    if not any(char.isdigit() for char in passWord):
        print("\nSorry! Your password is invalid.")
        print("It must contain at least one numerical digit.")
        return False

    # Check for at least one alphabetical character
    if not any(char.isalpha() for char in passWord):
        print("\nSorry! Your password is invalid.")
        print("It must contain at least one alphabetical character.")
        return False

    # If all checks pass
    print("\nCongratulations! Your password is valid!")
    return True

main()
