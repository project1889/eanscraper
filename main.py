'''
Main file for the EAN scraper web application.
'''
from tkinter import Tk
from gui import ScraperGUI
def main():
    try:
        root = Tk()
        app = ScraperGUI(root)
        root.mainloop()
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()