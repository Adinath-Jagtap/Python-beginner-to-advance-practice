'''
DAY 14: Web Scraping with BeautifulSoup
'''

# =============================================================================
# WEB SCRAPING INTRODUCTION
# =============================================================================
'''
Web Scraping: Extracting data from websites
- Automated data collection from web pages
- Parses HTML and extracts specific information
- Useful for data analysis, research, monitoring

BeautifulSoup: Python library for parsing HTML and XML
- Easy to use and learn
- Powerful search and navigation methods
- Works with different parsers (html.parser, lxml)

Common Use Cases:
- Price monitoring (e-commerce)
- News aggregation
- Research data collection
- Job listings
- Social media data

Legal & Ethical Considerations:
- Check website's robots.txt file
- Respect website's Terms of Service
- Don't overload servers (add delays)
- Use APIs when available
- Don't scrape personal/copyrighted data
'''

# --- Installing Required Libraries ---
# pip install beautifulsoup4
# pip install requests
# pip install lxml (optional, faster parser)

from bs4 import BeautifulSoup
import requests
import time

# Check versions
print(f"BeautifulSoup version: {BeautifulSoup.__version__ if hasattr(BeautifulSoup, '__version__') else 'Installed'}")


# =============================================================================
# HTML BASICS (Quick Review)
# =============================================================================
'''
HTML Structure:
- Tags: <tag>content</tag>
- Attributes: <tag attribute="value">content</tag>
- Common tags: <div>, <p>, <a>, <h1>, <table>, <img>

HTML Example:
<html>
  <head>
    <title>Page Title</title>
  </head>
  <body>
    <h1 class="heading">Main Heading</h1>
    <p id="intro">This is a paragraph.</p>
    <a href="https://example.com">Link</a>
  </body>
</html>

CSS Selectors:
- Tag: p, div, a
- Class: .classname
- ID: #idname
- Attribute: [attribute=value]
'''


# =============================================================================
# BASIC BEAUTIFULSOUP USAGE
# =============================================================================

# --- Creating BeautifulSoup Object ---
# Sample HTML
html_content = """
<html>
    <head>
        <title>My First Web Page</title>
    </head>
    <body>
        <h1>Welcome to Web Scraping</h1>
        <p class="intro">This is an introduction paragraph.</p>
        <p class="content">This is the main content.</p>
        <a href="https://example.com">Visit Example</a>
    </body>
</html>
"""

# Create BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Pretty print HTML
print(soup.prettify())

# Get type
print(type(soup))  # <class 'bs4.BeautifulSoup'>


# --- Fetching Real Webpage ---
# Using requests to get webpage
url = "https://example.com"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    
    # Create soup from response content
    soup = BeautifulSoup(response.content, 'html.parser')
    # or use response.text for string content
    
except requests.exceptions.RequestException as e:
    print(f"Error fetching page: {e}")


# =============================================================================
# SCRAPING WEBPAGE TITLE
# =============================================================================
'''
Title Tag: <title> tag in <head> section
- Contains webpage title
- Shows in browser tab
- Important for SEO
'''

# --- Extract Title ---
html = """
<html>
    <head>
        <title>Python Web Scraping Tutorial</title>
    </head>
    <body>
        <h1>Welcome</h1>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

# Method 1: Using .title tag
title_tag = soup.title
print(title_tag)  # <title>Python Web Scraping Tutorial</title>
print(type(title_tag))  # <class 'bs4.element.Tag'>

# Method 2: Get title text
title_text = soup.title.string
print(title_text)  # Python Web Scraping Tutorial

# Method 3: Using find()
title = soup.find('title').string
print(title)


# --- Real Website Example ---
url = "https://example.com"

try:
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    if soup.title:
        print(f"Page Title: {soup.title.string}")
    else:
        print("No title found")
        
except Exception as e:
    print(f"Error: {e}")


# =============================================================================
# EXTRACTING ALL LINKS
# =============================================================================
'''
Links: <a> tags with href attribute
- href contains the URL
- Can be relative or absolute URLs
'''

# --- Extract All Links ---
html = """
<html>
    <body>
        <a href="https://example.com">Example</a>
        <a href="https://google.com">Google</a>
        <a href="/about">About Page</a>
        <a href="/contact">Contact</a>
        <a>No Link Here</a>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

