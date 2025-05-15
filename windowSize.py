import pygetwindow as gw
import tkinter as tk
from tkinter import ttk
# import time
import os

set1width = -999
set1height = -999


def getOpenWindow():
    windows = gw.getAllWindows()
    window_titles = [window.title for window in windows if window.title]
    return window_titles


def getSize(wind_title, width_entry, height_entry):
    wind = gw.getWindowsWithTitle(wind_title)[0]

    width_entry.delete(0, tk.END)
    width_entry.insert(0, wind.size[0])
    height_entry.delete(0, tk.END)
    height_entry.insert(0, wind.size[1])

    return wind.size


def setSize(wind_title, width_entry, height_entry):
    wind = gw.getWindowsWithTitle(wind_title)[0]
    try:
        wind.resizeTo(int(width_entry.get()), int(height_entry.get()))
        wind.moveTo(0, 0)
    # setSize(wind, int(width_entry.get()), int(height_entry.get()))
    except ValueError:
        print("Invalid input. Please enter a number.")

    except Exception as e:
        print("Error: ", e)


def set1(wind_title, width_entry, height_entry):
    global set1width, set1height
    if set1width == -999 and set1height == -999:
        if width_entry.get() == "" or height_entry.get() == "":
            print("Widht or Height is empty -> run getSize()")
            getSize(wind_title, width_entry, height_entry)
        else:
            pass
        set1width = width_entry.get()
        set1height = height_entry.get()
        print(f"set1width: {set1width}, set1height: {set1height}")

    else:
        print(f"set1width: {set1width}, set1height: {set1height}")
        wind = gw.getWindowsWithTitle(wind_title)[0]
        wind.resizeTo(int(set1width), int(set1height))
        wind.moveTo(0, 0)


def clear():
    global set1width, set1height
    set1width = -999
    set1height = -999
    print(f"clear! -> set1width: {set1width}, set1height: {set1height}")


def gui():

    root = tk.Tk()
    root.title("window adjustment")

    root.minsize(300, 200)
    root.maxsize(600, 400)
    root.resizable(True, True)
    # icon
    icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
    root.iconbitmap(icon_path)
    root.config(bg="lightblue")

    window_titles = getOpenWindow()
    wind_dropdown = ttk.Combobox(root, values=window_titles, width=50)
    wind_dropdown.pack()

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
                                       height_entry)
                           )
    set_button.pack(side="left", padx=5, pady=5)

    set1_button = tk.Button(root, text="set1",
                            command=lambda: set1(wind_dropdown.get(),
                                                 width_entry, height_entry)
                            )
    set1_button.pack(side="left", padx=5, pady=5,
                     )

    # cancel_button
    cancel_button = tk.Button(root, text="Cancel",
                              command=root.destroy)
    cancel_button.pack(side="bottom", anchor="e", padx=5, pady=5)

    clear_button = tk.Button(root, text="Clear",
                             command=lambda: clear())
    clear_button.pack(side="bottom", anchor="e", padx=5, pady=5)

    root.mainloop()


if __name__ == '__main__':
    # window = gw.getWindowsWithTitle('Book1 - Excel')[0]
    # window.move(0, 0)
    # time.sleep(1)
    # window.moveTo(0, 0)
    # print(window.size)
    # width, height = getSize()
    # print(f"wdith: {width}, height: {height}")
    # setSize(window, width, height)

    gui()
