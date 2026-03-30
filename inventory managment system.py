class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = int(quantity)

    def show_product(self):
        print(f"{self.name}: {self.quantity}")

    def update_stock(self, new_stock):
        self.quantity = int(new_stock)
        print("Stock updated successfully")


items = {}

try:
    with open("inventory.txt", "r") as file:
        for line in file:
            name, qty = line.strip().split(",")
            items[name] = Product(name, qty)
except FileNotFoundError:
    pass


while True:
    print("\n1. Add Product")
    print("2. View Products")
    print("3. Update Stock")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter product name: ")

        if name in items:
            print("Product already exists")
        else:
            qty = int(input("Enter quantity: "))
            items[name]= Product(name, qty)
            print("Product added")

    elif choice == "2":
        if not items:
            print("No products available")
        else:
            for produc in items.values():
                produc.show_product()

    elif choice == "3":
        name = input("Enter product name: ")

        if name in items:
            new_qty = int(input("Enter new quantity: "))
            items[name].update_stock(new_qty)
        else:
            print("Product not found")

    elif choice == "4":
        name = input("Enter product name to delete: ")

        if name in items:
            del items[name]
            print("Product deleted")
        else:
            print("Product not found")

    elif choice == "5":
        with open("inventory.txt", "w") as file:
            for product in items.values():
                file.write(f"{product.name},{product.quantity}\n")

        print("Data saved. Bye ")
        break

    else:
        print("Invalid choice")
