import tkinter as tk
from quadratic_equation_solver_aletse import solver


def create_equation_label(text: str):
    return tk.Label(equation_frame, text=text,
                    font=("Regular", 14),
                    fg="#3d3176",
                    bg="white",
                    anchor="c")


def create_equation_entry():
    return tk.Entry(equation_frame, width=5, font=("Regular", 14),
                    fg="#c0c0c0",
                    bg="white",
                    justify="center")


def create_button(file, command):
    return tk.Button(buttons_frame, image=file, borderwidth=0, bg="#bab0e9", command=command)


def on_arrow_key(event):
    current_widget = event.widget
    if event.keysym == "Right":
        current_widget.tk_focusNext().focus()
    elif event.keysym == "Left":
        current_widget.tk_focusPrev().focus()


def calculate_result():
    try:
        text = None
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        result = solver(a, b, c)
        if result is None:
            text = "There is no solution,\nsince the discriminant is less than zero."
        elif isinstance(result, float):
            text = f"Answer:\n\n" \
                   f"x\u2081 = x\u2082 = {result}\n"
        elif len(result) == 2:
            x1, x2 = result[0], result[1]
            text = f"Answer:\n\n" \
                   f"x\u2081 = {x1}\n" \
                   f"x\u2082 = {x2}"
    except ValueError:
        text = "Values must be integers."
    result_label.config(text=text)
    result_label.pack(ipadx=10, ipady=10, pady=15)


def clear():
    result_label.pack_forget()
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)


window = tk.Tk()
window.geometry("600x500")
window.minsize(525, 450)
window.title("Calculator")
window.config(bg="#bab0e9")
photo = tk.PhotoImage(file="func.png")
window.iconphoto(False, photo)

title = tk.Label(window, text="Quadratic equation calculator",
                 font=("Regular", 18, "bold"),
                 fg="white",
                 bg="#3d3176",
                 anchor="c")
title.pack(fill="x", ipadx=30, ipady=30)

main_frame = tk.Frame(window, bg="#bab0e9")
main_frame.pack(padx=90)

instructions = tk.Label(main_frame, text="Enter the values of the constants in\nthe quadratic equation.",
                        font=("Regular", 14),
                        fg="#3d3176",
                        bg="#bab0e9",
                        anchor="c")
instructions.pack(ipadx=30, ipady=30)

equation_frame = tk.Frame(main_frame, bg="white", padx=5, pady=5)
equation_frame.pack()

label1 = create_equation_label("x\u00B2 +")
label2 = create_equation_label("x +")
label3 = create_equation_label("= 0")

entry_a = create_equation_entry()
entry_b = create_equation_entry()
entry_c = create_equation_entry()

entry_a.pack(side="left")
entry_a.insert(0, "-1")
entry_a.bind("<Right>", on_arrow_key)

label1.pack(side="left")

entry_b.pack(side="left")
entry_b.insert(0, "7")
entry_b.bind("<Right>", on_arrow_key)
entry_b.bind("<Left>", on_arrow_key)

label2.pack(side="left")

entry_c.pack(side="left")
entry_c.insert(0, "-10")
entry_c.bind("<Left>", on_arrow_key)

label3.pack(side="left")

buttons_frame = tk.Frame(main_frame, bg="#bab0e9", padx=10, pady=15)
buttons_frame.pack()

result_label = tk.Label(main_frame,
                        font=("Regular", 14),
                        fg="#3d3176",
                        bg="#bab0e9",
                        anchor="c")

calculate_image = tk.PhotoImage(file="calculate.png")
calculate_button = create_button(calculate_image, calculate_result)
clear_image = tk.PhotoImage(file="clear.png")
clear_button = create_button(clear_image, clear)

calculate_button.pack(side="left")
clear_button.pack(side="left")

window.mainloop()