# Find all <a> tags
links = soup.find_all('a')

print(f"Total links found: {len(links)}")

for link in links:
    print(link)


# --- Extract href Attributes ---
for link in links:
    href = link.get('href')  # Get href attribute
    text = link.string       # Get link text
    
    if href:  # Check if href exists
        print(f"Text: {text} | URL: {href}")


# --- Alternative Methods ---
# Method 1: Using .attrs dictionary
for link in links:
    if 'href' in link.attrs:
        print(link.attrs['href'])

# Method 2: Using bracket notation
for link in links:
    try:
        print(link['href'])
    except KeyError:
        print("No href attribute")


# --- Filter Links ---
# Only external links (starting with http)
external_links = []
for link in links:
    href = link.get('href')
    if href and href.startswith('http'):
        external_links.append(href)

print("External links:", external_links)

# Only internal links (starting with /)
internal_links = [link.get('href') for link in links 
                  if link.get('href') and link.get('href').startswith('/')]
print("Internal links:", internal_links)


# --- Real Website Example ---
url = "https://example.com"

try:
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    links = soup.find_all('a')
    print(f"\nFound {len(links)} links:")
    
    for i, link in enumerate(links[:10], 1):  # First 10 links
        href = link.get('href', 'No href')
        text = link.get_text(strip=True) or 'No text'
        print(f"{i}. {text[:50]} -> {href}")
        
except Exception as e:
    print(f"Error: {e}")


# =============================================================================
# FINDING PARAGRAPHS AND TEXT
# =============================================================================
'''
Paragraphs: <p> tags containing text content
- Common element for text content
- Can have class, id, or other attributes
'''

# --- Find All Paragraphs ---
html = """
<html>
    <body>
        <p>First paragraph with some text.</p>
        <p class="important">Second paragraph - important.</p>
        <p id="intro">Introduction paragraph.</p>
        <div>
            <p>Nested paragraph inside div.</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

# Find all <p> tags
paragraphs = soup.find_all('p')

print(f"Total paragraphs: {len(paragraphs)}")

for i, para in enumerate(paragraphs, 1):
    print(f"Paragraph {i}: {para.string}")


# --- Extract Text Content ---
# Method 1: .string (works for simple tags)
for para in paragraphs:
    print(para.string)

# Method 2: .get_text() (better for nested content)
for para in paragraphs:
    print(para.get_text())

# Method 3: .get_text(strip=True) - remove extra whitespace
for para in paragraphs:
    text = para.get_text(strip=True)
    print(text)


# --- Get Text with Separator ---
html = """
<p>This is <strong>bold</strong> and <em>italic</em> text.</p>
"""

soup = BeautifulSoup(html, 'html.parser')
para = soup.find('p')

# Get text with default separator
print(para.get_text())  # This is bold and italic text.

# Get text with custom separator
print(para.get_text(separator=' | '))  # This is | bold | and | italic | text.


# --- Get All Text from Page ---
html = """
<html>
    <body>
        <h1>Heading</h1>
        <p>First paragraph.</p>
        <p>Second paragraph.</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

# Get all text from entire page
all_text = soup.get_text(strip=True)
print(all_text)

# Get text with line breaks
all_text = soup.get_text(separator='\n', strip=True)
print(all_text)


# --- Filter Paragraphs by Length ---
paragraphs = soup.find_all('p')

# Only paragraphs with more than 20 characters
long_paragraphs = [p.get_text(strip=True) for p in paragraphs 
                   if len(p.get_text(strip=True)) > 20]
print(long_paragraphs)


# =============================================================================
# SCRAPING HTML TABLES
# =============================================================================
'''
Tables: <table> tag with <tr> (rows) and <td> (cells)
- <thead>: Table header
- <tbody>: Table body
- <th>: Header cells
- <td>: Data cells
'''

