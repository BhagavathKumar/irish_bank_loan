# Include logic to calculate emi for different loan types
# provided by different banks for different emi types
# There is also provision to compare loan provided by different Irish Banks

from tabulate import tabulate

class LoanCalculator:
    
    def __init__(self):
        self.bank = None
        self.loan_type = None
        self.amount = 0.0
        self.years = 0
        self.emi_frequency = None
        self.interest_rate_dict = {}
        self.interest_rate = 0
        self.number_of_installments = 0
        self.installments_per_year = 0

    def get_user_input(self, mode):
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
        if mode == 1:

            # Type 1 : EMI for a specific bank
            print("***Welcome to EMI Calculator for a Specific Bank***\n")
            print("Bank Types: AIB, BOI, Revolute, Avant Money, An Post")
            print("Loan Types: Personal Loan, Student Loan, Car Loan")

            self.bank = input("Enter the bank name: ")
            self.loan_type = input("Enter the loan type: ").lower()

        elif mode == 2:

            # Type 2 : Compare EMI across banks
            print("***Welcome to Bank Loan Comparision***")
            print("Loan Types: Personal Loan, Student Loan, Car Loan")

            self.loan_type = input("Enter the loan type: ").lower()

        self.amount = float(input("Enter the loan amount: "))
        self.years = int(input("Enter the repayment period (in years): "))
        print("EMI Frquency: Weekly, Fornightly or Monthly")
        self.emi_frequency = input("Enter EMI frequency: ").lower()

        # Get the intrest rate dictionary for particular loan type
        # Will use for mode:2 to comapre emi's
        self.interest_rate_dict = self.get_intrest_rate()
        self.interest_rate = self.interest_rate_dict.get(self.bank, 0)

        # Calculate total number of installments and installments per year
        self.number_of_installments, self.installments_per_year = self.calculate_intallments()

    def get_intrest_rate(self):
        # Dictionary to store different loan types, banks and their intrest rates
        interest_rates = {
            "personal loan":{
                "AIB":8.95,
                "BOI":8.5,
                "Revolute":6.5,
                "Avant Money":8.7,
                "An Post":8.2
            }
            # "Student Loan":{
            #     "AIB":,
            #     "BOI":,
            #     "Revolute":,
            #     "Avant Money":,
            #     "An Post":
            # },
            # "Car Loan":{
            #     "AIB":,
            #     "BOI":,
            #     "Revolute":,
            #     "Avant Money":,
            #     "An Post":
            # }
        }

        # Get the intrest rate for the particular loan type for a bank
        return interest_rates.get(self.loan_type, {})
    
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
        print(f"Bank: {self.bank}")
        print(f"Loan type: {self.loan_type}")
        print(f"Loan Amount: €{self.amount}")
        print(f"Repayment Period: {self.years} years")
        print(f"EMI Frequency: {self.emi_frequency.capitalize()}\n")
        print(f"EMI: €{emi} ({self.emi_frequency.capitalize()})")
        print(f"Total Payment: €{total_payment:}")
        print(f"Total Interest: €{total_interest:}")
        print(f"Interest Rate of {self.bank} for {self.loan_type}: {self.interest_rate}")

    def compare_emis(self):
        # if self.loan_type not in self.interest_rate_dict:
        #     print("Invalid loan type. Please try again.")
        #     return

        table_data = []
        
        print(f"\n--- EMI Comparison for {self.loan_type.capitalize()} ---\n")

        # Loop through each bank
        for bank, rate in self.interest_rate_dict.items():
            # Self interest rate and bank from the dictionary for the iteration
            self.bank = bank
            self.interest_rate = rate
            
            # Calculate the emi for particular bank
            emi = self.calculate_emi()
            total_payment = self.calculate_total_payment()
            total_interest = self.calculate_total_interest()

            table_data.append([bank, rate, emi, total_payment, total_interest])
            
        # Sort the output table by emi column
        table_data = sorted(table_data, key=lambda x: x[2])

        # Define table headings
        headers = ["Bank Name", "Interest Rate (%)", f"EMI - {self.emi_frequency.capitalize()} (€)", "Total Payment (€)", "Total Interest(€)"]

        # Print the output table
        print(tabulate(table_data, headers=headers, tablefmt="grid"))