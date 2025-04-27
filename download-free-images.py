import requests
import os
from urllib.parse import urlparse
import time

# You'll need to sign up for a free Unsplash API key at https://unsplash.com/developers
UNSPLASH_API_KEY = "XqZcFE1rCuseA2vxQzzHxfB7oQXBQ9CXiTX_XVlnp7U"  # API key set
UNSPLASH_API_URL = "https://api.unsplash.com"

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Project image definitions
PROJECT_IMAGES = {
    "projects-banner": {
        "query": "construction site modern",
        "filename": "projects-banner.jpg",
        "description": "Modern construction site with workers and equipment"
    },
    "project1": {
        "query": "modern office building glass facade",
        "filename": "project1.jpg",
        "description": "Modern office complex with glass facade"
    },
    "project2": {
        "query": "luxury modern house",
        "filename": "project2.jpg",
        "description": "Luxury residential home"
    },
    "project3": {
        "query": "modern retail shopping center",
        "filename": "project3.jpg",
        "description": "Modern retail shopping center"
    },
    "project4": {
        "query": "historic building renovation",
        "filename": "project4.jpg",
        "description": "Historic building renovation"
    },
    "project5": {
        "query": "modern apartment complex",
        "filename": "project5.jpg",
        "description": "Multi-family apartment complex"
    },
    "project6": {
        "query": "modern restaurant interior",
        "filename": "project6.jpg",
        "description": "Modern restaurant interior"
    },
    "project7": {
        "query": "modern community center building",
        "filename": "project7.jpg",
        "description": "Community center building"
    },
    "project8": {
        "query": "corporate headquarters building modern",
        "filename": "project8.jpg",
        "description": "Corporate headquarters building"
    },
    "project9": {
        "query": "modern elementary school building",
        "filename": "project9.jpg",
        "description": "Elementary school building"
    }
}

def search_unsplash(query):
    """Search Unsplash for an image matching the query"""
    headers = {
        "Authorization": f"Client-ID {UNSPLASH_API_KEY}"
    }
    
    params = {
        "query": query,
        "orientation": "landscape",
        "per_page": 1
    }
    
    response = requests.get(
        f"{UNSPLASH_API_URL}/search/photos",
        headers=headers,
        params=params
    )
    
    if response.status_code == 200:
        results = response.json()
        if results["results"]:
            return results["results"][0]["urls"]["regular"]
    return None

def download_image(url, filename):
    """Download an image from a URL and save it to the images directory"""
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join('images', filename), 'wb') as f:
            f.write(response.content)
        return True
    return False

def main():
    print("Starting to download project images...")
    
    for project_id, project_info in PROJECT_IMAGES.items():
        print(f"\nProcessing {project_id}...")
        print(f"Searching for: {project_info['description']}")
        
        image_url = search_unsplash(project_info['query'])
        if image_url:
            print(f"Found image, downloading to {project_info['filename']}...")
            if download_image(image_url, project_info['filename']):
                print("Successfully downloaded!")
            else:
                print("Failed to download image")
        else:
            print("No image found")
            
        # Sleep to respect API rate limits
        time.sleep(1)
    
    print("\nImage download process complete!")

if __name__ == "__main__":
    main() 