# --- Basic Table Structure ---
html = """
<html>
    <body>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Age</th>
                    <th>City</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>John</td>
                    <td>25</td>
                    <td>New York</td>
                </tr>
                <tr>
                    <td>Alice</td>
                    <td>30</td>
                    <td>London</td>
                </tr>
                <tr>
                    <td>Bob</td>
                    <td>35</td>
                    <td>Paris</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

# Find the table
table = soup.find('table')


# --- Extract Table Headers ---
headers = []
for th in table.find_all('th'):
    headers.append(th.get_text(strip=True))

print("Headers:", headers)


# --- Extract Table Rows ---
rows = table.find_all('tr')

print(f"\nTotal rows (including header): {len(rows)}")

# Skip header row, get data rows
for row in rows[1:]:  # Skip first row (header)
    cells = row.find_all('td')
    row_data = [cell.get_text(strip=True) for cell in cells]
    print(row_data)


# --- Convert Table to List of Dictionaries ---
table_data = []

# Get headers
headers = [th.get_text(strip=True) for th in table.find_all('th')]

# Get rows
rows = table.find('tbody').find_all('tr')

for row in rows:
    cells = row.find_all('td')
    row_data = [cell.get_text(strip=True) for cell in cells]
    
    # Create dictionary with headers as keys
    row_dict = dict(zip(headers, row_data))
    table_data.append(row_dict)

print("\nTable as list of dictionaries:")
for item in table_data:
    print(item)


# --- Convert to Pandas DataFrame (Optional) ---
import pandas as pd

df = pd.DataFrame(table_data)
print("\nTable as DataFrame:")
print(df)


# --- Handle Tables Without Headers ---
html_no_header = """
<table>
    <tr>
        <td>John</td>
        <td>25</td>
    </tr>
    <tr>
        <td>Alice</td>
        <td>30</td>
    </tr>
</table>
"""

soup = BeautifulSoup(html_no_header, 'html.parser')
table = soup.find('table')

for row in table.find_all('tr'):
    cells = row.find_all('td')
    data = [cell.get_text(strip=True) for cell in cells]
    print(data)


# =============================================================================
# CSS SELECTORS
# =============================================================================
'''
CSS Selectors: Powerful way to find elements
- More flexible than find() methods
- Similar to CSS styling selectors
- Use .select() or .select_one() methods
'''

html = """
<html>
    <body>
        <div class="container">
            <h1 id="main-title">Main Title</h1>
            <p class="intro">Introduction paragraph.</p>
            <p class="content">Content paragraph 1.</p>
            <p class="content">Content paragraph 2.</p>
            <div class="section">
                <h2>Section Title</h2>
                <a href="https://example.com" class="link">Example Link</a>
            </div>
        </div>
        <footer id="page-footer">
            <p>Footer text</p>
        </footer>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')


# --- Select by Tag ---
# Find all <p> tags
paragraphs = soup.select('p')
print(f"Found {len(paragraphs)} paragraphs")


# --- Select by Class ---
# Find elements with class="content"
content_paras = soup.select('.content')
for para in content_paras:
    print(para.get_text(strip=True))


# --- Select by ID ---
# Find element with id="main-title"
title = soup.select_one('#main-title')
print(title.get_text(strip=True))


# --- Select by Attribute ---
# Find links with specific href
links = soup.select('a[href="https://example.com"]')
print(links)


# --- Descendant Selector ---
# Find <p> inside <div class="container">
paras_in_container = soup.select('div.container p')
print(f"Paragraphs in container: {len(paras_in_container)}")


# --- Child Selector ---
# Direct children only (>)
direct_children = soup.select('div.container > p')
print(f"Direct child paragraphs: {len(direct_children)}")


# --- Multiple Selectors ---
# Find all h1 and h2 tags
headings = soup.select('h1, h2')
for heading in headings:
    print(heading.get_text(strip=True))


