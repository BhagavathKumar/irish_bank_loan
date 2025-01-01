# some constant values that doesnot change in the project

# valid emi frequencies
valid_emi_period = ['weekly', 'fortnightly', 'monthly']

# Interest rates for different types of loan for different Irish banks
# !!! More detailes to be updaed in coming versions !!!
interest_rates = {
    "personal loan":{
        "aib":8.95,
        "boi":8.5,
        "revolute":6.5,
        "avant money":8.7,
        "an post":8.2
    }
}

# Bank message to be displayed before user input
bank_message = """
***Welcome to EMI Calculator for a Specific Bank***
When the user provided with the following details:
    - Bank Name: AIB, BOI, Revolute, Avant Money, An Post
    - Loan Types: Personal Loan. (Student Loan, Car Loan - under development!)
    - Total loan amount to be applied for
    - Repayment period in years
    - Preffered EMI frequency (Weekly, Fortnightly or Monthly
Our personalised loan calculator will calculate the amount repayable, 
frequent repayment amount, interest rate and cost of credit.

Provide the above details when prompted!
"""

important_note = """
Please note that the loan calculator results are for illustrative purpose only. 
The actual interest rate assigned will be based on the credit score of the applicant.
"""