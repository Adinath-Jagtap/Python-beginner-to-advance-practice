'''
DAY 13: Working with APIs & Requests Library
'''

# =============================================================================
# APIs & REQUESTS INTRODUCTION
# =============================================================================
'''
API (Application Programming Interface): 
- Way for applications to communicate with each other
- Allows you to request data from servers
- Commonly uses HTTP methods: GET, POST, PUT, DELETE

REST API (Representational State Transfer):
- Most common type of API
- Uses standard HTTP methods
- Returns data in JSON or XML format

requests Library:
- Python library for making HTTP requests
- Simple and easy to use
- Handles sessions, cookies, authentication

Why Use APIs?
- Access real-time data (weather, stocks, news)
- Integrate services (payment gateways, social media)
- Automate data collection
- Build applications that use external data
'''

# --- Installing requests ---
# pip install requests

import requests
import json

# Check requests version
print(requests.__version__)


# =============================================================================
# HTTP METHODS
# =============================================================================
'''
Common HTTP Methods:
- GET: Retrieve data from server (read-only)
- POST: Send data to server (create new resource)
- PUT: Update existing resource
- DELETE: Delete resource
- PATCH: Partially update resource

HTTP Status Codes:
- 200: OK (success)
- 201: Created (resource created successfully)
- 400: Bad Request (client error)
- 401: Unauthorized (authentication required)
- 403: Forbidden (no permission)
- 404: Not Found (resource doesn't exist)
- 500: Internal Server Error (server error)
'''


# =============================================================================
# MAKING GET REQUESTS
# =============================================================================
'''
GET Request: Retrieve data from an API
- Most common type of request
- Used to fetch information
- Does not modify server data
'''

# --- Basic GET Request ---
# Using JSONPlaceholder - Free fake API for testing
url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print(response)  # <Response [200]>
print(response.status_code)  # 200
print(response.ok)  # True (status code < 400)

# Get response text (as string)
print(response.text)

# Get response as JSON (Python dictionary)
data = response.json()
print(data)
print(type(data))  # <class 'dict'>

# Access specific data
print(data['title'])
print(data['body'])
print(data['userId'])


# --- GET Request to List Endpoint ---
# Get multiple items
url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
posts = response.json()

print(f"Total posts: {len(posts)}")  # 100

# Loop through first 5 posts
for post in posts[:5]:
    print(f"ID: {post['id']}, Title: {post['title']}")


# --- Response Object Properties ---
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print(response.url)          # URL that was requested
print(response.status_code)  # HTTP status code
print(response.headers)      # Response headers (dictionary-like)
print(response.encoding)     # Response encoding
print(response.elapsed)      # Time taken for request


# =============================================================================
# PARSING JSON RESPONSE
# =============================================================================
'''
JSON (JavaScript Object Notation):
- Standard format for API responses
- Similar to Python dictionaries
- Easy to parse and work with
'''

# --- Simple JSON Response ---
url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url)

user_data = response.json()
print(user_data)

# Access nested data
print(user_data['name'])
print(user_data['email'])
print(user_data['address']['city'])
print(user_data['address']['geo']['lat'])


# --- Nested JSON Parsing ---
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

users = response.json()

# Extract specific fields from all users
for user in users:
    name = user['name']
    email = user['email']
    city = user['address']['city']
    company = user['company']['name']
    print(f"{name} | {email} | {city} | {company}")


# --- Handle Missing Keys Safely ---
# Use .get() method to avoid KeyError
user_data = response.json()[0]

# Safe access with default value
phone = user_data.get('phone', 'N/A')
website = user_data.get('website', 'No website')

# Nested safe access
zipcode = user_data.get('address', {}).get('zipcode', 'Unknown')


# =============================================================================
# ADDING HEADERS TO REQUESTS
# =============================================================================
'''
Headers: Additional information sent with HTTP request
- Content-Type: Format of data being sent
- Authorization: Authentication token
- User-Agent: Information about client making request
- Accept: Format of data client can accept
'''

# --- Basic Headers ---
url = "https://jsonplaceholder.typicode.com/posts"

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)
print(response.status_code)


# --- Authorization Header ---
# Example with API key (not a real key)
url = "https://api.example.com/data"

headers = {
    'Authorization': 'Bearer YOUR_API_KEY_HERE',
    'Content-Type': 'application/json'
}

