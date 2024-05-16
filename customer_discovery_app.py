# customer_discovery_app.py

import csv
import sqlite3
from pymongo import MongoClient
from tkinter import Tk, Label, Button, Entry, Text, END, messagebox, Frame
import os
import webbrowser

class Customer:
    def __init__(self, email, boolean_value, favorite_number):
        self.email = email
        self.boolean_value = boolean_value
        self.favorite_number = favorite_number

class CustomerDiscoveryApp:
    def __init__(self, data_file='customer_data.csv', db_type='csv'):
        self.data_file = data_file
        self.db_type = db_type
        self.customers = self.load_customers()

    def load_customers(self):
        customers = []
        if self.db_type == 'csv':
            try:
                with open(self.data_file, 'r') as file:
                    reader = csv.reader(file)
                    next(reader)  # Skip header
                    for row in reader:
                        email, boolean_value, favorite_number = row
                        customers.append(Customer(email, boolean_value == 'True', int(favorite_number)))
            except FileNotFoundError:
                pass
        elif self.db_type == 'qlite':
            conn = sqlite3.connect(self.data_file)
            c = conn.cursor()
            c.execute("SELECT * FROM customers")
            rows = c.fetchall()
            for row in rows:
                email, boolean_value, favorite_number = row
                customers.append(Customer(email, boolean_value == 'True', int(favorite_number)))
            conn.close()
        elif self.db_type == 'ongodb':
            client = MongoClient()
            db = client[self.data_file]
            collection = db.customers
            for document in collection.find():
                email = document['email']
                boolean_value = document['boolean_value']
                favorite_number = document['favorite_number']
                customers.append(Customer(email, boolean_value, favorite_number))
            client.close()
        return customers

    def save_customers(self):
        if self.db_type == 'csv':
            with open(self.data_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Email', 'Boolean Value', 'Favorite Number'])  # Header
                for customer in self.customers:
                    writer.writerow([customer.email, str(customer.boolean_value), customer.favorite_number])
        elif self.db_type == 'qlite':
            conn = sqlite3.connect(self.data_file)
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS customers (email TEXT, boolean_value INTEGER, favorite_number INTEGER)")
            for customer in self.customers:
                c.execute("INSERT INTO customers VALUES (?,?,?)", (customer.email, int(customer.boolean_value), customer.favorite_number))
            conn.commit()
            conn.close()
        elif self.db_type == 'ongodb':
            client = MongoClient()
            db = client[self.data_file]
            collection = db.customers
            for customer in self.customers:
                document = {'email': customer.email, 'boolean_value': customer.boolean_value, 'favorite_number': customer.favorite_number}
                collection.insert_one(document)
            client.close()

    def add_customer(self, email, boolean_value, favorite_number):
        if any(customer.email == email for customer in self.customers):
            messagebox.showerror("Error", "Duplicate email found.")
            return
        self.customers.append(Customer(email, boolean_value, favorite_number))
        self.save_customers()

    def get_customers(self):
        return self.customers

class GUI:
    def __init__(self, master, app):
        self.master = master
        self.app= app
        self.master.title("Customer Discovery App")
        self.master.geometry("400x300")

        self.email_label = Label(master, text="Email:")
        self.email_label.pack()
        self.email_entry = Entry(master)
        self.email_entry.pack()

        self.boolean_label = Label(master, text="Boolean Value:")
        self.boolean_label.pack()
        self.boolean_entry = Entry(master)
        self.boolean_entry.pack()

        self.favorite_label = Label(master, text="Favorite Number:")
        self.favorite_label.pack()
        self.favorite_entry = Entry(master)
        self.favorite_entry.pack()

        self.add_button = Button(master, text="Add Customer", command=self.add_customer)
        self.add_button.pack()

        self.list_button = Button(master, text="List Customers", command=self.list_customers)
        self.list_button.pack()

        self.text_area = Text(master)
        self.text_area.pack()

        self.exit_button = Button(master, text="Exit", command=self.master.destroy)
        self.exit_button.pack()

        self.download_button_frame = Frame(master)
        self.download_button_frame.pack()

        self.csv_download_button = Button(self.download_button_frame, text="Download CSV", command=self.download_csv)
        self.csv_download_button.grid(row=0, column=0, padx=5, pady=5)

        self.sqlite_download_button = Button(self.download_button_frame, text="Download SQLite", command=self.download_sqlite)
        self.sqlite_download_button.grid(row=0, column=1, padx=5, pady=5)

    def add_customer(self):
        email = self.email_entry.get()
        boolean_value = self.boolean_entry.get() == 'True'
        favorite_number = int(self.favorite_entry.get())
        self.app.add_customer(email, boolean_value, favorite_number)
        self.email_entry.delete(0, END)
        self.boolean_entry.delete(0, END)
        self.favorite_entry.delete(0, END)

    def list_customers(self):
        self.text_area.delete(1.0, END)
        customers = self.app.get_customers()
        for customer in customers:
            self.text_area.insert(END, f"Email: {customer.email}, Boolean Value: {customer.boolean_value}, Favorite Number: {customer.favorite_number}\n")

    def download_csv(self):
        if self.app.db_type != 'csv':
            self.app.save_customers()
        filename = os.path.basename(self.app.data_file)
        webbrowser.open(f"file:///{os.path.realpath(self.app.data_file)}")

    def download_sqlite(self):
        if self.app.db_type != 'qlite':
            self.app.save_customers()
        filename = os.path.basename(self.app.data_file)
        webbrowser.open(f"file:///{os.path.realpath(self.app.data_file)}")

def main():
    db_type = input("Choose a database type (csv, sqlite, mangoDB): ")
    app = CustomerDiscoveryApp(db_type=db_type)
    root = Tk()
    gui = GUI(root, app)
    root.mainloop()

if __name__ == '__main__':
    main()
