# Irish Bank Loan Calculator

This command line calculator can be used to calculate the loan that been provided by some prominent Irish banks. Major banks include:
- AIB (Allied Irish Bank)
- BOI (Bank of Ireland)
- Avant Money
- An Post
- Revolute


## Version 1

In the first version, we are only focusing on Personal Loan provided by these banks. The interest rates are picked from the respective bank websites.

- **Features**:
  - EMI calculation for a specific bank.
  - Simple functionality to calculate and display monthly EMI.

- **Example Usage**

  * Provide the details shown as an example below when prompted.
    ```
    Enter the bank name: aib
    Enter the loan type: personal loan
    Enter the loan amount: 10000
    Enter the repayment period (in years): 2
    EMI Frquency: Weekly, Fornightly or Monthly
    Enter EMI frequency: weekly
    ```
  * After providing the details, and if they are valid, the user will get the response similar to below:
    ```
    Bank: Aib
    Loan type: Personal loan
    Loan Amount: €10000
    Repayment Period: 2 Years
    EMI Frequency: Weekly

    EMI: €105.1 (Weekly)
    Total Payment: €10930.4
    Total Interest: €930.4
    Interest Rate of Aib for Personal loan: 8.95
    ```

- **How to Run**:
  1. Clone the repository:
     ```
     git clone https://github.com/BhagavathKumar/irish_bank_loan.git
     ```
  2. Switch to the `main` branch:
     ```
     git checkout main
     ```
  3. Run `run.py` to calculate EMI for a specific bank.
  
### Note: 
- Please note that the loan calculator results are for illustrative purpose only. 
- The actual interest rate assigned will be based on the credit score of the applicant.
- The interest rates are fetched from the respective banks official websites. The rates will be changed in due time.
- Before applying for loan, please read the full terms and conditions provided by each bank.

## Future Versions

Some of the features that are planning to be included in the future versions are:
- Different loan types (Student Loan, Car Loan, House Loan etc.) will be included.
- EMI comparison across multiple banks for different loan types, and customer can choose the one which is best suitable for them.

## Reference
- AIB Loans (https://aib.ie/our-products/loans)
- Bank of Ireland Loans (https://personalbanking.bankofireland.com/borrow/loans/)
- Avant Money Personal Loans (https://www.avantmoney.ie/personal-loans)
- An Post Money Loans (https://www.anpost.com/Money/Low-Fixed-Rate-Loans)
- Revolut Loans (https://www.revolut.com/en-IE/personal-loans/)
