
# Task 1: Decisions with Many Boundaries
# Electricity subsidy eligibility

households = [
    ("H1", 100, True, False),
    ("H2", 101, True, False),
    ("H3", 200, True, False),
    ("H4", 201, False, True),
    ("H5", 150, False, False),
    ("H6", 250, True, False),
    ("H7", 80, False, True),
    ("H8", 201, True, False),
]


# Version 1: Developer's faulty separate-if implementation
def subsidy_separate_if(units, ration_card, senior_member):
    decisions = []

    if units <= 100:
        decisions.append("Full subsidy")

    # BUG: This condition also accepts units below 101.
    if units <= 200 and ration_card:
        decisions.append("Partial subsidy")

    if units > 200 and senior_member:
        decisions.append("Senior exception subsidy")

    if len(decisions) == 0:
        decisions.append("No subsidy")

    return decisions


# Version 2: Correct if-elif-else implementation
def subsidy_if_elif(units, ration_card, senior_member):
    if units <= 100:
        return "Full subsidy"

    elif 101 <= units <= 200 and ration_card:
        return "Partial subsidy"

    elif units > 200 and senior_member:
        return "Senior exception subsidy"

    else:
        return "No subsidy"


# Alternative: match-case (Python 3.10 or later)
def subsidy_match(units, ration_card, senior_member):
    match True:
        case _ if units <= 100:
            return "Full subsidy"

        case _ if 101 <= units <= 200 and ration_card:
            return "Partial subsidy"

        case _ if units > 200 and senior_member:
            return "Senior exception subsidy"

        case _:
            return "No subsidy"


# Display and compare the results
print("ELECTRICITY SUBSIDY RESULTS")
print("-" * 75)

for name, units, ration_card, senior_member in households:
    separate_result = subsidy_separate_if(
        units, ration_card, senior_member
    )

    elif_result = subsidy_if_elif(
        units, ration_card, senior_member
    )

    match_result = subsidy_match(
        units, ration_card, senior_member
    )

    print(f"\nHousehold: {name}")
    print(f"Units consumed: {units}")
    print(f"Ration card: {ration_card}")
    print(f"Member above 80: {senior_member}")
    print(f"Separate if result: {separate_result}")
    print(f"if-elif-else result: {elif_result}")
    print(f"match-case result: {match_result}")
