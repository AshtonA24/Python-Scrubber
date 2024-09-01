import requests
from PIL import Image
from io import BytesIO

# URL of the image
url = "https://media-photos.depop.com/b1/7632291/1853543653_dfff66d7f2ec4092b6f46702c7c6c795/P0.jpg"

# Fetch the image data
response = requests.get(url)
response.raise_for_status()  # Check for request errors

# Load the image into a Pillow Image object
img = Image.open(BytesIO(response.content))

# Display the image
img.show()

# Optionally save the image to a file
img.save("downloaded_image.jpg")
