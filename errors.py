# Error handling for different user inputs

import constants as const

class ValidationErrors:
    
    def validate_loan_amount(amount, min_amount=1000, max_amount=100000):
        if not (min_amount <= amount <= max_amount):
            raise ValueError(f"Loan amount of '{amount}' is invalid. It should be between {min_amount} and {max_amount}.")
        
    def validate_no_year(year, max_year = 10):
        if year > max_year:
            raise ValueError(f"Invalid repayment period '{year}'. It should be between 1 to {max_year} years.")
        
    def validate_loan(loan_type, valid_loan_types):
        if loan_type not in valid_loan_types:
            raise ValueError(f"Invalid loan type '{loan_type}'. Valid loan types are: {', '.join(valid_loan_types)}")
        
    def valiadate_bank(loan_type, bank, interest_rates):
        if loan_type not in interest_rates:
            raise ValueError(f"Invalid loan type '{loan_type}'. Valid loan types are: {', '.join(interest_rates.keys())} ")
        if bank not in interest_rates[loan_type]:
            raise ValueError(f"Invalid bank '{bank}' for loan type '{loan_type}'. Valid banks are: {', '.join(interest_rates[loan_type].keys())}")
        
    def validate_emi_period(emi_period):
        valid_emi_periods = const.valid_emi_period
        if emi_period not in valid_emi_periods:
            raise ValueError(f"Invalid EMI frequency '{emi_period}'. Valid EMI frequencies are: {', '.join(valid_emi_periods[:])}")