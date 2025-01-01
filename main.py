# Include logic to calculate emi for different loan types
# provided by different banks for different emi types
# There is also provision to compare loan provided by different Irish Banks
# which include AIB, BOI, Avant Money, An Post and Revolute
# In the first version, the emi for personal loan of above banks are calculated

import constants as const
from errors import ValidationErrors

class LoanCalculator:
    
    def __init__(self):
        self.bank = None
        self.loan_type = None
        self.amount = 0.0
        self.years = 0
        self.emi_frequency = None
        self.interest_rate = 0
        self.number_of_installments = 0
        self.installments_per_year = 0

    def get_user_input(self):
        """
        Collect user input based on selected mode
        Initialize all the nexessary fields for calculations.

        The following variables will be intialized from user input:
        - bank, loan_type, amount, years, emi_frequency

        The following variables required for emi calculation 
        are calculated from following functions:
        - interest_rate_dict from get_interest_rate()
        - number_of_installments, installments_per_year from calculate_intallments()
        """

        # EMI for a specific bank
        print(const.bank_message)
        self.bank = input("Enter the bank name: ").lower()
        self.loan_type = input("Enter the loan type: ").lower()
        self.amount = int(input("Enter the loan amount: "))
        self.years = int(input("Enter the repayment period (in years): "))
        print("EMI Frquency: Weekly, Fornightly or Monthly")
        self.emi_frequency = input("Enter EMI frequency: ").lower()

        # Error handling for amount, years and emi_frequency
        ValidationErrors.validate_loan_amount(self.amount)
        ValidationErrors.validate_no_year(self.years)
        ValidationErrors.validate_emi_period(self.emi_frequency)

        # Get interest rate for the particular bank
        self.interest_rate = self.get_intrest_rate()

        # Calculate total number of installments and installments per year
        self.number_of_installments, self.installments_per_year = self.calculate_intallments()

    def get_intrest_rate(self):

        # Get whole interest rate dict form contants.py
        interest_rates = const.interest_rates

        # Error handling for invalid loan_types and banks
        ValidationErrors.validate_loan(self.loan_type, interest_rates.keys())
        ValidationErrors.valiadate_bank(self.loan_type, self.bank, interest_rates)

        # Get the intrest rate for the particular loan type for a bank
        return interest_rates.get(self.loan_type, {}).get(self.bank, 0)
    
    def calculate_intallments(self):
        """
        Evaluate the number of installments based on the EMI frequency
        There are 4.33 week/month. Hence:
        Weekly: 52 installments per year
        Fortnightly: 26 installments per year
        Monthly: 12 installments per year
        """
        if self.emi_frequency == 'weekly':
            return self.years * 52, 52
        elif self.emi_frequency == 'fortnightly':
            return self.years *26, 26
        elif self.emi_frequency == 'monthly':
            return self.years * 12, 12
        else:
            raise ValueError("Invalid EMI frequency. Choose from 'weekly', 'fortnightly', or 'monthly'.")

    def calculate_emi(self):
        """
        Calculate the EMI:
        EMI = [P * r * (1 + r)^n] / [(1 + r)^n - 1]
        where:
        - P = Principal (loan) amount
        - r = Interest rate per installment (annual interest / number of installments per year)
        - n = Number of installments
        """

        p = self.amount
        r = self.interest_rate / (100 * self.installments_per_year)
        n = self.number_of_installments

        emi = (p * r * (1 + r)**n) / ((1 + r)**n - 1)
        emi = round(emi, 2)
        return emi
    
    # Calculate total amount to be paid back to bank
    def calculate_total_payment(self):
        emi = self.calculate_emi()
        total_payment = round((emi * self.number_of_installments), 2)
        return total_payment
    
    # Calculate total intrest amount paid to bank
    def calculate_total_interest(self):
        total_payment = self.calculate_total_payment()
        total_interest = round((total_payment - self.amount), 2)
        return total_interest
    
    def display_results(self):

        # Calculate the emi, total amount to pay and total interest
        emi = self.calculate_emi()
        total_payment = self.calculate_total_payment()
        total_interest = self.calculate_total_interest()

        # Display the results
        print("\n---- Loan Details ----\n")
        print(f"Bank: {self.bank.capitalize()}")
        print(f"Loan type: {self.loan_type.capitalize()}")
        print(f"Loan Amount: €{self.amount}")
        print(f"Repayment Period: {self.years} Years")
        print(f"EMI Frequency: {self.emi_frequency.capitalize()}\n")
        print(f"EMI: €{emi} ({self.emi_frequency.capitalize()})")
        print(f"Total Payment: €{total_payment:}")
        print(f"Total Interest: €{total_interest:}")
        print(f"Interest Rate of {self.bank.capitalize()} for {self.loan_type.capitalize()}: {self.interest_rate}")
        print(const.important_note)