# response = requests.get(url, headers=headers)


# --- Custom Headers ---
headers = {
    'X-Custom-Header': 'CustomValue',
    'User-Agent': 'MyApp/1.0'
}

# response = requests.get(url, headers=headers)


# =============================================================================
# MAKING POST REQUESTS
# =============================================================================
'''
POST Request: Send data to server
- Creates new resource
- Sends data in request body
- Returns created resource or confirmation
'''

# --- Basic POST Request ---
url = "https://jsonplaceholder.typicode.com/posts"

# Data to send (Python dictionary)
data = {
    'title': 'My New Post',
    'body': 'This is the content of my post',
    'userId': 1
}

response = requests.post(url, json=data)

print(response.status_code)  # 201 (Created)
print(response.json())  # Server response with new resource


# --- POST with Headers ---
url = "https://jsonplaceholder.typicode.com/posts"

headers = {
    'Content-Type': 'application/json'
}

data = {
    'title': 'Another Post',
    'body': 'Post content here',
    'userId': 2
}

response = requests.post(url, json=data, headers=headers)
print(response.json())


# --- POST Form Data ---
# For HTML form submissions
url = "https://httpbin.org/post"

form_data = {
    'username': 'john_doe',
    'password': 'secret123',
    'email': 'john@example.com'
}

response = requests.post(url, data=form_data)  # Note: data, not json
print(response.json())


# --- POST with Files ---
url = "https://httpbin.org/post"

files = {
    'file': open('example.txt', 'rb')  # 'rb' = read binary
}

# response = requests.post(url, files=files)
# Don't forget to close the file or use 'with' statement


# =============================================================================
# HANDLING API ERRORS
# =============================================================================
'''
Error Handling: Gracefully handle API failures
- Network errors
- HTTP errors (4xx, 5xx)
- Invalid JSON responses
- Timeouts
'''

# --- Basic Try-Except ---
url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises HTTPError for bad status codes
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print(f"Error occurred: {e}")


# --- Handling Different Error Types ---
url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=5)  # Timeout after 5 seconds
    response.raise_for_status()
    data = response.json()
    print(data)
    
except requests.exceptions.HTTPError as e:
    # HTTP error (4xx, 5xx)
    print(f"HTTP Error: {e}")
    print(f"Status Code: {response.status_code}")
    
except requests.exceptions.ConnectionError as e:
    # Network problem
    print(f"Connection Error: {e}")
    
except requests.exceptions.Timeout as e:
    # Request timed out
    print(f"Timeout Error: {e}")
    
except requests.exceptions.RequestException as e:
    # Catch-all for any other errors
    print(f"Error: {e}")


# --- Check Status Code Manually ---
url = "https://jsonplaceholder.typicode.com/posts/999999"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Success:", data)
elif response.status_code == 404:
    print("Resource not found")
elif response.status_code == 500:
    print("Server error")
else:
    print(f"Unexpected status code: {response.status_code}")


# --- Validate JSON Response ---
url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url)
    response.raise_for_status()
    
    # Try to parse JSON
    try:
        data = response.json()
        print(data)
    except json.JSONDecodeError:
        print("Invalid JSON response")
        print("Response text:", response.text)
        
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")


# =============================================================================
# EXTRACTING DATA FROM NESTED JSON
# =============================================================================
'''
Nested JSON: JSON objects containing other objects or arrays
- Common in real-world APIs
- Requires careful navigation
- Use .get() for safe access
'''

# --- Simple Nested JSON ---
url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url)

user = response.json()

# Access nested fields
name = user['name']
email = user['email']
city = user['address']['city']
street = user['address']['street']
lat = user['address']['geo']['lat']
lng = user['address']['geo']['lng']
company_name = user['company']['name']

print(f"Name: {name}")
print(f"Email: {email}")
print(f"Location: {street}, {city}")
print(f"Coordinates: ({lat}, {lng})")
print(f"Company: {company_name}")


# --- Extracting from Arrays ---
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

users = response.json()

# Extract all emails
emails = [user['email'] for user in users]
print(emails)

# Extract all cities
cities = [user['address']['city'] for user in users]
print(cities)