# --- Attribute Selectors ---
# Elements with any href attribute
all_links = soup.select('[href]')

# Links starting with https
https_links = soup.select('a[href^="https"]')

# Links containing "example"
example_links = soup.select('a[href*="example"]')

# Links ending with .com
com_links = soup.select('a[href$=".com"]')


# --- Combining Selectors ---
# <p> tags with class "content" inside div
complex_select = soup.select('div p.content')


# --- nth-child Selector ---
html_list = """
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
    <li>Item 4</li>
</ul>
"""

soup = BeautifulSoup(html_list, 'html.parser')

# First li
first_item = soup.select('li:nth-child(1)')

# Last li
last_item = soup.select('li:last-child')

# Even items
even_items = soup.select('li:nth-child(even)')


# =============================================================================
# FINDING ELEMENTS BY CLASS NAME
# =============================================================================
'''
Class Names: Multiple elements can share same class
- Used for styling and grouping elements
- Elements can have multiple classes
- Use find_all() or select() to find by class
'''

html = """
<html>
    <body>
        <div class="product">
            <h2 class="product-title">Product 1</h2>
            <p class="product-price">$99.99</p>
            <p class="product-description">Great product!</p>
        </div>
        <div class="product featured">
            <h2 class="product-title">Product 2</h2>
            <p class="product-price">$149.99</p>
            <p class="product-description">Amazing product!</p>
        </div>
        <div class="product">
            <h2 class="product-title">Product 3</h2>
            <p class="product-price">$79.99</p>
            <p class="product-description">Good product!</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')


# --- Method 1: find_all() with class_ ---
# Note: class_ with underscore (class is Python keyword)
products = soup.find_all('div', class_='product')
print(f"Found {len(products)} products")


# --- Method 2: CSS Selector ---
products = soup.select('.product')
print(f"Found {len(products)} products")


# --- Extract Data from Each Product ---
products = soup.find_all('div', class_='product')

for i, product in enumerate(products, 1):
    title = product.find('h2', class_='product-title').get_text(strip=True)
    price = product.find('p', class_='product-price').get_text(strip=True)
    description = product.find('p', class_='product-description').get_text(strip=True)
    
    print(f"\nProduct {i}:")
    print(f"  Title: {title}")
    print(f"  Price: {price}")
    print(f"  Description: {description}")


# --- Find Element with Multiple Classes ---
# Element with both "product" and "featured"
featured = soup.find('div', class_='product featured')
print("\nFeatured product:", featured.find('h2').get_text(strip=True))


# --- Find Elements with Partial Class Match ---
# Elements with class containing "product"
elements = soup.find_all(class_=lambda x: x and 'product' in x)
print(f"\nElements with 'product' in class: {len(elements)}")


# =============================================================================
# SCRAPING IMAGE URLs
# =============================================================================
'''
Images: <img> tag with src attribute
- src: Image URL (required)
- alt: Alternative text
- Can be relative or absolute URLs
'''

html = """
<html>
    <body>
        <img src="https://example.com/image1.jpg" alt="Image 1">
        <img src="/images/image2.png" alt="Image 2">
        <img src="https://example.com/image3.gif" alt="Image 3">
        <div class="gallery">
            <img src="https://example.com/gallery1.jpg" alt="Gallery 1">
            <img src="https://example.com/gallery2.jpg" alt="Gallery 2">
        </div>
        <img>  <!-- No src attribute -->
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')


# --- Find All Images ---
images = soup.find_all('img')
print(f"Found {len(images)} images")


# --- Extract Image URLs ---
for img in images:
    src = img.get('src')
    alt = img.get('alt', 'No alt text')
    
    if src:  # Check if src exists
        print(f"Image: {alt} | URL: {src}")


# --- Get Only Absolute URLs ---
absolute_urls = []

for img in images:
    src = img.get('src')
    if src and src.startswith('http'):
        absolute_urls.append(src)

print("\nAbsolute image URLs:")
for url in absolute_urls:
    print(url)


