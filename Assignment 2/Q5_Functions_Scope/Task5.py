
# Task 5: Functions, Parameters and Scope
# Context: College Canteen Order System


# --------------------------------------------------
# PART 1: Demonstrate the default-list bug
# --------------------------------------------------

def add_item_buggy(item, order=[]):
    order.append(item)
    return order


print("PART 1: DEFAULT LIST BUG")
print("Buggy calls:")
print(add_item_buggy("Tea"), add_item_buggy("Vada"))

# Show the default list stored by the function.
print("Stored default:", add_item_buggy.__defaults__)


# --------------------------------------------------
# PART 2: Correct the bug
# --------------------------------------------------

def add_item(item, order=None):
    # Create a new list if no order was supplied.
    if order is None:
        order = []

    order.append(item)
    return order


print("\nPART 2: CORRECTED FUNCTION")
print("Separate calls:")
print(add_item("Tea"))
print(add_item("Vada"))


# Test three customers in sequence.
customer1 = []
customer2 = []
customer3 = []

add_item("Tea", customer1)
add_item("Vada", customer1)

add_item("Coffee", customer2)
add_item("Samosa", customer2)

add_item("Juice", customer3)
add_item("Sandwich", customer3)

print("\nThree independent customer orders:")
print("Customer 1:", customer1)
print("Customer 2:", customer2)
print("Customer 3:", customer3)


# --------------------------------------------------
# PART 3: Positional, keyword and default parameters
# --------------------------------------------------

def greet_customer(name, message="Welcome to our canteen"):
    print(message + ", " + name + "!")


print("\nPART 3: PARAMETER TYPES")
greet_customer("Anu")  # Positional argument + default message
greet_customer(name="Bala", message="Good afternoon")


# --------------------------------------------------
# PART 4: Return more than one value
# --------------------------------------------------

def calculate_bill(amount, gst_rate=0.05):
    gst = amount * gst_rate
    final_total = amount + gst
    return final_total, gst


print("\nPART 4: BILL AND GST")
total, gst = calculate_bill(100)

print(f"Bill before GST: Rs.100.00")
print(f"GST: Rs.{gst:.2f}")
print(f"Final total: Rs.{total:.2f}")


# --------------------------------------------------
# PART 5: Local and global scope
# --------------------------------------------------

canteen_name = "Campus Canteen"
orders_processed = 0


def show_canteen():
    local_message = "Order received"
    print("Global variable:", canteen_name)
    print("Local variable:", local_message)


def count_order():
    global orders_processed
    orders_processed += 1
    print("Orders processed:", orders_processed)


print("\nPART 5: LOCAL AND GLOBAL")
show_canteen()
count_order()
count_order()


# --------------------------------------------------
# PART 6: Nonlocal scope using a closure
# --------------------------------------------------

def make_order_counter():
    count = 0

    def add_order():
        nonlocal count
        count += 1
        return count

    return add_order


print("\nPART 6: NONLOCAL SCOPE")
counter = make_order_counter()
print("Order count:", counter())
print("Order count:", counter())
print("Order count:", counter())


# --------------------------------------------------
# PART 7: Time and space analysis
# --------------------------------------------------

print("\nPART 7: COMPLEXITY")
print("Adding one item to a list: O(1) amortised time")
print("Storing n items in one customer's order: O(n) space")
print("Each customer receives an independent order list.")
