# Simple Hotel Menu Program with Quantity Support

# Function to display categories
def display_categories():
    print("\nMenu Categories:")
    print("1. Starters")
    print("2. Main Course")
    print("3. Desserts")
    print("4. Drinks")

# Function to display items in a selected category
def display_menu(category):
    if category == "1":
        print("\nStarters:")
        print("1. Soup - ₹100")
        print("2. Spring Rolls - ₹150")
        print("3. Garlic Bread - ₹120")
    elif category == "2":
        print("\nMain Course:")
        print("1. Paneer Butter Masala - ₹250")
        print("2. Chicken Curry - ₹300")
        print("3. Veg Biryani - ₹200")
        print("4. Butter Naan - ₹50")
    elif category == "3":
        print("\nDesserts:")
        print("1. Gulab Jamun - ₹50")
        print("2. Ice Cream - ₹80")
        print("3. Brownie - ₹100")
    elif category == "4":
        print("\nDrinks:")
        print("1. Soda - ₹50")
        print("2. Coffee - ₹120")
        print("3. Lemonade - ₹60")

# Main program
def main():
    total_bill = 0
    selected_items = []  # Stores details of each selected item (name, quantity, total price)
    while True:
        display_categories()
        category = input("Select a category (1-4) or type 'stop' to finish: ").lower()
        if category == "stop":
            break
        elif category in ["1", "2", "3", "4"]:
            display_menu(category)
            while True:
                choice = input("Enter the number of the food item you want (or type 'back' to go back): ").lower()
                if choice == "back":
                    break
                
                # Get the quantity from the user
                quantity = input("Enter the quantity: ")
                if not quantity.isdigit():
                    print("Please enter a valid quantity.")
                    continue
                quantity = int(quantity)
                
                # Match the selected item
                if category == "1":  # Starters
                    if choice == "1":
                        item_name = "Soup"
                        price = 100
                    elif choice == "2":
                        item_name = "Spring Rolls"
                        price = 150
                    elif choice == "3":
                        item_name = "Garlic Bread"
                        price = 120
                    else:
                        print("Invalid choice. Please try again.")
                        continue
                elif category == "2":  # Main Course
                    if choice == "1":
                        item_name = "Paneer Butter Masala"
                        price = 250
                    elif choice == "2":
                        item_name = "Chicken Curry"
                        price = 300
                    elif choice == "3":
                        item_name = "Veg Biryani"
                        price = 200
                    elif choice == "4":
                        item_name = "Butter Naan"
                        price = 50
                    else:
                        print("Invalid choice. Please try again.")
                        continue
                elif category == "3":  # Desserts
                    if choice == "1":
                        item_name = "Gulab Jamun"
                        price = 50
                    elif choice == "2":
                        item_name = "Ice Cream"
                        price = 80
                    elif choice == "3":
                        item_name = "Brownie"
                        price = 100
                    else:
                        print("Invalid choice. Please try again.")
                        continue
                elif category == "4":  # Drinks
                    if choice == "1":
                        item_name = "Soda"
                        price = 50
                    elif choice == "2":
                        item_name = "Coffee"
                        price = 120
                    elif choice == "3":
                        item_name = "Lemonade"
                        price = 60
                    else:
                        print("Invalid choice. Please try again.")
                        continue
                
                # Calculate the total for this item
                item_total = price * quantity
                total_bill += item_total
                
                # Add item details to the selected_items list
                selected_items.append((item_name, quantity, item_total))
                print(f"Added {quantity} x {item_name} (₹{item_total}) to your bill.")
        else:
            print("Invalid category. Please try again.")
    
    # Display the final bill
    print("\nYour Final Bill:")
    for item_name, quantity, item_total in selected_items:
        print(f"- {quantity} x {item_name}: ₹{item_total}")
    print(f"Total Bill Amount: ₹{total_bill}")

# Run the program
if __name__ == "__main__":
    main()
