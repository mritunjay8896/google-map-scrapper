![gmap](https://github.com/user-attachments/assets/80b1f985-bce3-45f4-9bbc-e33b1194aa48)
![gmapscrapper](https://github.com/user-attachments/assets/376179cf-c2e7-4024-8f21-f1e8c697ac71)


<h1 style="text-align:center; color:#4CAF50;">Google Maps Data Extractor</h1>

<p style="text-align:center; color:#555;">
    This Python application extracts business information from Google Maps based on a specified keyword and city. 
    The extracted data, including titles, ratings, reviews, categories, and address/phone details, is saved to an Excel file for further use.
</p>

<h2 style="color:#2196F3;">Features</h2>
<ul>
    <li><b>Keyword Search:</b> Enter a keyword (e.g., "restaurants", "hotels") to search for businesses.</li>
    <li><b>City Selection:</b> Choose from a list of predefined cities.</li>
    <li><b>Data Extraction:</b> Extracts business names, ratings, reviews, categories, and contact information from Google Maps.</li>
    <li><b>Excel Export:</b> Saves the extracted data into an Excel file.</li>
</ul>

<h2 style="color:#2196F3;">Prerequisites</h2>
<p style="color:#555;">Ensure you have the following Python libraries installed:</p>
<ul>
    <li><b>selenium</b>: For automating the browser and extracting data from Google Maps.</li>
    <li><b>pandas</b>: For managing and saving extracted data in Excel format.</li>
    <li><b>tkinter</b>: For creating the graphical user interface (GUI).</li>
</ul>
<p>Install these libraries using pip:</p>
<pre><code>pip install selenium pandas tkinter</code></pre>

<h2 style="color:#2196F3;">Code Explanation</h2>

<h3 style="color:#4CAF50;">1. Setting Up the Selenium WebDriver</h3>
<p>The Selenium WebDriver is used to open Google Maps, search for businesses based on the provided keyword and city, and extract relevant data.</p>
<pre><code>
driver = webdriver.Chrome()  # Replace with your browser's driver if not using Chrome
driver.get("https://www.google.com/maps")
</code></pre>

<h3 style="color:#4CAF50;">2. Data Extraction</h3>
<p>The <b>extract_details()</b> function performs the extraction by searching Google Maps for businesses matching the given keyword and city. It extracts the business title, rating, category, and address/phone details for each result.</p>
<pre><code>
extracted_data = []
while True:
    results = driver.find_elements(By.CLASS_NAME, "UaQhfb")
    for result in results:
        title = result.find_element(By.CLASS_NAME, "qBF1Pd").text
        rating_reviews = result.find_element(By.CLASS_NAME, "e4rVHe").text
        category = result.find_element(By.XPATH, ".//div[@class='W4Efsd'][1]").text
        address_phone = result.find_element(By.XPATH, ".//div[@class='W4Efsd'][2]").text
        extracted_data.append({"Title": title, "Rating & Reviews": rating_reviews, "Category": category, "Address & Phone": address_phone})
</code></pre>

<h3 style="color:#4CAF50;">3. Exporting to Excel</h3>
<p>Once the data is collected, it is saved to an Excel file named <b>extracted_data.xlsx</b> using pandas.</p>
<pre><code>
df = pd.DataFrame(extracted_data)
df.to_excel("extracted_data.xlsx", index=False)
</code></pre>

<h2 style="color:#2196F3;">GUI Interface</h2>
<p>The app uses <b>tkinter</b> to create a graphical interface for the user to input a keyword and select a city. The interface includes:</p>
<ul>
    <li><b>Keyword Input:</b> Enter a keyword (e.g., "restaurant", "hotel").</li>
    <li><b>City Selection:</b> Choose a city from the dropdown list.</li>
    <li><b>Extract Button:</b> Initiates the extraction process and saves the results.</li>
</ul>

<h3 style="color:#4CAF50;">Example Layout</h3>
<table style="border:1px solid #ddd; width:100%; text-align:center;">
    <tr style="background-color:#f2f2f2;">
        <th>Business Title</th>
        <th>Rating & Reviews</th>
        <th>Category</th>
        <th>Address & Phone</th>
    </tr>
    <tr>
        <td>Restaurant XYZ</td>
        <td>4.5 (100 reviews)</td>
        <td>Restaurant</td>
        <td>123 Main St, +123456789</td>
    </tr>
    <tr>
        <td>Hotel ABC</td>
        <td>4.2 (50 reviews)</td>
        <td>Hotel</td>
        <td>456 Elm St, +987654321</td>
    </tr>
</table>

<h2 style="color:#2196F3;">How to Run</h2>
<ol>
    <li>Ensure you have installed the necessary libraries (Selenium, pandas, tkinter).</li>
    <li>Download the appropriate browser driver (e.g., ChromeDriver) for Selenium.</li>
    <li>Run the script:
        <pre><code>python script_name.py</code></pre>
    </li>
    <li>Enter a keyword (e.g., "restaurants") and select a city from the dropdown.</li>
    <li>Click "Extract Details" to begin the extraction process.</li>
    <li>Once complete, the data will be saved in an Excel file named <b>extracted_data.xlsx</b>.</li>
</ol>

<h2 style="color:#2196F3;">Notes</h2>
<ul>
    <li>Ensure that the Google Maps page loads properly within the script’s sleep time intervals (5 seconds).</li>
    <li>If Google Maps updates its layout, the class names and XPath selectors may need to be adjusted.</li>
    <li>This script uses Chrome as the default browser, but you can modify it to work with other browsers if needed.</li>
</ul>

<p style="text-align:center; color:#555;">
    Enjoy extracting Google Maps data! 🌍📍
</p>