# Extract specific fields
user_info = [
    {
        'name': user['name'],
        'email': user['email'],
        'city': user['address']['city']
    }
    for user in users
]
print(user_info)


# --- Deep Nested JSON ---
url = "https://jsonplaceholder.typicode.com/posts/1/comments"
response = requests.get(url)

comments = response.json()

for comment in comments:
    post_id = comment['postId']
    comment_id = comment['id']
    name = comment['name']
    email = comment['email']
    body = comment['body']
    
    print(f"Comment {comment_id} by {email}:")
    print(f"  {body[:50]}...")  # First 50 characters


# --- Safe Navigation with get() ---
# Avoid KeyError for missing keys
user_data = {
    'name': 'John',
    'address': {
        'city': 'New York'
    }
}

# Unsafe - will raise KeyError if key doesn't exist
# zipcode = user_data['address']['zipcode']  # KeyError!

# Safe - returns None if key doesn't exist
zipcode = user_data.get('address', {}).get('zipcode', 'Not provided')
print(zipcode)  # Not provided


# =============================================================================
# MAKING MULTIPLE API CALLS IN LOOP
# =============================================================================
'''
Batch Requests: Make multiple API calls
- Useful for fetching related data
- Be mindful of rate limits
- Consider adding delays between requests
'''

import time

# --- Loop Through IDs ---
base_url = "https://jsonplaceholder.typicode.com/posts/"

# Fetch posts 1 through 5
for post_id in range(1, 6):
    url = f"{base_url}{post_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        post = response.json()
        print(f"Post {post['id']}: {post['title']}")
    else:
        print(f"Failed to fetch post {post_id}")
    
    # Small delay to be respectful to API
    time.sleep(0.5)  # 500ms delay


# --- Collecting Results ---
base_url = "https://jsonplaceholder.typicode.com/users/"

all_users = []

for user_id in range(1, 6):
    url = f"{base_url}{user_id}"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        user = response.json()
        all_users.append(user)
        print(f"Fetched user: {user['name']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user {user_id}: {e}")
    
    time.sleep(0.3)

print(f"\nTotal users fetched: {len(all_users)}")


# --- Fetching Related Data ---
# Get a post and its comments
post_id = 1

# Get post
post_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
post_response = requests.get(post_url)
post = post_response.json()

# Get comments for that post
comments_url = f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments"
comments_response = requests.get(comments_url)
comments = comments_response.json()

print(f"Post: {post['title']}")
print(f"Number of comments: {len(comments)}")

for comment in comments:
    print(f"  - {comment['name']}: {comment['body'][:30]}...")


# --- Parallel Requests (Advanced) ---
# For faster execution, can use threading or async
# Basic example without threading:
urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3"
]

results = []
for url in urls:
    response = requests.get(url)
    results.append(response.json())

print(f"Fetched {len(results)} posts")


# =============================================================================
# SAVING API RESPONSE TO JSON FILE
# =============================================================================
'''
Saving Data: Store API responses for later use
- Reduces API calls
- Enables offline access
- Good for data analysis
'''

import json

# --- Save Single Response ---
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

data = response.json()

# Save to JSON file
with open('post_data.json', 'w') as f:
    json.dump(data, f, indent=4)  # indent=4 for pretty formatting

print("Data saved to post_data.json")


# --- Save Multiple Responses ---
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

posts = response.json()

# Save all posts
with open('all_posts.json', 'w') as f:
    json.dump(posts, f, indent=4)

print(f"Saved {len(posts)} posts to all_posts.json")


# --- Read Back from JSON File ---
# Load data from file
with open('post_data.json', 'r') as f:
    loaded_data = json.load(f)

print("Loaded data:")
print(loaded_data['title'])


# --- Save with Timestamp ---
from datetime import datetime

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

data = {
    'timestamp': datetime.now().isoformat(),
    'users': response.json()
}

with open('users_with_timestamp.json', 'w') as f:
    json.dump(data, f, indent=4)


# --- Append to Existing JSON File ---
# Load existing data
try:
    with open('collected_data.json', 'r') as f:
        existing_data = json.load(f)
except FileNotFoundError:
    existing_data = []

# Fetch new data
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
new_data = response.json()

# Append new data
existing_data.append(new_data)

# Save back to file
with open('collected_data.json', 'w') as f:
    json.dump(existing_data, f, indent=4)


