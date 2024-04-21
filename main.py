import tkinter as tk
from interface import ReciboApp

def main():
    root = tk.Tk()
    app = ReciboApp(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()