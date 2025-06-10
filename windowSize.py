import os
import tkinter as tk
from tkinter import ttk
import pygetwindow as gw

SET1WIDTH = -999
SET1HEIGHT = -999
SET2WIDTH = -999
SET2HEIGHT = -999


def updateWindowList(wind_dropdown):
    windows = gw.getAllWindows()
    window_titles = [window.title for window in windows if window.title]
    wind_dropdown['values'] = window_titles
    print("update window list in dropdown")


def getSize(wind_title, width_entry, height_entry):
    wind = gw.getWindowsWithTitle(wind_title)[0]
    width_entry.delete(0, tk.END)
    width_entry.insert(0, wind.size[0])
    height_entry.delete(0, tk.END)
    height_entry.insert(0, wind.size[1])
    return wind.size


def setSize(wind_title, width_entry, height_entry, choice):
    wind = gw.getWindowsWithTitle(wind_title)[0]
    gui = gw.getWindowsWithTitle("window adjustment")[0]
    global SET1WIDTH, SET1HEIGHT, SET2WIDTH, SET2HEIGHT
    try:
        if choice.get() == "Set1":
            if SET1WIDTH == -999 and SET1HEIGHT == -999:
                if width_entry.get() == "" or height_entry.get() == "":
                    print("Widht or Height is empty -> run getSize()")
                    getSize(wind_title, width_entry, height_entry)
                else:
                    pass
                SET1WIDTH = width_entry.get()
                SET1HEIGHT = height_entry.get()
                print(
                    f"Set Initial -> SET1WIDTH: {SET1WIDTH}, SET1HEIGHT: {SET1HEIGHT}")

            else:
                # wind = gw.getWindowsWithTitle(wind_title)[0]
                wind.moveTo(0, 0)
                wind.resizeTo(int(SET1WIDTH), int(SET1HEIGHT))
                print(
                    f"Set Window Size :: SET1WIDTH: {SET1WIDTH}, SET1HEIGHT: {SET1HEIGHT}")
        elif choice.get() == "Set2":
            if SET2WIDTH == -999 and SET2HEIGHT == -999:
                if width_entry.get() == "" or height_entry.get() == "":
                    print("Widht or Height is empty -> run getSize()")
                    getSize(wind_title, width_entry, height_entry)
                else:
                    pass
                SET2WIDTH = width_entry.get()
                SET2HEIGHT = height_entry.get()
                print(
                    f"Set Initial -> SET2WIDTH: {SET2WIDTH}, SET2HEIGHT: {SET2HEIGHT}")

            else:
                # wind = gw.getWindowsWithTitle(wind_title)[0]
                wind.moveTo(0, 0)
                wind.resizeTo(int(SET2WIDTH), int(SET2HEIGHT))
                print(
                    f"Set Window Size -> SET2WIDTH: {SET2WIDTH}, SET2HEIGHT: {SET2HEIGHT}")
        elif choice.get() == "manual":
            wind.moveTo(0, 0)
            wind.resizeTo(int(width_entry.get()), int(height_entry.get()))
            print(
                f"Set Window Size manual -> WIDTH : {width_entry.get()}, HEIGHT: {height_entry.get()}")

        gui.activate()
    # setSize(wind, int(width_entry.get()), int(height_entry.get()))
    except ValueError:
        print("Invalid input. Please enter a number.")

    except Exception as e:
        print("Error: ", e)


def clear(choice):
    global SET1WIDTH, SET1HEIGHT, SET2WIDTH, SET2HEIGHT
    try:
        if choice.get() == "Set1":
            SET1WIDTH = -999
            SET1HEIGHT = -999
            print(
                f"clear! -> SET1_WIDTH: {SET1WIDTH}, SET1_HEIGHT: {SET1HEIGHT}")
        elif choice.get() == "Set2":
            SET2WIDTH = -999
            SET2HEIGHT = -999
            print(
                f"clear! -> SET2_WIDTH: {SET2WIDTH}, SET2_HEIGHT: {SET2HEIGHT}")
    except Exception as e:
        print("Error: ", e)