# =============================================================================
# QUERY PARAMETERS
# =============================================================================
'''
Query Parameters: Add filters/options to API requests
- Passed in URL after '?'
- Format: ?key1=value1&key2=value2
- Used for filtering, pagination, sorting
'''

# --- Manual Query String ---
# Filter posts by userId
url = "https://jsonplaceholder.typicode.com/posts?userId=1"
response = requests.get(url)

posts = response.json()
print(f"Posts by user 1: {len(posts)}")


# --- Using params Parameter (Recommended) ---
url = "https://jsonplaceholder.typicode.com/posts"

# Dictionary of parameters
params = {
    'userId': 1
}

response = requests.get(url, params=params)
print(response.url)  # See full URL with parameters
print(f"Total posts: {len(response.json())}")


# --- Multiple Query Parameters ---
url = "https://jsonplaceholder.typicode.com/comments"

params = {
    'postId': 1,
    '_limit': 3  # Limit to 3 results
}

response = requests.get(url, params=params)
comments = response.json()

print(f"Comments for post 1 (limited to 3): {len(comments)}")
for comment in comments:
    print(f"  {comment['name']}")


# --- Pagination ---
url = "https://jsonplaceholder.typicode.com/posts"

# Get page 2, with 10 items per page
params = {
    '_page': 2,
    '_limit': 10
}

response = requests.get(url, params=params)
posts = response.json()

print(f"Page 2 posts: {len(posts)}")


# --- Search/Filter Parameters ---
url = "https://jsonplaceholder.typicode.com/posts"

params = {
    'userId': 1,
    '_sort': 'id',
    '_order': 'desc'  # Descending order
}

response = requests.get(url, params=params)
posts = response.json()

print("Posts by user 1 (sorted by ID desc):")
for post in posts[:3]:
    print(f"  ID {post['id']}: {post['title']}")


# --- Dynamic Parameters ---
def fetch_user_posts(user_id, limit=5):
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {
        'userId': user_id,
        '_limit': limit
    }
    response = requests.get(url, params=params)
    return response.json()

# Use the function
posts = fetch_user_posts(user_id=2, limit=3)
print(f"Fetched {len(posts)} posts for user 2")


# =============================================================================
# API AUTHENTICATION
# =============================================================================
'''
Authentication: Verify identity to access protected APIs
- API Keys: Simple token in header or query
- Bearer Token: Token in Authorization header
- Basic Auth: Username and password
- OAuth: More complex, used by social media APIs
'''

# --- API Key in Query Parameters ---
# Example (not real API)
url = "https://api.example.com/data"

params = {
    'api_key': 'YOUR_API_KEY_HERE'
}

# response = requests.get(url, params=params)


# --- API Key in Headers (More Secure) ---
url = "https://api.example.com/data"

headers = {
    'X-API-Key': 'YOUR_API_KEY_HERE'
}

# response = requests.get(url, headers=headers)


# --- Bearer Token Authentication ---
url = "https://api.example.com/protected"

headers = {
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN_HERE'
}

# response = requests.get(url, headers=headers)


# --- Basic Authentication ---
from requests.auth import HTTPBasicAuth

url = "https://api.example.com/protected"

# Method 1: Using auth parameter
# response = requests.get(url, auth=HTTPBasicAuth('username', 'password'))

# Method 2: Shorthand
# response = requests.get(url, auth=('username', 'password'))


# --- Example with Real API (GitHub) ---
# GitHub API example (works without auth but has rate limits)
url = "https://api.github.com/users/octocat"

# Without authentication
response = requests.get(url)
print(response.json()['name'])

# With authentication (replace with your token)
# headers = {
#     'Authorization': 'token YOUR_GITHUB_TOKEN'
# }
# response = requests.get(url, headers=headers)


# --- Session with Authentication ---
# Maintain authentication across multiple requests
session = requests.Session()
session.headers.update({
    'Authorization': 'Bearer YOUR_TOKEN_HERE'
})

# Now all requests in this session use the token
# response1 = session.get('https://api.example.com/endpoint1')
# response2 = session.get('https://api.example.com/endpoint2')


# =============================================================================
# REAL-WORLD API EXAMPLES
# =============================================================================

