import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv


load_dotenv() 

# Replace with your Cloudinary credentials
cloudinary.config(
  cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
  api_key=os.getenv("CLOUDINARY_API_KEY"),
  api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

def upload_image_to_cloudinary(local_image_path):
    try:
        result = cloudinary.uploader.upload(local_image_path)
        return result.get("secure_url")
    except Exception as e:
        print("❌ Upload failed:", e)
        return None

