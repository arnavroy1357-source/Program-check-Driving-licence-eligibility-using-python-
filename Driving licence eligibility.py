def check_license_eligibility(age):
    if age < 0:
        return "❌ Invalid age. Please enter a positive number."
    elif age < 16:
        return "🚫 Too young! You cannot apply for a license yet."
    elif 16 <= age < 18:
        return "⚠️ You can apply for a learner's license only."
    elif 18 <= age <= 100:
        return "✅ You are eligible for a driving license.\n👉 PROCEED NOW"
    else:
        return "❌ Invalid age. Please enter a realistic age (0-100)."

def main():
    while True:
        print("\n" + "="*40)
        print("🚗 Driving License Eligibility Checker 🚗")
        print("="*40)
        print("1. Check Eligibility")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            try:
                age = int(input("\nEnter your age: "))
                print("\n" + check_license_eligibility(age))
            except ValueError:
                print("⚠️ Please enter a valid number for age.")
        elif choice == "2":
            print("\n👋 Thank you for using the system. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1 or 2.")

# Run the program
main()