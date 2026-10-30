# Task 3: Vehicle Registration Number Validator
# Uses string methods and slicing only (no regular expressions).

def normalise(text):
    """Convert typed registration text to uppercase without spaces/hyphens."""
    return "".join(text.upper().replace("-", "").split())


def is_valid(reg):
    """Valid: 2 letters, 2 digits, 1-2 letters, 4 digits."""
    reg = normalise(reg)

    if len(reg) not in (9, 10):
        return False

    state = reg[:2]
    district = reg[2:4]
    series = reg[4:-4]
    vehicle_number = reg[-4:]

    return (
        len(state) == 2
        and state.isalpha()
        and len(district) == 2
        and district.isdigit()
        and len(series) in (1, 2)
        and series.isalpha()
        and len(vehicle_number) == 4
        and vehicle_number.isdigit()
    )


def format_registration(reg):
    """Format a valid registration as 'TN 09 AB 1234'."""
    reg = normalise(reg)

    if not is_valid(reg):
        return "Invalid registration number"

    return f"{reg[:2]} {reg[2:4]} {reg[4:-4]} {reg[-4:]}"


def main():
    print("VEHICLE REGISTRATION NUMBER VALIDATOR")
    print("-" * 45)

    test_numbers = [
        "tn 09 ab 1234",
        "KA-01-M-0007",
        "Tn09Ab1234",
        "TN9AB1234",
        "TN 22 1234 AB",
        "KA01ABC1234",
    ]

    print("\nPREDICTED TEST CASES / OBSERVED RESULTS")

    for raw in test_numbers:
        reg = normalise(raw)
        result = "valid" if is_valid(reg) else "INVALID"

        if is_valid(reg):
            formatted = format_registration(reg)
        else:
            formatted = result

        print(f"{raw:18} -> {reg:11} {result:7} {formatted}")

    print("\nADDITIONAL TESTS")

    for raw in [
        "MH12DE1433",
        "KA01AB123",
        "KA01AB12345",
        "KA01@B1234",
    ]:
        reg = normalise(raw)
        result = "valid" if is_valid(reg) else "INVALID"
        print(f"{raw:18} -> {reg:11} {result}")

    print("\nCUSTOM INPUT")
    user_text = input("Enter a vehicle registration number: ")
    reg = normalise(user_text)

    if is_valid(reg):
        print("Valid registration number")
        print("Receipt format:", format_registration(reg))
    else:
        print("Invalid registration number")


if __name__ == "__main__":
    main()
