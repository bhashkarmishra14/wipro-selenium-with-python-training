# 1) Parse HTML – Extract title and h1
#
# from bs4 import BeautifulSoup
#
# html = '''
# <html>
# <head><title>My Page</title></head>
# <body>
# <h1>Welcome</h1>
# <p>This is a paragraph.</p>
# </body>
# </html>
# '''
# 2) Extract All Paragraphs
# 3) Extract All Links and Count
# 4) Extract Attributes
# 5) Extract First h2
# 6) Extract Bold Text
# 7) Extract All href Values
# 8) Get All Text Without Tags
# 9) Extract Title from Website
# 10) Extract All Headings
# 11) Extract Table Data
# 12) Extract Images
#

from bs4 import BeautifulSoup
import requests

html = """
<html>
<head><title>My Page</title></head>
<body>
<h1>Welcome</h1>
<h2>I am Bhashkar</h2>

<p>This is My paragraph.</p>
<p>I am very smart.</p>

<a href="https://google.com">Google</a>
<a href="https://github.com">GitHub</a>

<b>Bold Text Example</b>

<img src="image1.jpg" alt="Image1">
<img src="image2.png" alt="Image2">

<table>
<tr><th>Name</th><th>Age</th></tr>
<tr><td>John</td><td>25</td></tr>
<tr><td>Mary</td><td>30</td></tr>
</table>

</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

print("Title:", soup.title.text)
print("H1:", soup.find("h1").text)

print("\nParagraphs:")
for p in soup.find_all("p"):
    print(p.text)

links = soup.find_all("a")
print("\nTotal Links:", len(links))

print("\nFirst Link Attributes:", links[0].attrs)

h2 = soup.find("h2")
print("\nFirst H2:", h2.text if h2 else "Not found")

bold = soup.find("b")
print("\nBold Text:", bold.text if bold else "Not found")

print("\nAll Href Values:")
for link in links:
    print(link.get("href"))

print("\nAll Text:")
print(soup.get_text())

try:
    response = requests.get("https://www.python.org")
    website_soup = BeautifulSoup(response.text, "html.parser")
    print("\nWebsite Title:", website_soup.title.text)
except:
    print("\nCould not fetch website title")

print("\nAll Headings:")
for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
    print(heading.text)

print("\nTable Data:")
for row in soup.find_all("tr"):
    cols = row.find_all(["th", "td"])
    print([col.text for col in cols])

print("\nImages:")
for img in soup.find_all("img"):
    print("Source:", img.get("src"), "Alt:", img.get("alt"))
