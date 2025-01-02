import time
import tkinter as tk
from tkinter import messagebox, ttk

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def extract_details():
    
    keyword = keyword_entry.get()
    city = city_combobox.get()

    if not keyword or not city:
        messagebox.showerror("Input Error", "Please enter a keyword and select a city.")
        return

   
    try:
        driver = webdriver.Chrome()  # Replace with your browser's driver if not using Chrome
        driver.get("https://www.google.com/maps")

        # Search in Google Maps
        search_box = driver.find_element(By.ID, "searchboxinput")
        search_box.send_keys(f"{keyword} in {city}")
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)

        extracted_data = []
        while True:
            results = driver.find_elements(By.CLASS_NAME, "UaQhfb")

            for result in results:
                try:
                    title = result.find_element(By.CLASS_NAME, "qBF1Pd").text
                    rating_reviews = result.find_element(By.CLASS_NAME, "e4rVHe").text
                    category = result.find_element(By.XPATH, ".//div[@class='W4Efsd'][1]").text
                    address_phone = result.find_element(By.XPATH, ".//div[@class='W4Efsd'][2]").text

                    extracted_data.append({
                        "Title": title,
                        "Rating & Reviews": rating_reviews,
                        "Category": category,
                        "Address & Phone": address_phone
                    })
                except Exception as e:
                    continue

            
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
            time.sleep(5)

            
            if driver.find_elements(By.CLASS_NAME, "HlvSq"):
                break

        # Save data to an Excel file
        df = pd.DataFrame(extracted_data)
        df.to_excel("extracted_data.xlsx", index=False)

        messagebox.showinfo("Success", f"Data extracted successfully! Saved to extracted_data.xlsx")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

    finally:
        driver.quit()


root = tk.Tk()
root.title("Google Maps Data Extractor")
root.geometry("1100x900")


keyword_label = tk.Label(root, text="Enter Keyword:")
keyword_label.pack(pady=5)
keyword_entry = tk.Entry(root, width=250)
keyword_entry.pack(pady=5)


city_label = tk.Label(root, text="Select City:")
city_label.pack(pady=5)
cities = ["Gorakhpur", "Maharajganj", "Lucknow", "Basti" , "Banashankari" , "patna" , "chandigarh"]
city_combobox = ttk.Combobox(root, values=cities, state="readonly")
city_combobox.pack(pady=5)


extract_button = tk.Button(root, text="Extract Details", command=extract_details)
extract_button.pack(pady=20)

root.mainloop()
