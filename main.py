
import tkinter as tk
from tkinter import ttk

exchange_rates = {
    "USD": 470,
    "EUR": 510,
    "KZT": 1,
    "GBP": 590,
    "CNY": 65
}
currency_symbols = {
    "USD": "$",
    "EUR": "€",
    "KZT": "₸",
    "GBP": "£",
    "CNY": "¥"
}
root = tk.Tk()
root.title("Конвертер валют")
root.geometry("400x600")
entry_amount = tk.Entry(root, font=("Arial", 20), justify="center")
entry_amount.pack(pady=10)
frame_to = tk.Frame(root)
frame_to.pack(pady=10)
label_to_symbol = tk.Label(frame_to, text=currency_symbols["KZT"], font=("Arial", 18))  
label_to_symbol.pack(side="left")
combo_to = ttk.Combobox(frame_to, values=list(exchange_rates.keys()), font=("Arial", 18), state="readonly", width=10)
combo_to.set("KZT")
combo_to.pack(side="left")
frame_from = tk.Frame(root)
frame_from.pack(pady=10)
label_from_symbol = tk.Label(frame_from, text=currency_symbols["EUR"], font=("Arial", 18))  
label_from_symbol.pack(side="left")
combo_from = ttk.Combobox(frame_from, values=list(exchange_rates.keys()), font=("Arial", 18), state="readonly", width=10)
combo_from.set("EUR")
combo_from.pack(side="left")
def update_from_symbol(event):
    label_from_symbol.config(text=currency_symbols[combo_from.get()])
def update_to_symbol(event):
    label_to_symbol.config(text=currency_symbols[combo_to.get()])
combo_from.bind("<<ComboboxSelected>>", update_from_symbol)
combo_to.bind("<<ComboboxSelected>>", update_to_symbol)
def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = combo_from.get()
        to_currency = combo_to.get()
        
        if from_currency in exchange_rates and to_currency in exchange_rates:
            converted_amount = amount * (exchange_rates[to_currency] / exchange_rates[from_currency])
            result_label.config(text=f"{converted_amount:.2f}")
    except ValueError:
        result_label.config(text="Ошибка ввода")
convert_button = tk.Button(root, text="Конверттеу", command=convert_currency, font=("Arial", 16))
convert_button.pack(pady=20)
result_label = tk.Label(root, text="0.00", font=("Arial", 24))
result_label.pack(pady=10)
root.mainloop()
