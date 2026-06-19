# Wandering Coffee Beans ☕

Wandering Coffee Beans is a beginner-friendly Python console project that simulates a small coffee shop. The user can enter their name, view a coffee menu, choose a drink, and receive a random motivational message based on the selected coffee.

This project was created as practice for basic Python concepts such as dictionaries, lists, functions, loops, user input validation, imports, and the `random` module.

## Features

- Greets the user by name.
- Displays a coffee menu with type, price, energy level, and description.
- Lets the user choose a coffee by typing its name.
- Accepts flexible input, such as `latte`, `LATTE`, or ` latte `.
- Shows a random motivational message for the selected coffee.
- Lets the user order another coffee or exit the program.
- Validates empty names, invalid coffee options, and yes/no answers.
- Save the orders in an archive

## Project structure

```text
coffee_shop/
├── main.py       # Main program logic and user interaction
├── coffee.py     # Coffee menu data
├── messages.py   # Motivational messages for each coffee
└── README.md     # Project documentation
```

## Requirements

- Python 3.x

No external libraries are required. The project only uses Python's built-in `random` module.

## How to run the project

1. Clone or download this repository.
2. Open a terminal inside the project folder.
3. Run the program with:

```bash
python main.py
```

Depending on your system, you may need to use:

```bash
python3 main.py
```

## How to use it

1. Enter your name when the program asks for it.
2. Press Enter to continue.
3. Read the coffee menu.
4. Type the name of the coffee you want.
5. Receive your selected coffee and a random message.
6. Type `yes` to order another coffee or `no` to exit.

## Available coffees

- Espresso
- Latte
- Expat Coffee
- Michi Lover
- Cold Brew
- Iced Mocha

## Concepts practiced

- Dictionaries
- Nested dictionaries
- Lists
- Functions
- Loops
- User input
- Input validation
- Importing data from other files
- Random selection with `random.choice()`
- Basic project organization

## Future improvements

- Add a graphical interface.
- Build a web version using HTML, CSS, and Flask.
- Allow users to select coffees by number.
- Add images for each coffee.
- Add a more visual and cozy design.

## Author

Created as a basic Python learning project by Paulina Aristizabal
