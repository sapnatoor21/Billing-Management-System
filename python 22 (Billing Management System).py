import tkinter as tk
from tkinter import messagebox


# Initialize main window
root = tk.Tk()
root.title("Billing Management System")
root.geometry("400x500")


# Variables to store item details
item_name_var = tk.StringVar()
quantity_var = tk.IntVar()
price_var = tk.DoubleVar()
delete_item_var = tk.StringVar()  # Variable to store the name of item to delete
bill_items = []


# Function to add item to the bill
def add_item():
    item_name = item_name_var.get()
    quantity = quantity_var.get()
    price = price_var.get()

    if item_name and quantity > 0 and price > 0:
        total_price = quantity * price
        bill_items.append({"name": item_name,"quantity": quantity, "price": price, "total": total_price})
        update_bill_display()
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Please enter valid item details.")


# Function to clear input fields
def clear_entries():
    item_name_var.set("")
    quantity_var.set(1)
    price_var.set(0,0)

# Function to delete an item from the bill
def delete_item():
    item_name = delete_item_var.get()
    found = False
    for item in bill_items:
        if item['name'] == item_name:
            bill_items.remove(item)
            found = True
            break
    if found:
        update_bill_display()
        delete_item_var.set("")
        messagebox.showinfo("Item Deleted", f"Item '{item_name}' has been deleted from the bill.")
    else:
        messagebox.showwarning("Delete Error", f"No item named '{item_name}' found.")

# Function to update bill display
def update_bill_display():
    bill_text.delete("1.0", tk.END) # clear existing text
    total_bill_amount = 0.0
    bill_text.insert(tk.END, f"{'Item':<10}{'Qty':<10}{'price':<10}{'Total':<10}\n")
    bill_text.insert(tk.END, "_" * 40 + "\n")
    for item in bill_items:
        bill_text.insert(tk.END, f"{item['name']:<10}{item['quantity']:<10} {item['price']:<10} {item['total']:<10}\n")
        total_bill_amount += item["total"]
    bill_text.insert(tk.END, "_" * 40 + "\n")
    bill_text.insert(tk.END, f"{'Total Amount:':<30}{total_bill_amount:.2f}\n")

# Layout for item details entry
tk.Label(root, text="Item Name").pack(pady=5)
tk.Entry(root, textvariable=item_name_var).pack()

tk.Label(root, text="Quantity").pack(pady=5)
tk.Entry(root, textvariable=quantity_var).pack()

tk.Label(root, text="Price").pack(pady=5)
tk.Entry(root, textvariable=price_var).pack()

tk.Button(root, text="Add Item", command=add_item).pack(pady=10)

# Layout for deleting an item
tk.Label(root, text="Enter Item Name to Delete").pack(pady=5)
tk.Entry(root, textvariable=delete_item_var).pack()
tk.Button(root, text="Delete Item", command=delete_item).pack(pady=10)

# Bill display area
bill_text = tk.Text(root, height=15, width=40)
bill_text.pack(pady=10)

# Set initial values for quantity and price
quantity_var.set(1)
price_var.set(0.0)

root.mainloop()
