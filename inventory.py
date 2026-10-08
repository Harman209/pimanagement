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
        code = input("\nEnter Product Code to update price: ").strip()
        if code in products:
            old_price = products[code]['price']
            print(f"Current price for {products[code]['name']} is Rs. {old_price:.2f}")
            new_price = float(input("Enter new price: "))
            products[code]['price'] = new_price
            print("Price updated successfully.")
        else:
            print(f"Product with code '{code}' not found.")

    elif choice == '5':
        code = input("\nEnter Product Code to delete: ").strip()
        if code in products:
            deleted_name = products[code]['name']
            del products[code]
            print(f"Product '{deleted_name}' (Code: {code}) removed successfully.")
        else:
            print(f"Product with code '{code}' not found.")

    elif choice == '6':
        low_stock_list = []
        for code, details in products.items():
            if details['quantity'] < 10:
                record = [code, details['name'], details['category'], details['price'], details['quantity']]
                low_stock_list.append(record)

        if not low_stock_list:
            print("\nNo products found with quantity less than 10.")
        else:
            print("\n--- Low Stock Products (Quantity < 10) ---")
            print(f"{'Code':<10}{'Name':<20}{'Category':<22}{'Price (Rs)':<12}{'Quantity':<10}")
            print("-" * 74)
            for item in low_stock_list:
                print(f"{item[0]:<10}{item[1]:<20}{item[2]:<22}{item[3]:<12.2f}{item[4]:<10}")

    elif choice == '7':
        found = False
        print("\n--- Products in Price Range (Rs. 500 - Rs. 1000) ---")
        print(f"{'Code':<10}{'Name':<20}{'Category':<22}{'Price (Rs)':<12}{'Quantity':<10}")
        print("-" * 74)
        for code, details in products.items():
            if 500 <= details['price'] <= 1000:
                print(f"{code:<10}{details['name']:<20}{details['category']:<22}{details['price']:<12.2f}{details['quantity']:<10}")
                found = True
        if not found:
            print("No products found in the price range Rs. 500 to Rs. 1000.")

    elif choice == '8':
        print("\nExiting program.")
        break
    else:
        print("Invalid choice. Please select an option between 1 and 8.")
