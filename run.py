from main import LoanCalculator

def main():
    loan_calculator = LoanCalculator()

    print("Bank Loan Details")
    print("1. Calculate EMI for a specific bank and loan type.")
    print("2. Compare EMIs across different Irish banks for a particular loan type. (UNDER DEVELOPMENT)")
    mode = int(input("Select an option (1 or 2): "))

    # try:

    # Get user input
    loan_calculator.get_user_input(mode)

    if mode == 1:
        loan_calculator.display_results()

    elif mode == 2:
        loan_calculator.compare_emis()

    else:
        print("Invalid option selected. Please try again and select 1 or 2.")

    # except Exception as e:
    #     print(f"An error occured: {e}")


if __name__ == "__main__":
    main()
