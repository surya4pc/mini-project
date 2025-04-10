#!/usr/bin/env python
# coding: utf-8

import re
import requests
from datetime import datetime
from tkinter import *
import tkinter as tk
from tkinter import ttk

class RealTimeCurrencyConverter():
    def __init__(self, url):
        self.data = self.get_exchange_rates(url)
        self.currencies = self.data['rates']

    def get_exchange_rates(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error in API request: {e}")
            return None

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

        # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount

class HistoryPage(tk.Toplevel):
    def __init__(self, master, history):
        tk.Toplevel.__init__(self, master)
        self.title("Transaction History")
        self.geometry("400x200")

        self.create_history_gui(history)

    def create_history_gui(self, history):
        self.history_label = Label(self, text="Transaction History", font=('Courier', 15, 'bold'))
        self.history_label.pack(pady=10)

        for entry in history:
            history_entry_label = Label(self, text=entry, font=('Courier', 10))
            history_entry_label.pack()

class CurrencyConverterApp(tk.Tk):
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title('Currency Converter')
        self.currency_converter = converter

        self.configure_gui_layout()
        self.create_intro_labels()
        self.create_user_input_fields()
        self.create_conversion_fields()
        self.create_buttons()

    def configure_gui_layout(self):
        for i in range(6):
            self.rowconfigure(i, weight=1)
        for i in range(4):
            self.columnconfigure(i, weight=1)
        self.geometry("600x200")

    def create_intro_labels(self):
        self.welcome_label = Label(self, text='Welcome to Real Time Currency Converter', fg='blue', relief=tk.RAISED, borderwidth=3)
        self.welcome_label.config(font=('Courier', 15, 'bold'))
        self.welcome_label.grid(row=0, column=0, columnspan=4, pady=10, sticky='nsew')

        self.date_label = Label(self, text=f"1 Indian Rupee equals = {self.currency_converter.convert('INR','USD',1)} USD \n Date : {self.currency_converter.data['date']}", relief=tk.GROOVE, borderwidth=5)
        self.date_label.grid(row=1, column=1, columnspan=2, sticky='nsew')

    def create_user_input_fields(self):
        self.name_label = Label(self, text="Enter Your Name:", font=('Courier', 10))
        self.name_entry = Entry(self, bd=3, relief=tk.RIDGE, justify=tk.CENTER)
        self.name_label.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
        self.name_entry.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

        valid = (self.register(self.restrict_number_only), '%d', '%P')
        self.amount_field = Entry(self, bd=3, relief=tk.RIDGE, justify=tk.CENTER, validate='key', validatecommand=valid)
        self.converted_amount_field_label = Label(self, text='', fg='black', bg='white', relief=tk.RIDGE, justify=tk.CENTER, width=17, borderwidth=3)

        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("INR")
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD")

        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable, values=list(self.currency_converter.currencies.keys()), font=font, state='readonly', justify=tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable, values=list(self.currency_converter.currencies.keys()), font=font, state='readonly', justify=tk.CENTER)

        self.from_currency_dropdown.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')
        self.amount_field.grid(row=3, column=1, padx=10, pady=10, sticky='nsew')
        self.to_currency_dropdown.grid(row=3, column=2, padx=10, pady=10, sticky='nsew')
        self.converted_amount_field_label.grid(row=3, column=3, padx=10, pady=10, sticky='nsew')

    def create_conversion_fields(self):
        self.convert_button = Button(self, text="Convert", fg="black", command=self.perform_conversion)
        self.convert_button.config(font=('Courier', 10, 'bold'))
        self.convert_button.grid(row=4, column=1, columnspan=2, pady=10, sticky='nsew')

    def create_buttons(self):
        self.history_button = Button(self, text="Transaction History", fg="black", command=self.show_transaction_history)
        self.history_button.config(font=('Courier', 10, 'bold'))
        self.history_button.grid(row=5, column=1, columnspan=2, pady=10, sticky='nsew')

    def perform_conversion(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(from_curr, to_curr, amount)
        converted_amount = round(converted_amount, 2)

        self.converted_amount_field_label.config(text=str(converted_amount))

        user_name = self.name_entry.get()

        self.update_history(user_name, from_curr, to_curr, amount, converted_amount)

    def restrict_number_only(self, action, string):
        regex = re.compile(r'^[0-9]*\.?[0-9]*$')
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))

    def update_history(self, user_name, from_curr, to_curr, amount, converted_amount):
        history_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {user_name}: {amount} {from_curr} to {converted_amount} {to_curr}"

        if hasattr(self, 'history'):
            self.history.insert(0, history_entry)
            self.history = self.history[:10]
        else:
            self.history = [history_entry]

    def show_transaction_history(self):
        HistoryPage(self, self.history)

if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)
    app = CurrencyConverterApp(converter)
    app.mainloop()