# --- Using CSS Selectors ---
# All images
all_images = soup.select('img')

# Images with src attribute
images_with_src = soup.select('img[src]')

# Images inside specific div
gallery_images = soup.select('div.gallery img')

print(f"\nGallery images: {len(gallery_images)}")
for img in gallery_images:
    print(img['src'])


# --- Extract Image Data as Dictionary ---
image_data = []

for img in soup.find_all('img'):
    if img.get('src'):
        image_info = {
            'src': img.get('src'),
            'alt': img.get('alt', ''),
            'title': img.get('title', '')
        }
        image_data.append(image_info)

print("\nImage data:")
for img in image_data:
    print(img)


# --- Convert Relative URLs to Absolute ---
from urllib.parse import urljoin

base_url = "https://example.com"

for img in soup.find_all('img'):
    src = img.get('src')
    if src:
        absolute_url = urljoin(base_url, src)
        print(f"Relative: {src} -> Absolute: {absolute_url}")


# =============================================================================
# HANDLING REQUESTS ERRORS
# =============================================================================
'''
Error Handling: Important for robust web scraping
- Network errors (no internet, timeout)
- HTTP errors (404, 500, etc.)
- Parsing errors (invalid HTML)
- Missing elements
'''

# --- Complete Error Handling Example ---
url = "https://example.com"

try:
    # Make request with timeout
    response = requests.get(url, timeout=10)
    
    # Check for HTTP errors
    response.raise_for_status()
    
    # Parse HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract data with error handling
    title = soup.find('title')
    if title:
        print(f"Title: {title.string}")
    else:
        print("No title found")
    
    # Extract links safely
    links = soup.find_all('a')
    print(f"Found {len(links)} links")
    
except requests.exceptions.Timeout:
    print("Error: Request timed out")
    
except requests.exceptions.ConnectionError:
    print("Error: Could not connect to server")
    
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
    print(f"Status Code: {response.status_code}")
    
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    
except Exception as e:
    print(f"Unexpected error: {e}")


# --- Safe Element Extraction ---
url = "https://example.com"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Safe extraction with checks
    title_tag = soup.find('title')
    title = title_tag.string if title_tag else "No title"
    
    # Using .select_one() which returns None if not found
    main_heading = soup.select_one('h1')
    heading_text = main_heading.get_text(strip=True) if main_heading else "No heading"
    
    print(f"Title: {title}")
    print(f"Heading: {heading_text}")
    
except Exception as e:
    print(f"Error: {e}")


# --- Retry Logic ---
def fetch_with_retry(url, max_retries=3, delay=2):
    """Fetch URL with retry logic"""
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print("Max retries reached")
                raise

# Usage
try:
    soup = fetch_with_retry("https://example.com")
    print("Success!")
except Exception as e:
    print(f"Failed after retries: {e}")


# --- Check if Element Exists Before Accessing ---
soup = BeautifulSoup("<html><body></body></html>", 'html.parser')

# Bad - will raise AttributeError
# title = soup.find('title').string  # Error!

# Good - check first
title_tag = soup.find('title')
if title_tag:
    title = title_tag.string
else:
    title = "No title"

# Alternative - using try-except
try:
    title = soup.find('title').string
except AttributeError:
    title = "No title"


# =============================================================================
# EXTRACTING SPECIFIC DIV CONTENT
# =============================================================================
'''
Div Elements: <div> containers for grouping content
- Often have class or id for identification
- Can contain nested elements
- Common in modern web layouts
'''

