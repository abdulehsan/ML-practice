import os
from dotenv import load_dotenv
import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt


load_dotenv()

api_key = os.getenv('NASA_API_KEY')
nasa_api_url = f"https://api.nasa.gov/planetary/earth/assets?lon=73.084488&lat=33.738045&date=2024-01-01&&dim=0.10&api_key={api_key}"
response = requests.get(nasa_api_url)
data = response.json()


image_url = data['url']
image_response = requests.get(image_url)
img_data = image_response.content
img = Image.open(BytesIO(img_data))

plt.imshow(img)
plt.axis('off')
plt.show()
