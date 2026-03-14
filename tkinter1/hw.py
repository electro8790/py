import tkinter as tk
window = tk.Tk()
window.geometry("400x300")
window.title("Getting Started with Widgets")
description_label = tk.Label(window, text="Enter two numbers to calculate their product.", font=("Arial", 10))
description_label.pack(pady=10)    
label1 = tk.Label(window, text="Enter first number:")
label1.pack()
entry1 = tk.Entry(window, width=20)
entry1.pack()    
label2 = tk.Label(window, text="Enter second number:")
label2.pack()
entry2 = tk.Entry(window, width=20)
entry2.pack()
result_box = tk.Text(window, height=2, width=30, state=tk.DISABLED)
result_box.pack(pady=10)
calculate_button = tk.Button(window, text="Calculate Product", command=lambda: [
    result_box.config(state="normal"),
    result_box.delete("1.0", tk.END),
    result_box.insert(tk.END, f"Product: {int(entry1.get()) * int(entry2.get())}"),
    result_box.config(state="disabled")
])
calculate_button.pack(pady=10)
window.mainloop()

