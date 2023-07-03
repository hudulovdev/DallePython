import requests
import base64

def create_dalle_image(prompt, api_key):
    # Set up API endpoint and headers
    url = "https://api.openai.com/v1/images"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Send the prompt to the DALL·E API
    response = requests.post(
        url,
        headers=headers,
        json={
            "prompt": prompt
        }
    )
    response_json = response.json()
    image_data = response_json["image"]

    # Decode and save the generated image
    image_bytes = base64.b64decode(image_data)
    with open("dalle_image.jpg", "wb") as file:
        file.write(image_bytes)

# Provide your DALL·E API key and prompt for image generation
api_key = "your_dalle_api_key"
prompt = "A colorful bird with a tree in the background"

create_dalle_image(prompt, api_key)
