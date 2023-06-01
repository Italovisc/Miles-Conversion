import tkinter as tk
import ttkbootstrap as ttk


# [CONVERSION]
def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)


# [WINDOW]
window = ttk.Window(themename='journal')
window.title('Miles Conversion')
window.geometry('350x200')

# [WIDGETS]
# title
title_label = ttk.Label(
    master=window, 
    text ='Miles to Kilometers', 
    font='Georgia 24 bold'
    )
title_label.pack()

# input
entry_int = tk.IntVar()
input_frame = ttk.Frame(master=window)

entry = ttk.Entry(
    master=input_frame, 
    textvariable=entry_int
    )
button = ttk.Button(
    master=input_frame, 
    text='Convert', 
    command=convert
    )
input_frame.pack(pady=10)
entry.pack(pady=5)
button.pack()

# output
output_string = tk.StringVar()

output_label = ttk.Label(
    master=window, 
    text='Output', 
    font='Georgia 24', 
    textvariable=output_string
    )
output_label.pack(pady=5)

# [RUN WINDOW]
window.mainloop()