def print_choice(choice, width_entry, height_entry):
    global SET1WIDTH, SET1HEIGHT, SET2WIDTH, SET2HEIGHT
    try:
        if choice.get() == "Set1":
            print(f"mode : {choice.get()}, w = {SET1WIDTH}, h = {SET1HEIGHT}")
            width_entry.delete(0, tk.END)
            width_entry.insert(0, SET1WIDTH)
            height_entry.delete(0, tk.END)
            height_entry.insert(0, SET1HEIGHT)
        elif choice.get() == "Set2":
            print(f"mode : {choice.get()}, w = {SET2WIDTH}, h = {SET2HEIGHT}")
            width_entry.delete(0, tk.END)
            width_entry.insert(0, SET2WIDTH)
            height_entry.delete(0, tk.END)
            height_entry.insert(0, SET2HEIGHT)
        elif choice.get() == "manual":
            print(f"mode : {choice.get()}")
    except Exception as e:
        print("Error: ", e)


def gui():
    root = tk.Tk()
    root.title("window adjustment")

    root.minsize(300, 250)
    root.maxsize(800, 400)
    root.resizable(True, True)

    # icon
    icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
    root.iconbitmap(icon_path)
    root.config(bg="lightblue")

    # window_titles = getOpenWindow()
    wind_dropdown = ttk.Combobox(root, values=[], width=40)
    wind_dropdown.bind("<Button-1>",
                       lambda event: updateWindowList(wind_dropdown))
    wind_dropdown.grid(row=0, column=0, columnspan=4,
                       sticky='w', padx=5, pady=5)

    # width_label
    width_label = tk.Label(root, width=8, height=1, text="Width")
    width_label.grid(row=1, column=0, sticky='w', padx=5, pady=5)
    # width_entry
    width_entry = tk.Entry(root, width=15)
    width_entry.grid(row=1, column=1, sticky='w', padx=5, pady=5)

    # height_label
    height_label = tk.Label(root, width=8, height=1, text="Height")
    height_label.grid(row=2, column=0, sticky='w', padx=5, pady=5)
    # height_entry
    height_entry = tk.Entry(root, width=15)
    height_entry.grid(row=2, column=1,
                      sticky='w', padx=5, pady=5)

    # get_button
    get_button = tk.Button(root, text="Get Size", width=7,
                           command=lambda: [size := getSize(wind_dropdown.get(), width_entry, height_entry),
                                            print(size)
                                            ])
    get_button.grid(row=7, column=0, sticky='w', padx=5, pady=5)

    # set_button
    set_button = tk.Button(root, text="Set size", width=7,
                           command=lambda:
                               setSize(wind_dropdown.get(),
                                       width_entry,
                                       height_entry,
                                       choice)
                           )
    set_button.grid(row=7, column=1, sticky='w', padx=5, pady=5)

    # label_frame
    label_frame = tk.LabelFrame(root, text="Please select mode")
    # label_frame.pack(side="left", anchor="w", padx=10,
    #                  pady=10, fill="both", expand=True)
    label_frame.grid(row=5, column=0, rowspan=2,
                     columnspan=3, sticky='w', padx=5, pady=5)

    # choice for Racio button
    choice = tk.StringVar()
    choice.set("manual")

    radio1 = tk.Radiobutton(label_frame, text="Set1",
                            variable=choice, value="Set1", command=lambda:
                            print_choice(choice, width_entry, height_entry))
    radio1.grid(row=6, column=0, sticky='w', padx=5, pady=5)
    radio2 = tk.Radiobutton(label_frame, text="Set2",
                            variable=choice, value="Set2", command=lambda:
                            print_choice(choice, width_entry, height_entry))
    radio2.grid(row=6, column=1, sticky='w', padx=5, pady=5)
    radio3 = tk.Radiobutton(label_frame, text="manual",
                            variable=choice, value="manual", command=lambda:
                            print_choice(choice, width_entry, height_entry))
    radio3.grid(row=6, column=2, sticky='w', padx=5, pady=5)

    # clear_button
    clear_button = tk.Button(root, text="Clear", width=7,
                             command=lambda: clear(choice))
    clear_button.grid(row=8, column=0, sticky='w', padx=5, pady=5)

    # cancel_button
    cancel_button = tk.Button(root, text="Cancel", width=7,
                              command=root.destroy)
    cancel_button.grid(row=8, column=1, sticky='w', padx=5, pady=5)

    # start GUI
    root.mainloop()


if __name__ == '__main__':
    gui()
