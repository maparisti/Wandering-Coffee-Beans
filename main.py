import random

from coffee import coffees
from messages import messages_per_coffee

ORDER_ARCHIVE = "orders.txt"

def welcome_message():
    """Ask for the user's name and return a personalized greeting."""
    username = input("""Welcome to Wandering Coffee Beans
What is your name? """).strip()

    # Keep asking until the user enters a valid name.
    while username == "":
        username = input("Please enter your name: ").strip()

    return "Hello " + username


def show_menu():
    """Print the coffee menu using the information stored in coffee.py."""
    number = 1
    print("\n☕ Wandering Coffee Beans Menu\n")

    # Loop through each coffee and print its details.
    for coffee_name, info in coffees.items():
        print(f"{number}: {coffee_name}")
        number += 1

        for key, value in info.items():
            print(f"{key}: {value}")

        print()


def create_coffee_options():
    """Create a flexible dictionary for user input validation.

    Example:
    'latte' -> 'Latte'
    'cold brew' -> 'Cold Brew'
    """
    coffee_options = {}

    for coffee_name in coffees:
        coffee_options[coffee_name.lower()] = coffee_name

    return coffee_options


def choose_coffee():
    """Ask the user to choose a coffee and print a random message for it."""
    coffee_options = create_coffee_options()
    show_menu()

    selected_coffee = ""

    # Keep asking until the user types a coffee that exists in the menu.
    while selected_coffee not in coffee_options:
        selected_coffee = input("Type the name of the coffee you would like: ").strip().lower()

        if selected_coffee not in coffee_options:
            print("Invalid option, try again.")

    # Get the original coffee name with the correct capitalization.
    real_coffee_name = coffee_options[selected_coffee]

    # Create a order history
    with open(ORDER_ARCHIVE, "a", encoding="UTF-8") as archive:
        archive.write(real_coffee_name + "\n")

    # Choose one random message from the selected coffee's message list.
    random_message = random.choice(messages_per_coffee[real_coffee_name])

    print(f"\nHere is your {real_coffee_name}")
    print(random_message)
    print("\n------------------------------\n")


def ask_to_order_again():
    """Ask the user if they want to order another coffee."""
    answer = input("Do you want to order another coffee? yes/no: ").strip().lower()

    # Validate the answer so only 'yes' or 'no' are accepted.
    while answer != "yes" and answer != "no":
        answer = input("Please type yes or no: ").strip().lower()

    return answer


def main():
    """Run the main coffee shop program."""
    greeting = welcome_message()
    print(greeting)

    input("Press Enter to continue...")

    keep_ordering = "yes"

    # Main loop: the user can order several coffees before leaving.
    while keep_ordering == "yes":
        choose_coffee()
        keep_ordering = ask_to_order_again()

    print("Thank you for visiting Wandering Coffee Beans!")
    print("May your coffee be strong and your bugs be easy to find.")


if __name__ == "__main__":
    main()
