# ===== STORE INFO (Tuple) =====
store_info = ("Kirana Store",)

# ===== GST =====
gst = 18

# ===== PRODUCTS (price per KG) =====
products = {
    "rice": {"price": 60, "stock": 50},   # price per kg
    "wheat": {"price": 40, "stock": 30},
    "sugar": {"price": 45, "stock": 20},
    "oil": {"price": 120, "stock": 15}
}

# ===== CART (List) =====
cart = []

# ===== CUSTOMERS (Set) =====
customers = set()

print(f"Welcome to {store_info[0]} ({store_info[1]})")

while True:
    print("\n---- MENU ----")
    print("1. Show products")
    print("2. Buy product (KG wise)")
    print("3. Add new product (Admin)")
    print("4. Remove product (Admin)")
    print("5. Exit & Generate Bill")

    choice = int(input("Enter your choice: "))

    # ===== SHOW PRODUCTS =====
    if choice == 1:
        print("\nAvailable Products (Price per KG):")
        for item, info in products.items():
            print(f"{item.title()} - ₹{info['price']}/kg | Stock: {info['stock']} kg")

    # ===== BUY PRODUCT =====
    elif choice == 2:
        cname = input("Enter customer name: ")
        customers.add(cname)

        pname = input("Enter product name: ").lower()

        if pname not in products:
            print("❌ Product not available")
            continue

        kg = float(input("Enter quantity (in KG): "))

        if kg <= 0:
            print("❌ Invalid quantity")
            continue

        if kg > products[pname]["stock"]:
            print("❌ Not enough stock available")
            continue

        price_per_kg = products[pname]["price"]
        amount = kg * price_per_kg

        print(f"👉 {kg} kg {pname.title()} = ₹{amount}")

        # update stock
        products[pname]["stock"] -= kg

        # add to cart
        cart.append((pname, kg, price_per_kg, amount))

        print("✅ Item added to cart")

    # ===== ADD NEW PRODUCT =====
    elif choice == 3:
        pname = input("Enter new product name: ").lower()

        if pname in products:
            print("❌ Product already exists")
            continue

        price = float(input("Enter price per KG: "))
        stock = float(input("Enter stock (KG): "))

        products[pname] = {"price": price, "stock": stock}
        print("✅ Product added successfully")

    # ===== REMOVE PRODUCT =====
    elif choice == 4:
        pname = input("Enter product name to remove: ").lower()

        if pname in products:
            del products[pname]
            print("✅ Product removed")
        else:
            print("❌ Product not found")

    # ===== EXIT & BILL =====
    elif choice == 5:
        print("\n🧾 ---- FINAL BILL ----")
        total = 0

        for item in cart:
            pname, kg, price_per_kg, amount = item
            total += amount
            print(f"{pname.title()} | {kg} kg × ₹{price_per_kg} = ₹{amount}")

        gst_amount = total * gst / 100
        final_amount = total + gst_amount

        print(f"\nSubtotal: ₹{total}")
        print(f"GST ({gst}%): ₹{gst_amount}")
        print(f"Final Amount: ₹{final_amount}")

        print("\n👥 Customers Today:", customers)
        print("\n🙏 Thank you for shopping!")
        break

    else:

        print("❌ Invalid choice")
