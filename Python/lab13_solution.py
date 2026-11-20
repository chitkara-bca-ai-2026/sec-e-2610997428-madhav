inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

print("======================================")
print("       INVENTORY CONTROL SYSTEM")
print("======================================")

while True:
    print("\nSelect an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        print("\n--- Current Inventory ---")
        for item in inventory:
            print("-", item)

    elif choice == "2":
        item = input("Enter item name to add: ")

        if item in inventory:
            print("Item already exists in inventory.")
        else:
            inventory.append(item)
            print(f"[SUCCESS] '{item}' added to inventory.")

    elif choice == "3":
        item = input("Enter item name to remove: ")

        if item in inventory:
            inventory.remove(item)
            print(f"[SUCCESS] '{item}' removed from inventory.")
        else:
            print("Item not found in inventory.")

    elif choice == "4":
        inventory.sort()
        print("[SUCCESS] Inventory sorted alphabetically.")
        print("Updated Inventory:")
        for item in inventory:
            print("-", item)

    elif choice == "5":
        print("Exiting Inventory Control System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
