#!/usr/bin/env python3

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the BankAccount with an optional initial balance."""
        self._account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount > 0:
            self._account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw a specified amount if sufficient funds are available."""
        if amount > self._account_balance:
            return False
        elif amount > 0:
            self._account_balance -= amount
            return True
        else:
            raise ValueError("Withdraw amount must be positive.")

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self._account_balance:.2f}")
