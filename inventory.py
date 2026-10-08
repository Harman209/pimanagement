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
        if not products:
            print("\nInventory is empty. No products to display.")
        else:
            print("\n--- Stored Products ---")
            print(f"{'Code':<10}{'Name':<20}{'Category':<22}{'Price (Rs)':<12}{'Quantity':<10}")
            print("-" * 74)
            for code, details in products.items():
                print(f"{code:<10}{details['name']:<20}{details['category']:<22}{details['price']:<12.2f}{details['quantity']:<10}")

    elif choice == '3':
        code = input("\nEnter Product Code to search: ").strip()
        if code in products:
            item = products[code]
            print("\nProduct Found:")
            print(f"Code: {code}")
            print(f"Name: {item['name']}")
            print(f"Category: {item['category']}")
            print(f"Price: Rs. {item['price']:.2f}")
            print(f"Quantity: {item['quantity']}")
        else:
            print(f"Product with code '{code}' not found.")

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
