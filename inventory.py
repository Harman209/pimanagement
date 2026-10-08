# product inventory management

products = {}

while True:
    print("\n===== PRODUCT INVENTORY MANAGEMENT =====")
    print("1. Add Product")
    print("2. Display All Products")
    print("3. Search by Product Code")
    print("4. Update Product Price")
    print("5. Delete Product")
    print("6. Low Stock Products (Quantity < 10)")
    print("7. Products in Price Range (Rs 500 - 1000)")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ").strip()

    if choice == '1':
        while True:
            code = input("\nEnter Product Code: ").strip()
            if code in products:
                print("Error: Product code already exists. Please enter a unique code.")
            else:
                name = input("Enter Product Name: ").strip()
                category = input("Enter Category: ").strip()
                price = float(input("Enter Price: "))
                quantity = int(input("Enter Quantity: "))

                products[code] = {
                    'name': name,
                    'category': category,
                    'price': price,
                    'quantity': quantity
                }
                print(f"Product '{name}' added successfully.")

            more = input("Do you want to add another product? (y/n): ").strip().lower()
            if more != 'y':
                break

    elif choice == '2':
        print("\n[Display Products - to be implemented]")
    elif choice == '3':
        print("\n[Search - to be implemented]")
    elif choice == '4':
        print("\n[Update - to be implemented]")
    elif choice == '5':
        print("\n[Delete - to be implemented]")
    elif choice == '6':
        print("\n[Low Stock - to be implemented]")
    elif choice == '7':
        print("\n[Price Range - to be implemented]")
    elif choice == '8':
        print("\nExiting program.")
        break
    else:
        print("Invalid choice. Please select an option between 1 and 8.")
