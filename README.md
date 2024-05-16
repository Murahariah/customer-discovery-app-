## Customer Discovery App

### Introduction

The Customer Discovery App is a simple Python application designed to manage customer data using different types of databases such as CSV, SQLite, and MongoDB. It provides a graphical user interface (GUI) for users to add, list, and download customer data.

### Features

1. **Database Support**: Supports three types of databases:
   - CSV (Comma Separated Values)
   - SQLite
   - MongoDB

2. **Add Customer**: Allows users to add customer data including email, boolean value, and favorite number.

3. **List Customers**: Displays a list of all customers with their details.

4. **Download Data**: Provides options to download customer data in CSV and SQLite formats.

### Code Explanation

#### `customer_discovery_app.py`

### Imports

The script begins with importing necessary modules:

```python
import csv
import sqlite3
from pymongo import MongoClient
from tkinter import Tk, Label, Button, Entry, Text, END, messagebox, Frame
import os
import webbrowser
```

- `csv`: Module to handle CSV files.
- `sqlite3`: Module to interact with SQLite databases.
- `pymongo`: Module for MongoDB interaction.
- `Tkinter`: GUI toolkit for building the application's graphical interface.
- `os`: Module for interacting with the operating system.
- `webbrowser`: Module for opening URLs in web browsers.

### Customer Class

Defines the `Customer` class to represent customer data:

```python
class Customer:
    def __init__(self, email, boolean_value, favorite_number):
        self.email = email
        self.boolean_value = boolean_value
        self.favorite_number = favorite_number
```

- Attributes:
  - `email`: Customer's email address.
  - `boolean_value`: Boolean value representing some customer attribute.
  - `favorite_number`: Customer's favorite number.

### CustomerDiscoveryApp Class

Defines the main application class responsible for managing customer data:

```python
class CustomerDiscoveryApp:
    def __init__(self, data_file='customer_data.csv', db_type='csv'):
        self.data_file = data_file
        self.db_type = db_type
        self.customers = self.load_customers()
```

- `data_file`: File name or path where customer data is stored.
- `db_type`: Type of database used to store customer data (default is CSV).
- `customers`: List to store `Customer` objects.

### load_customers Method

Loads customer data from the specified database type:

```python
def load_customers(self):
    customers = []
    if self.db_type == 'csv':
        # Load from CSV file
    elif self.db_type == 'qlite':
        # Load from SQLite database
    elif self.db_type == 'ongodb':
        # Load from MongoDB database
    return customers
```

- Depending on the `db_type`, loads data from CSV, SQLite, or MongoDB.

### save_customers Method

Saves customer data to the specified database type:

```python
def save_customers(self):
    if self.db_type == 'csv':
        # Save to CSV file
    elif self.db_type == 'qlite':
        # Save to SQLite database
    elif self.db_type == 'ongodb':
        # Save to MongoDB database
```

- Depending on the `db_type`, saves data to CSV, SQLite, or MongoDB.

### GUI Class

Constructs the graphical user interface for the application:

```python
class GUI:
    def __init__(self, master, app):
        # GUI elements initialization
        # Entry fields for email, boolean value, and favorite number
        # Buttons for adding customers, listing customers, and exiting
        # Text area for displaying customer information
        # Buttons for downloading data in CSV and SQLite formats
```

- Initializes GUI elements using Tkinter widgets.

### add_customer Method

Adds a new customer when the "Add Customer" button is clicked:

```python
def add_customer(self):
    email = self.email_entry.get()
    boolean_value = self.boolean_entry.get() == 'True'
    favorite_number = int(self.favorite_entry.get())
    self.app.add_customer(email, boolean_value, favorite_number)
    # Clear entry fields after adding customer
```

- Retrieves data from entry fields, converts to appropriate types, and adds a new customer.

### list_customers Method

Displays all customers when the "List Customers" button is clicked:

```python
def list_customers(self):
    self.text_area.delete(1.0, END)
    customers = self.app.get_customers()
    for customer in customers:
        # Display customer information in text area
```

- Clears the text area and populates it with customer information.

### download_csv and download_sqlite Methods

Downloads customer data in CSV and SQLite formats respectively:

```python
def download_csv(self):
    # Save customer data if not already in CSV format
    # Open CSV file in web browser

def download_sqlite(self):
    # Save customer data if not already in SQLite format
    # Open SQLite file in web browser
```

- Saves customer data in the respective format and opens the file in the default web browser.

### Main Function

Starts the application by creating an instance of `CustomerDiscoveryApp` and launching the GUI:

```python
def main():
    # Prompt user to choose a database type
    # Initialize the application with the chosen database type
    # Create Tkinter root window and GUI instance
    # Start the Tkinter event loop
```

- Prompts the user to choose a database type, initializes the application, and starts the GUI.

---

Feel free to expand upon this README and provide additional details or instructions as needed.
### Usage

1. Run the `customer_discovery_app.py` script.
2. Choose a database type (csv, sqlite, or mangoDB).
3. Use the GUI to add, list, and download customer data.

### Output

![Screenshot 2024-05-17 010520](https://github.com/Murahariah/customer-discovery-app-/assets/122876058/2b38ef4d-1dbb-4ed4-b10a-826c65765d02)

![Screenshot (1122)](https://github.com/Murahariah/customer-discovery-app-/assets/122876058/538fb96e-4fc4-4e2f-acee-cffbb8bc80ef)
