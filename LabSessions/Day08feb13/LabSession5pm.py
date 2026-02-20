# pip install beautifulsoup4 requests

from bs4 import BeautifulSoup
import requests

# -------------------------------
# 1️⃣ Parse Small HTML String
# -------------------------------

html_doc = """
<html>
  <head><title>Test Page</title></head>
  <body>
    <h1>Welcome</h1>
    <p>This is a paragraph.</p>
    <a href="https://example.com">Visit Example</a>
  </body>
</html>
"""

soup = BeautifulSoup(html_doc, "html.parser")

print("---- Basic Extraction ----")
print("Title:", soup.title.text)
print("H1:", soup.h1.text)
print("Paragraph:", soup.p.text)

# -------------------------------
# 2️⃣ Find First <a> Tag
# -------------------------------

first_link = soup.find("a")
print("\nFirst <a> Tag:", first_link)
print("Href:", first_link.get("href"))

# -------------------------------
# 3️⃣ Prettify HTML
# -------------------------------

print("\n---- Prettified HTML ----")
print(soup.prettify())

# -------------------------------
# 4️⃣ find() vs find_all()
# -------------------------------

print("\n---- find() vs find_all() ----")

print("Using find():")
print(soup.find("p"))  # First match

print("\nUsing find_all():")
print(soup.find_all("p"))  # List of all matches


# -------------------------------
# 5️⃣ Scrape Product Details
# -------------------------------

product_html = """
<div class="product">
  <h2 class="name">Laptop</h2>
  <span class="price">$1200</span>
  <span class="rating">4.5</span>
  <span class="availability">In Stock</span>
</div>
"""

product_soup = BeautifulSoup(product_html, "html.parser")

print("\n---- Product Details ----")

product_name = product_soup.find("h2", class_="name").text
price = product_soup.find("span", class_="price").text
rating = product_soup.find("span", class_="rating").text
availability = product_soup.find("span", class_="availability").text

print("Product Name:", product_name)
print("Price:", price)
print("Rating:", rating)
print("Availability:", availability)


# -------------------------------
# 6️⃣ Extract All Image URLs
# -------------------------------

print("\n---- Extract Image URLs ----")

image_html = """
<html>
  <body>
    <img src="image1.jpg" />
    <img src="image2.png" />
    <img src="image3.gif" />
  </body>
</html>
"""

image_soup = BeautifulSoup(image_html, "html.parser")

images = image_soup.find_all("img")

for img in images:
    print("Image URL:", img.get("src"))


# -------------------------------
# 7️⃣ Real Website Example (Optional)
# -------------------------------

print("\n---- Real Website Example ----")

try:
    response = requests.get("https://jsonplaceholder.typicode.com/")
    print("Status Code:", response.status_code)
except Exception as e:
    print("Error fetching website:", e)
