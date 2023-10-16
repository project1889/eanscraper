'''
GUI implementation for the EAN scraper web application.
'''
from tkinter import Tk, Label, Entry, Button, Text
from scraper import EANScraper
class ScraperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("EAN Scraper")
        self.brand_label = Label(root, text="Brand Name:")
        self.brand_label.pack()
        self.brand_entry = Entry(root)
        self.brand_entry.pack()
        self.scrape_button = Button(root, text="Scrape", command=self.scrape)
        self.scrape_button.pack()
        self.result_text = Text(root)
        self.result_text.pack()
    def scrape(self):
        brand_name = self.brand_entry.get()
        scraper = EANScraper()
        try:
            results = scraper.scrape_brand(brand_name)
            self.result_text.delete(1.0, "end")
            for result in results:
                self.result_text.insert("end", result + "\n")
        except Exception as e:
            self.result_text.delete(1.0, "end")
            self.result_text.insert("end", f"Error: {e}")