# --- Weather API Example (OpenWeatherMap style) ---
# Note: Requires API key from openweathermap.org
"""
url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    'q': 'London',
    'appid': 'YOUR_API_KEY',
    'units': 'metric'
}

response = requests.get(url, params=params)
data = response.json()

print(f"City: {data['name']}")
print(f"Temperature: {data['main']['temp']}°C")
print(f"Weather: {data['weather'][0]['description']}")
"""


# --- REST Countries API (No auth required) ---
url = "https://restcountries.com/v3.1/name/india"

response = requests.get(url)
countries = response.json()

for country in countries:
    print(f"Name: {country['name']['common']}")
    print(f"Capital: {country['capital'][0]}")
    print(f"Population: {country['population']:,}")
    print(f"Region: {country['region']}")


# --- Free Quote API (No auth required) ---
url = "https://api.quotable.io/random"

response = requests.get(url)
quote_data = response.json()

print(f"\"{quote_data['content']}\"")
print(f"- {quote_data['author']}")


# =============================================================================
# BEST PRACTICES
# =============================================================================
'''
🔹 Always handle errors with try-except
🔹 Check status codes before parsing response
🔹 Use timeout parameter to avoid hanging requests
🔹 Add delays between multiple requests (respect rate limits)
🔹 Store API keys in environment variables, not in code
🔹 Use sessions for multiple requests to same API
🔹 Read API documentation for rate limits and authentication
🔹 Validate JSON before accessing nested keys
🔹 Log API requests for debugging
🔹 Cache responses when possible to reduce API calls
'''


# =============================================================================
# KEY TAKEAWAYS - APIs & REQUESTS
# =============================================================================
'''
📌 GET REQUESTS:
- Use requests.get(url) to fetch data
- response.json() converts JSON to Python dict
- response.status_code shows HTTP status (200 = success)
- Most common method for reading data from APIs

📌 JSON PARSING:
- response.json() automatically parses JSON response
- Access nested data with brackets: data['key']['nested_key']
- Use .get() method for safe access: data.get('key', 'default')
- List comprehensions work great for extracting from arrays

📌 HEADERS:
- Pass headers as dictionary: requests.get(url, headers={...})
- Common headers: Authorization, Content-Type, User-Agent
- Headers contain metadata about request/response
- Required for authentication and API requirements

📌 POST REQUESTS:
- Use requests.post(url, json=data) to send data
- json parameter automatically converts dict to JSON
- data parameter for form data
- Returns 201 status code on successful creation

📌 ERROR HANDLING:
- Use try-except to catch request errors
- response.raise_for_status() raises exception for 4xx/5xx codes
- Handle specific errors: HTTPError, ConnectionError, Timeout
- Always add timeout parameter: requests.get(url, timeout=5)
- Check status_code manually for custom error handling

📌 NESTED JSON:
- Use bracket notation for nested access: data['level1']['level2']
- Safe navigation: data.get('key', {}).get('nested', 'default')
- Loop through arrays to extract specific fields
- List comprehensions for extracting data from multiple items

📌 MULTIPLE REQUESTS:
- Use loops to make multiple API calls
- Add time.sleep() to respect rate limits
- Collect results in list for batch processing
- Consider using sessions for better performance
- Handle errors for each request individually

📌 SAVING RESPONSES:
- Use json.dump() to save to file
- json.load() to read back from file
- indent=4 parameter for readable formatting
- Save with timestamps for tracking
- Good for caching and reducing API calls

📌 QUERY PARAMETERS:
- Pass as dictionary: requests.get(url, params={...})
- Used for filtering, pagination, sorting
- Automatically URL-encoded by requests library
- Check response.url to see final URL with parameters
- Common params: page, limit, sort, filter

📌 AUTHENTICATION:
- API Key: In headers or query parameters
- Bearer Token: Authorization header with 'Bearer TOKEN'
- Basic Auth: auth=('username', 'password')
- Store credentials securely (environment variables)
- Use sessions to maintain auth across requests

💡 BEST PRACTICES:
- Always use try-except for error handling
- Set timeout to avoid hanging requests
- Respect API rate limits (add delays)
- Read API documentation thoroughly
- Use environment variables for API keys
- Cache responses when appropriate
- Validate data before accessing nested keys
- Use sessions for multiple requests to same API
- Log requests for debugging
- Check response status before parsing JSON
'''
