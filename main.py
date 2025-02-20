from tkinter import Tk, StringVar, IntVar, Text, END
from tkinter.ttk import Label, Frame, Button, Entry, Spinbox, Radiobutton, Checkbutton, Style


def draw_name_input():
    name_var = StringVar()
    Label(main_frame, text="Name:").grid(column=0, row=0)
    entry_widget = Entry(main_frame, textvariable=name_var)
    entry_widget.grid(row=0, column=1)
    return name_var


def draw_age_input():
    age_var = IntVar()
    Label(main_frame, text="Age:").grid(row=1, column=0)
    spinbox_widget = Spinbox(main_frame,
                             textvariable=age_var,
                             width=4,
                             from_=1,
                             to=999)
    spinbox_widget.grid(row=1, column=1)
    return age_var


def draw_gender_input():
    gender_var = StringVar()  # 🏳️‍🌈
    Label(main_frame, text="Gender:").grid(row=2, column=0)
    spinbox_widget = Entry(main_frame, textvariable=gender_var)
    spinbox_widget.grid(row=2, column=1)
    return gender_var


def draw_politics_input():
    starting_row = 3

    label = Label(main_frame, text="Political position:")
    label.grid(row=starting_row, column=0)

    political_position_var = StringVar()
    for i, option in enumerate(["Left-wing", "Right-wing"]):
        radio_button_widget = Radiobutton(main_frame,
                                          text=option,
                                          value=option,
                                          variable=political_position_var)
        radio_button_widget.grid(row=starting_row + i, column=1, columnspan=1)

    return political_position_var


def draw_hobbies_input():
    starting_row = 5

    label = Label(main_frame, text="Hobbies:")
    label.grid(row=starting_row, column=0)

    HOBBIES = ["Stamp collecting", "Chess", "Reading", "Sports", "Walking"]
    hobbies_variables: dict[str, IntVar()] = {}
    for i, hobby in enumerate(HOBBIES):
        hobby_variable = hobbies_variables[hobby] = IntVar()
        radio_button_widget = Checkbutton(main_frame,
                                          text=hobby,
                                          variable=hobby_variable)
        radio_button_widget.grid(row=starting_row + i, column=1, columnspan=1)

    return hobbies_variables


def on_submit():
    included_hobbies = []
    for hobby, is_checked in hobbies.items():
        if is_checked.get():
            included_hobbies.append(hobby)

    hobbies_string = ", ".join(included_hobbies)

    output = f"""
Name: {name.get()}
Age: {age.get()}
Gender: {gender.get()}
Political position: {politics.get()}
Hobbies: {hobbies_string}
    """.strip()

    output_widget.replace("0.0", END, output)

    with open("questionnaire_results.txt", "w", encoding="utf-8") as file:
        file.write(output)


window = Tk()
window.title("Tkinter questionnaire")

main_frame = Frame(window, padding=10)
main_frame.grid()

# Use the more modern Clam theme for tk widgets
style = Style()
style.theme_use("clam")

name = draw_name_input()
age = draw_age_input()
gender = draw_gender_input()
politics = draw_politics_input()
hobbies = draw_hobbies_input()

submit_button = Button(main_frame, command=on_submit, text="Submit")
submit_button.grid(row=10, column=0, columnspan=2)

output_widget = Text(main_frame, wrap="word", width=40, height=10)
output_widget.grid(row=11, column=0, columnspan=2)

# Label(main_frame, text="Hello World!").grid(column=0, row=0)
# Button(main_frame, text="Quit", command=window.destroy).grid(column=1, row=0)
window.mainloop()
