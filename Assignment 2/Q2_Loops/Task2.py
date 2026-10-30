
# Task 2: Loops that Count Attempts
# OTP verification at a bank kiosk

CORRECT_OTP = "123456"
SECURITY_ANSWER = "blue"


# Version 1: Using a while loop
def verify_while():
    attempts = 0

    while attempts < 3:
        entered = input("Enter OTP: ").strip()

        # Blank entries do not count
        if entered == "":
            print("Blank entry. Please try again.")
            continue

        attempts += 1

        if entered == CORRECT_OTP:
            print("Verification successful!")
            break

        print("Wrong OTP.")

        # pass does nothing; this is a placeholder for
        # possible audit logging after the second attempt.
        if attempts == 2:
            pass
    else:
        print("Three wrong attempts. Account locked for 30 minutes.")


# Version 2: Using for with range(3)
def verify_for():
    for attempt in range(3):
        # Keep asking until a non-blank OTP is entered.
        # A blank entry must not consume an attempt.
        while True:
            entered = input("Enter OTP: ").strip()

            if entered == "":
                print("Blank entry. Please try again.")
                continue

            break

        if entered == CORRECT_OTP:
            print("Verification successful!")
            break

        print("Wrong OTP. Counted attempt:", attempt + 1)
    else:
        print("Three wrong attempts. Account locked for 30 minutes.")


# Version 3: Updated rule with security question
def verify_with_security():
    attempts = 0

    while attempts < 3:
        entered = input("Enter OTP: ").strip()

        if entered == "":
            print("Blank entry. Please try again.")
            continue

        attempts += 1

        if entered == CORRECT_OTP:
            print("Verification successful!")
            return

        print("Wrong OTP. Counted attempt:", attempts)

    # This section runs only after three wrong OTP attempts.
    print("Three OTP attempts used.")
    answer = input("Security question: What is your sample colour? ")
    if answer.strip().lower() != SECURITY_ANSWER:
        print("Incorrect security answer.")
        print("Account locked for 30 minutes.")
        return

    print("Security answer correct. Two extra attempts allowed.")

    extra_attempts = 0

    while extra_attempts < 2:
        entered = input("Enter OTP for extra attempt: ").strip()

        if entered == "":
            print("Blank entry. Please try again.")
            continue

        extra_attempts += 1

        if entered == CORRECT_OTP:
            print("Verification successful!")
            break

        print("Wrong OTP. Extra attempt:", extra_attempts)
    else:
        print("Extra attempts exhausted.")
        print("Account locked for 30 minutes.")


# Version 4: Recursive alternative
def verify_recursive(attempts_left=3):
    if attempts_left == 0:
        print("Three wrong attempts. Account locked for 30 minutes.")
        return

    # Blank entries are retried in a loop so they do not
    # use an OTP attempt or create extra recursive calls.
    while True:
        entered = input("Enter OTP: ").strip()

        if entered != "":
            break

        print("Blank entry. Please try again.")

    if entered == CORRECT_OTP:
        print("Verification successful!")
        return

    print("Wrong OTP. Attempts remaining:", attempts_left - 1)
    verify_recursive(attempts_left - 1)


# Choose which version to test
print("OTP VERIFICATION")
print("1. While loop")
print("2. For loop")
print("3. Security question + extra attempts")
print("4. Recursive alternative")

choice = input("Choose 1, 2, 3 or 4: ").strip()

if choice == "1":
    verify_while()
elif choice == "2":
    verify_for()
elif choice == "3":
    verify_with_security()
elif choice == "4":
    verify_recursive()
else:
    print("Invalid choice. Run the program again.")
