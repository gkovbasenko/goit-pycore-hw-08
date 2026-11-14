# goit-pycore-hw-08

Advanced address book with birthdays, CLI commands, object serialization (pickle), and comprehensive unit tests.

Built on OOP entities: `Field`, `Name`, `Phone`, `Birthday`, `Record`, and `AddressBook` with a command-line interface and support for pickle serialization.

## Instructions

### Setup

```bash
# Enter the project directory
cd goit-pycore-hw-08

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install in editable mode with dev dependencies
pip install -e ".[dev]"
```

### Run the Application

```bash
# Start the CLI assistant
python3 -m hw08
```

### Run Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/address_book/test_birthday.py -v

# Run specific test class
pytest tests/address_book/test_commands.py::TestAddContactCommand -v
```

### Available Commands

- `hello` — Get a greeting from the bot
- `add <name> [phone]` — Add a new contact or add phone to existing (phone is optional)
- `change <name> <old_phone> <new_phone>` — Change phone number for a contact
- `phone <name>` — Show phone numbers for a contact
- `all` — Show all contacts in address book
- `add-birthday <name> <DD.MM.YYYY>` — Add a birthday for a contact
- `show-birthday <name>` — Show birthday for a contact
- `birthdays` — Show upcoming birthdays in the next 7 days
- `close` / `exit` — Quit the program

### Requirements

- Python 3.10+
- No external dependencies
