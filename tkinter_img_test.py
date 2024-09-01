import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import requests
from io import BytesIO

def load_image_from_url(url, max_size=(400, 300)):
    # Fetch the image data
    response = requests.get(url)
    response.raise_for_status()

    # Load the image into a Pillow Image object
    img = Image.open(BytesIO(response.content))
    
    # Resize the image
    img.thumbnail(max_size)
    return img

def display_image(url):
    # Load the image
    img = load_image_from_url(url)

    # Create a Tkinter window
    root = tk.Tk()
    root.title("Image Viewer")

    # Convert the Pillow Image object to a Tkinter PhotoImage object
    tk_img = ImageTk.PhotoImage(img)

    # Create a label to display the image
    image_label = Label(root, image=tk_img)
    image_label.pack()

    # Create a label with bold text
    text_label = Label(root, text="Cool Pants", font=("Helvetica", 16, "bold"))
    text_label.pack()

    # Run the Tkinter event loop
    root.mainloop()

# URL of the image
url = "https://media-photos.depop.com/b1/7632291/1853543653_dfff66d7f2ec4092b6f46702c7c6c795/P0.jpg"

# Display the image in a Tkinter window
display_image(url)