html = """
<html>
    <body>
        <div id="header">
            <h1>Website Header</h1>
            <nav>Navigation</nav>
        </div>
        
        <div class="main-content">
            <div class="article" id="article-1">
                <h2>Article 1 Title</h2>
                <p class="author">By John Doe</p>
                <p class="text">Article 1 content goes here.</p>
                <span class="date">2024-01-15</span>
            </div>
            
            <div class="article" id="article-2">
                <h2>Article 2 Title</h2>
                <p class="author">By Jane Smith</p>
                <p class="text">Article 2 content goes here.</p>
                <span class="date">2024-01-16</span>
            </div>
        </div>
        
        <div id="sidebar">
            <div class="widget">
                <h3>Widget 1</h3>
                <p>Widget content</p>
            </div>
        </div>
        
        <div id="footer">
            <p>Copyright 2024</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')


# --- Find Div by ID ---
header = soup.find('div', id='header')
print("Header:", header.get_text(strip=True))

# Using select_one with ID
footer = soup.select_one('#footer')
print("Footer:", footer.get_text(strip=True))


# --- Find Div by Class ---
main_content = soup.find('div', class_='main-content')
print("\nMain content div found:", main_content is not None)


# --- Find Multiple Divs with Same Class ---
articles = soup.find_all('div', class_='article')
print(f"\nFound {len(articles)} articles")

for article in articles:
    title = article.find('h2').get_text(strip=True)
    author = article.find('p', class_='author').get_text(strip=True)
    text = article.find('p', class_='text').get_text(strip=True)
    date = article.find('span', class_='date').get_text(strip=True)
    
    print(f"\nTitle: {title}")
    print(f"Author: {author}")
    print(f"Date: {date}")
    print(f"Content: {text}")


# --- Extract All Content from Specific Div ---
main_content = soup.find('div', class_='main-content')

# Get all text
all_text = main_content.get_text(strip=True, separator='\n')
print("\nAll content from main-content div:")
print(all_text)


# --- Find Nested Divs ---
# Find widgets inside sidebar
sidebar = soup.find('div', id='sidebar')
widgets = sidebar.find_all('div', class_='widget')

print(f"\nFound {len(widgets)} widgets in sidebar")
for widget in widgets:
    widget_title = widget.find('h3').get_text(strip=True)
    print(f"Widget: {widget_title}")


# --- Using CSS Selectors for Divs ---
# All divs with class "article"
articles = soup.select('div.article')

# Div with specific ID
header = soup.select_one('div#header')

# Divs inside main-content
nested_divs = soup.select('div.main-content div')

# Direct child divs only
direct_children = soup.select('div.main-content > div')


# --- Extract Attributes from Div ---
articles = soup.find_all('div', class_='article')

for article in articles:
    article_id = article.get('id')
    article_class = article.get('class')
    
    print(f"\nArticle ID: {article_id}")
    print(f"Article Classes: {article_class}")


# =============================================================================
# SCRAPING MULTIPLE PAGES IN LOOP
# =============================================================================
'''
Multi-Page Scraping: Scrape data from multiple pages
- Pagination (page=1, page=2, etc.)
- Sequential URLs (article/1, article/2, etc.)
- List of URLs to scrape
- Always add delays to respect servers
'''

# --- Scraping Sequential Pages ---
base_url = "https://jsonplaceholder.typicode.com/posts/"

all_posts = []

for post_id in range(1, 6):  # Scrape posts 1 through 5
    url = f"{base_url}{post_id}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # For JSON API
        post = response.json()
        all_posts.append(post)
        
        print(f"Scraped post {post_id}: {post['title'][:50]}...")
        
        # Add delay between requests
        time.sleep(1)  # 1 second delay
        
    except Exception as e:
        print(f"Error scraping post {post_id}: {e}")
        continue

print(f"\nTotal posts scraped: {len(all_posts)}")


# --- Scraping with Pagination ---
# Example: Scraping multiple pages with page parameter
def scrape_paginated_site(base_url, total_pages):
    """Scrape multiple pages from paginated website"""
    all_data = []
    
    for page_num in range(1, total_pages + 1):
        url = f"{base_url}?page={page_num}"
        
        try:
            print(f"Scraping page {page_num}...")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract data from page (customize based on site)
            items = soup.find_all('div', class_='item')
            
            for item in items:
                # Extract relevant data
                data = {
                    'title': item.find('h2').get_text(strip=True) if item.find('h2') else None,
                    'description': item.find('p').get_text(strip=True) if item.find('p') else None
                }
                all_data.append(data)
            
            print(f"  Found {len(items)} items on page {page_num}")
            
            # Respectful delay
            time.sleep(2)
            
        except Exception as e:
            print(f"Error on page {page_num}: {e}")
            continue
    
    return all_data

# Usage
# data = scrape_paginated_site("https://example.com/items", total_pages=5)


# --- Scraping List of URLs ---
urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
]

results = []

for i, url in enumerate(urls, 1):
    print(f"\nScraping {i}/{len(urls)}: {url}")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract data
        title = soup.find('title')
        title_text = title.string if title else "No title"
        
        results.append({
            'url': url,
            'title': title_text,
            'status': 'success'
        })
        
        print(f"  Title: {title_text}")
        
        # Delay between requests
        time.sleep(1)
        
    except Exception as e:
        print(f"  Error: {e}")
        results.append({
            'url': url,
            'title': None,
            'status': 'failed'
        })

# Summary
successful = sum(1 for r in results if r['status'] == 'success')
print(f"\n\nSummary: {successful}/{len(urls)} pages scraped successfully")


# --- Following Next Page Links ---
def scrape_with_next_link(start_url, max_pages=10):
    """Scrape pages by following 'next' links"""
    current_url = start_url
    page_count = 0
    all_data = []
    
    while current_url and page_count < max_pages:
        page_count += 1
        print(f"Scraping page {page_count}: {current_url}")
        
        try:
            response = requests.get(current_url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract data from current page
            items = soup.find_all('div', class_='item')
            all_data.extend(items)
            
            # Find next page link
            next_link = soup.find('a', class_='next')
            current_url = next_link['href'] if next_link else None
            
            time.sleep(2)
            
        except Exception as e:
            print(f"Error: {e}")
            break
    
    return all_data


# --- Save Scraped Data to File ---
import json

# Example: Save multiple pages data
all_data = []

for page in range(1, 4):
    url = f"https://jsonplaceholder.typicode.com/posts?_page={page}&_limit=5"
    
    try:
        response = requests.get(url, timeout=10)
        posts = response.json()
        all_data.extend(posts)
        time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")

# Save to JSON file
with open('scraped_data.json', 'w') as f:
    json.dump(all_data, f, indent=4)

print(f"Saved {len(all_data)} items to scraped_data.json")


# --- Progress Tracking ---
from tqdm import tqdm  # pip install tqdm

urls_to_scrape = [f"https://example.com/page{i}" for i in range(1, 11)]

results = []

for url in tqdm(urls_to_scrape, desc="Scraping pages"):
    try:
        response = requests.get(url, timeout=10)
        # Process response...
        time.sleep(1)
    except Exception as e:
        continue


# =============================================================================
# BEST PRACTICES FOR WEB SCRAPING
# =============================================================================
'''
🔹 Legal & Ethical:
   - Check robots.txt (example.com/robots.txt)
   - Read Terms of Service
   - Use APIs when available
   - Don't scrape personal data without permission

🔹 Technical:
   - Add delays between requests (time.sleep())
   - Use headers to identify your bot
   - Handle errors gracefully
   - Respect rate limits
   - Cache data to reduce requests

🔹 Code Quality:
   - Always use try-except for requests
   - Check if elements exist before accessing
   - Use meaningful variable names
   - Log your scraping activities
   - Validate scraped data

🔹 Performance:
   - Don't scrape more than needed
   - Use sessions for multiple requests
   - Consider using async for many requests
   - Store data incrementally (don't lose everything if crash)

🔹 Maintenance:
   - Websites change - your scraper will break
   - Make code modular and easy to update
   - Add tests for key functionality
   - Document your scraping logic
'''


# --- Good Scraping Template ---
def scrape_website(url, delay=2):
    """
    Template for scraping with best practices
    
    Args:
        url (str): URL to scrape
        delay (int): Delay between requests in seconds
    
    Returns:
        dict: Scraped data or None if failed
    """
    
    # Set custom headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Educational Bot) Python/3.x',
        'Accept': 'text/html,application/xhtml+xml',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    
    try:
        # Make request with timeout
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract data safely
        data = {
            'url': url,
            'title': soup.find('title').string if soup.find('title') else None,
            'scraped_at': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Add delay for next request
        time.sleep(delay)
        
        return data
        
    except requests.exceptions.Timeout:
        print(f"Timeout error for {url}")
        return None
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error {e.response.status_code} for {url}")
        return None
        
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None


# =============================================================================
# KEY TAKEAWAYS - WEB SCRAPING & BEAUTIFULSOUP
# =============================================================================
'''
📌 BEAUTIFULSOUP BASICS:
- Create soup: soup = BeautifulSoup(html_content, 'html.parser')
- Always use html.parser or lxml as parser
- soup.prettify() formats HTML for reading
- Works with requests library to fetch web pages

📌 WEBPAGE TITLE:
- Access with soup.title or soup.find('title')
- Get text with .string or .get_text()
- Always check if title exists before accessing

📌 EXTRACTING LINKS:
- Find all links: soup.find_all('a')
- Get URL: link.get('href') or link['href']
- Check if href exists before accessing
- Filter external (http) vs internal (/) links

📌 PARAGRAPHS & TEXT:
- Find all: soup.find_all('p')
- Get text: .get_text() or .string
- strip=True removes whitespace
- Use separator parameter for formatting

📌 HTML TABLES:
- Find table: soup.find('table')
- Headers in <th>, data in <td>
- Loop through rows: table.find_all('tr')
- Convert to list of dicts for easy processing

📌 CSS SELECTORS:
- More powerful than find(): soup.select('selector')
- Tag: 'p', Class: '.classname', ID: '#idname'
- Descendant: 'div p', Child: 'div > p'
- Attribute: 'a[href^="https"]'
- Multiple: 'h1, h2, h3'

📌 FIND BY CLASS:
- Use class_ (underscore): find_all('div', class_='name')
- Or CSS: soup.select('.classname')
- Elements can have multiple classes
- Use lambda for partial matches

📌 IMAGE URLs:
- Find images: soup.find_all('img')
- Get URL: img.get('src') or img['src']
- Check alt text: img.get('alt')
- Convert relative to absolute with urljoin()

📌 ERROR HANDLING:
- Always use try-except with requests
- Handle: Timeout, ConnectionError, HTTPError
- Check if elements exist before accessing
- Use .get() for safe attribute access
- Add retry logic for important scraping

📌 SPECIFIC DIV CONTENT:
- By ID: soup.find('div', id='name')
- By class: soup.find('div', class_='name')
- Multiple: soup.find_all('div', class_='name')
- Extract nested content carefully

📌 MULTIPLE PAGES:
- Use loops with range() for sequential pages
- Add time.sleep() between requests (1-3 seconds)
- Track progress and errors
- Save data incrementally
- Follow pagination links dynamically

💡 BEST PRACTICES:
- Check robots.txt before scraping
- Add User-Agent header to identify your bot
- Always add delays (time.sleep) between requests
- Handle all errors gracefully
- Validate data after extraction
- Use sessions for multiple requests
- Cache data to avoid re-scraping
- Respect website's Terms of Service
- Prefer APIs over scraping when available
- Make code modular and maintainable
'''


# =============================================================================
# PYTHON PRACTICE QUESTIONS - WEB SCRAPING (BeautifulSoup)
# =============================================================================
'''
1. Scrape the webpage title using BeautifulSoup
2. Extract all hyperlinks (<a> tags) from a webpage
3. Find all paragraph (<p>) elements and print their text
4. Scrape structured data from an HTML table
5. Extract data using CSS selectors with select() / select_one()
6. Find elements by class name using find_all()
7. Scrape image URLs (<img> src attributes) from a webpage
8. Handle HTTP and request errors gracefully using try-except
9. Extract specific content from a <div> based on id or class
10. Scrape multiple pages in a loop (pagination handling)
'''