from main import LoanCalculator

def main():
    loan_calculator = LoanCalculator()

    print("\n---Bank Loan Calculator---")
    
    try:

        # Get user input
        loan_calculator.get_user_input()
        loan_calculator.display_results()


    except Exception as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":
    main()
