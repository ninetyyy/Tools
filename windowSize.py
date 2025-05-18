import os
import tkinter as tk
from tkinter import ttk
import pygetwindow as gw

SET1WIDTH = -999
SET1HEIGHT = -999
SET2WIDTH = -999
SET2HEIGHT = -999


# def getOpenWindow():
#     windows = gw.getAllWindows()
#     window_titles = [window.title for window in windows if window.title]
#     return window_titles


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
                    f"Set Initial :: SET1WIDTH: {SET1WIDTH}, SET1HEIGHT: {SET1HEIGHT}")

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

    # setSize(wind, int(width_entry.get()), int(height_entry.get()))
    except ValueError:
        print("Invalid input. Please enter a number.")

    except Exception as e:
        print("Error: ", e)


def set1(wind_title, width_entry, height_entry):
    global SET1WIDTH, SET1HEIGHT
    if SET1WIDTH == -999 and SET1HEIGHT == -999:
        if width_entry.get() == "" or height_entry.get() == "":
            print("Widht or Height is empty -> run getSize()")
            getSize(wind_title, width_entry, height_entry)
        else:
            pass
        SET1WIDTH = width_entry.get()
        SET1HEIGHT = height_entry.get()
        print(f"SET1WIDTH: {SET1WIDTH}, SET1HEIGHT: {SET1HEIGHT}")

    else:
        print(f"SET1WIDTH: {SET1WIDTH}, SET1HEIGHT: {SET1HEIGHT}")
        wind = gw.getWindowsWithTitle(wind_title)[0]
        wind.resizeTo(int(SET1WIDTH), int(SET1HEIGHT))
        wind.moveTo(0, 0)


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


def print_choice(choice):
    print(choice.get())


def gui():

    root = tk.Tk()
    root.title("window adjustment")

    root.minsize(300, 200)
    root.maxsize(800, 400)
    root.resizable(True, True)
    # icon
    icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
    root.iconbitmap(icon_path)
    root.config(bg="lightblue")

    # window_titles = getOpenWindow()
    wind_dropdown = ttk.Combobox(root, values=[], width=50)
    wind_dropdown.bind("<Button-1>",
                       lambda event: updateWindowList(wind_dropdown))
    wind_dropdown.pack(side="top", anchor="w")

    # width_label
    width_label = tk.Label(root, text="Width")
    width_label.pack(side="top", padx=5, pady=5)

    # height_label
    height_label = tk.Label(root, text="Height")
    height_label.pack(side="top", padx=5, pady=5)
    # width_entry
    width_entry = tk.Entry(root, width=10)
    width_entry.pack(side="left", padx=5, pady=5)
    # height_entry
    height_entry = tk.Entry(root, width=10)
    height_entry.pack(side="left", padx=5, pady=5)

    # get_button
    get_button = tk.Button(root, text="Get Size",
                           command=lambda: [size := getSize(wind_dropdown.get(), width_entry, height_entry),
                                            print(size)
                                            # width_entry.delete(0, tk.END),
                                            # width_entry.insert(0, size[0]),
                                            # height_entry.delete(0, tk.END),
                                            # height_entry.insert(0, size[1])
                                            ])
    get_button.pack(side="left", padx=5, pady=5)

    # set_button
    set_button = tk.Button(root, text="Set size",
                           command=lambda:
                               setSize(wind_dropdown.get(),
                                       width_entry,
                                       height_entry, choice)
                           )
    set_button.pack(side="left", padx=5, pady=5)

    # set1_button
    set1_button = tk.Button(root, text="set1",
                            command=lambda: set1(wind_dropdown.get(),
                                                 width_entry, height_entry)
                            )
    set1_button.pack(side="left", padx=5, pady=5,
                     )
    # label_frame
    label_frame = tk.LabelFrame(root, text="Please select mode")
    label_frame.pack(side="left", anchor="w", padx=10,
                     pady=10, fill="both", expand=True)

    choice = tk.StringVar()
    choice.set("manual")

    radio1 = tk.Radiobutton(label_frame, text="Set1",
                            variable=choice, value="Set1", command=lambda: print_choice(choice))
    # radio1.bind("<Button-1>", lambda event: print_choice(choice))
    radio1.pack(side="left", anchor="w", padx=10, pady=10)
    radio2 = tk.Radiobutton(label_frame, text="Set2",
                            variable=choice, value="Set2", command=lambda: print_choice(choice))
    # radio2.bind("<Button-1>", lambda event: print_choice(choice))
    radio2.pack(side="left", anchor="w", padx=10, pady=10)
    radio3 = tk.Radiobutton(label_frame, text="manual",
                            variable=choice, value="manual", command=lambda: print_choice(choice))
    # radio3.bind("<Button-1>", lambda event: print_choice(choice))
    radio3.pack(side="left", anchor="w", padx=10, pady=10)

    # cancel_button
    cancel_button = tk.Button(root, text="Cancel",
                              command=root.destroy)
    cancel_button.pack(side="bottom", anchor="e", padx=5, pady=5)

    # clear_button
    clear_button = tk.Button(root, text="Clear",
                             command=lambda: clear(choice))
    clear_button.pack(side="bottom", anchor="e", padx=5, pady=5)

    root.mainloop()


if __name__ == '__main__':
    gui()
