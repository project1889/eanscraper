# EAN Scraper User Manual

## Introduction

The EAN Scraper is a web application developed to scrape websites and retrieve information about products based on a given brand name. It lists all websites, EANs (European Article Numbers), product titles, and sales prices it can find for each EAN from that brand.

This user manual provides step-by-step instructions on how to install the necessary dependencies and use the EAN Scraper web application.

## Installation

To install the EAN Scraper, follow these steps:

1. Make sure you have Python installed on your system. If not, download and install Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Download the EAN Scraper code files from the provided source.

3. Open a terminal or command prompt and navigate to the directory where you downloaded the EAN Scraper code files.

4. Create a virtual environment (optional but recommended) by running the following command:

   ```
   python -m venv myenv
   ```

   Replace `myenv` with the desired name for your virtual environment.

5. Activate the virtual environment by running the appropriate command based on your operating system:

   - **Windows:**

     ```
     myenv\Scripts\activate
     ```

   - **Mac/Linux:**

     ```
     source myenv/bin/activate
     ```

6. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary packages, including `beautifulsoup4` and `requests`.

7. The EAN Scraper is now installed and ready to use.

## Usage

To use the EAN Scraper web application, follow these steps:

1. Open a terminal or command prompt and navigate to the directory where you downloaded the EAN Scraper code files.

2. Activate the virtual environment (if you created one) by running the appropriate command (as mentioned in the installation steps).

3. Run the following command to start the EAN Scraper web application:

   ```
   python main.py
   ```

4. The EAN Scraper GUI window will open.

5. Enter the brand name for which you want to scrape EANs and product information in the "Brand Name" field.

6. Click the "Scrape" button to initiate the scraping process.

7. The EAN Scraper will start scraping the specified websites for the given brand name.

8. Once the scraping process is complete, the results will be displayed in the text area below the "Scrape" button. The results will include the website name, EAN, product title, and sales price for each product found.

9. You can repeat the process by entering a new brand name and clicking the "Scrape" button again.

10. To exit the EAN Scraper web application, simply close the GUI window.

## Troubleshooting

If you encounter any issues while installing or using the EAN Scraper, please ensure that you have followed the installation steps correctly and have the necessary dependencies installed. If the issue persists, you can contact our support team for assistance.

## Conclusion

The EAN Scraper web application provides a convenient way to scrape websites and retrieve product information based on a given brand name. By following the installation and usage instructions provided in this user manual, you can easily utilize the EAN Scraper to gather the desired information efficiently.