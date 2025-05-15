import pygetwindow as gw
import tkinter as tk
import time
import os


def getSize(wind):
    # w = wind.size.width
    # h = wind.size.height
    # return w, h
    return wind.size


def setSize(wind, width_entry, height_entry):
    # wind.moveTo(100, 100)
    try:
        wind.resizeTo(int(width_entry.get()), int(height_entry.get()))
        # setSize(wind, int(width_entry.get()), int(height_entry.get()))
    except Exception as e:
        print("Error: ", e)


def gui(wind):

    root = tk.Tk()
    root.title("window adjustment")

    root.minsize(300, 200)
    root.maxsize(600, 400)
    root.resizable(True, True)

    icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
    root.iconbitmap(icon_path)
    root.config(bg="lightblue")

    width_entry = tk.Entry(root, width=10)
    width_entry.pack(side="left", padx=5, pady=5)

    height_entry = tk.Entry(root, width=10)
    height_entry.pack(side="left", padx=5, pady=5)

    get_button = tk.Button(root, text="Get Size",
                           command=lambda: [size := getSize(wind),
                                            print(size),
                                            width_entry.delete(0, tk.END),
                                            width_entry.insert(0, size[0]),
                                            height_entry.delete(0, tk.END),
                                            height_entry.insert(0, size[1])
                                            ])
    get_button.pack(side="left", padx=5, pady=5)

    set_button = tk.Button(root, text="Set size",
                           command=lambda:
                               setSize(wind, width_entry, height_entry)
                           )
    set_button.pack(side="left", padx=5, pady=5)

    cancel_button = tk.Button(root, text="Cancel",
                              command=root.destroy)
    cancel_button.pack(side="bottom", anchor="e", padx=5, pady=5)

    root.mainloop()


if __name__ == '__main__':
    # window = gw.getWindowsWithTitle('Book1 - Excel')[0]
    # window.move(0, 0)
    time.sleep(3)
    window = gw.getActiveWindow()
    # window.moveTo(0, 0)
    # print(window.size)
    width, height = getSize(window)

    print(f"wdith: {width}, height: {height}")

    # setSize(window, width, height)

    gui(window)
