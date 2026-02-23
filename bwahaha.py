# ----- IMPORTING ESSENTIAL LIBRARIES -----

import matplotlib.pyplot as plt
import customtkinter as ctk
import warnings
warnings.filterwarnings('ignore')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
from PIL import Image


# -----  CREATING EMPTY LISTS FOR DATA ENTRY -----

expense = []
amount = []

# ----- INITIALISING UI STYLE -----

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('blue')

# ----- UI -----

app = ctk.CTk()
app.configure(fg_color='#E6FAFF')
app.title('Expense Visualiser')
app.geometry('1200x800')
app.resizable(False, False)

# ----- loading bg image -----

bg_image = ctk.CTkImage(
    light_image=Image.open('image4.jpg'),
    dark_image=Image.open('image4.jpg'),
    size=(1200, 800)
)

bg_label = ctk.CTkLabel(app, image=bg_image, text = '')
bg_label.place(x=0, y=0, relwidth=1, relheight=1)



# ----- LAYOUT -----

app.grid_columnconfigure(0, weight=2) # bottom left
app.grid_columnconfigure(1, weight=1) # bottom right
app.grid_rowconfigure(0, weight=1) # uppermost
app.grid_rowconfigure(1, weight=2)

plot_frame = ctk.CTkFrame(app, fg_color='white')
plot_frame.grid(column=0, row=1, pady = 20, padx = 20 , sticky='nsew') # pie will be plotted in this frame

entry_frame = ctk.CTkFrame(app, fg_color='white')
entry_frame.grid(column=1, row=1, pady = 20, padx = 20 , sticky='nsew') # user is prompted entries in this frame

title_frame = ctk.CTkFrame(app, height = 20, fg_color='white')
title_frame.grid(column=0, row=0, columnspan = 2, pady = 20, padx = 20, sticky='nsew' )
title_frame.grid_propagate(False) # this is time pass

# ----- FUNCTIONS -----

def cleared():
    net_salary.delete(0, 'end')
    expense_name.delete(0, 'end')
    expense_amount.delete(0, 'end')

def add_expense():
    try:
        name = expense_name.get().lower().strip()
        net = float(net_salary.get())
        val = float(expense_amount.get())

        # ---- WARNINGS BASED ON PERCENTAGE RULES ----

        if name == "food" and val > 0.20 * net:
            messagebox.showwarning(
                "Warning",
                "Food expense exceeds 10% of net salary"
            )

        if name == "rent" and val > 0.20 * net:
            messagebox.showwarning(
                "Warning",
                "Rent exceeds 20% of net salary"
            )

        if name == "savings" and val < 0.20 * net:
            messagebox.showwarning(
                "Warning",
                "Savings are less than 20% of net salary"
            )

        if not name:
            return


        expense.append(name)
        amount.append(float(expense_amount.get()))

        expense_name.delete(0, 'end')
        expense_amount.delete(0, 'end')




    except ValueError:
        messagebox.showerror("Error", "Please enter a numeric value")


def plot_graph():
    for widget in plot_frame.winfo_children():
        widget.destroy()

    fig, ax = plt.subplots(figsize = (4,4))
    ax.pie(amount, labels = expense, autopct = '%1.2f%%', startangle=90)
    ax.set_title('Monthly Expense Visualiser')

    canvas = FigureCanvasTkAgg(fig, plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

# -----  BUTTONS AND ENTRIES -----

label1 = ctk.CTkLabel(entry_frame, height=20, text = 'Enter Net Salary', font = ctk.CTkFont(size = 20, family = 'Impact', weight = 'bold'))
label1.grid(column=0, row=0, pady = 10, padx = 10, sticky='nsew')
net_salary = ctk.CTkEntry(entry_frame, placeholder_text = 'Float / Int', width=270)
net_salary.grid(column = 1, row=0, padx = 10, pady = 10)

label2 = ctk.CTkLabel(entry_frame, height=20, text = 'Enter Expense Name', font = ctk.CTkFont(size = 20, family = 'Impact', weight = 'bold'))
label2.grid(column = 0, row = 1, pady = 10, padx =10)
expense_name = ctk.CTkEntry(entry_frame, placeholder_text='food, rent, savings',   width=270)
expense_name.grid(column = 1, row = 1, padx = 10, pady = 10)

label3 = ctk.CTkLabel(entry_frame, height=20, text = 'Enter Amount spent', font = ctk.CTkFont(size = 20, family = 'Impact', weight = 'bold'))
label3.grid(column = 0, row = 2, padx = 10, pady = 10)
expense_amount = ctk.CTkEntry(entry_frame, width=270)
expense_amount.grid(column = 1, row = 2, padx = 10, pady = 10)

title_label = ctk.CTkLabel(title_frame, text='Monthly Expense Visualiser......', font = ctk.CTkFont(size = 40, family = 'Impact', weight = 'bold', slant='italic'))
title_label.grid(column = 0, row = 0, pady = 40, padx = 10, sticky = 'nsew')

clear_button = ctk.CTkButton(entry_frame, text='Clear', command=cleared, fg_color='#E6FAFF', hover_color='white', border_color='grey', border_width=2, text_color='black')
clear_button.grid(column = 1, row = 3, padx = 10, pady = 10, sticky='nsew')

add_entry = ctk.CTkButton(entry_frame, text = 'Add Expense', command=add_expense, fg_color='#E6FAFF', hover_color='white', border_color='grey' ,border_width=2,text_color='black')
add_entry.grid(column = 1, row = 4, padx = 10, pady = 10, sticky='nsew')

plot_pie = ctk.CTkButton(entry_frame, text='Plot', command = plot_graph, fg_color='#E6FAFF', hover_color='white', border_color='grey', border_width=2, text_color='black')
plot_pie.grid(column = 1, row = 5, padx = 10, pady = 10, sticky='nsew')

quit = ctk.CTkButton(entry_frame, text='Quit', command=app.destroy, fg_color='#E6FAFF', hover_color='white', border_color='grey', border_width=2,text_color='black')
quit.grid(column = 1, row = 6, padx = 10, pady = 10, sticky='nsew')

app.mainloop()