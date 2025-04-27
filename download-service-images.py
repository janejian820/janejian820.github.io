import requests
import os
from urllib.parse import urlparse
import time

# Unsplash API configuration
UNSPLASH_API_KEY = "XqZcFE1rCuseA2vxQzzHxfB7oQXBQ9CXiTX_XVlnp7U"
UNSPLASH_API_URL = "https://api.unsplash.com"

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Service image definitions with precise queries matching our actual services
SERVICE_IMAGES = {
    "services-banner": {
        "query": "construction workers building site professional safety equipment",
        "filename": "services-banner.jpg",
        "description": "Construction workers in safety gear actively working on a professional construction site"
    },
    "commercial": {
        "query": "warehouse construction site industrial building office",
        "filename": "service-commercial.jpg",
        "description": "Commercial construction showing office buildings, warehouses, or industrial facilities under construction"
    },
    "residential": {
        "query": "custom luxury home construction smart home technology",
        "filename": "service-residential.jpg",
        "description": "Custom luxury home with modern smart home features being built"
    },
    "renovation": {
        "query": "kitchen bathroom renovation remodel before after",
        "filename": "service-renovation.jpg",
        "description": "Kitchen or bathroom renovation showing quality remodeling work"
    },
    "project-management": {
        "query": "construction site manager supervisor blueprint team",
        "filename": "service-project-management.jpg",
        "description": "Construction project manager reviewing plans with team on site"
    },
    "design": {
        "query": "architect team reviewing building plans construction site",
        "filename": "service-design.jpg",
        "description": "Design team collaborating on construction plans and blueprints"
    },
    "consultation": {
        "query": "construction planning meeting architect client professional",
        "filename": "service-consultation.jpg",
        "description": "Professional consultation meeting with clients reviewing construction plans"
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
        "per_page": 30  # Get more results to find better matches
    }
    
    response = requests.get(
        f"{UNSPLASH_API_URL}/search/photos",
        headers=headers,
        params=params
    )
    
    if response.status_code == 200:
        results = response.json()
        # Try to find the most relevant image from more results
        if results["results"]:
            # Get the first result that has good dimensions and quality
            for photo in results["results"]:
                width = photo["width"]
                height = photo["height"]
                # Ensure good aspect ratio and minimum size
                if width >= 1200 and height >= 800 and width/height >= 1.3:
                    return photo["urls"]["regular"]
            # If no ideal match found, return first result
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
    print("Starting to download service images...")
    
    for service_id, service_info in SERVICE_IMAGES.items():
        print(f"\nProcessing {service_id}...")
        print(f"Searching for: {service_info['description']}")
        
        image_url = search_unsplash(service_info['query'])
        if image_url:
            print(f"Found image, downloading to {service_info['filename']}...")
            if download_image(image_url, service_info['filename']):
                print("Successfully downloaded!")
            else:
                print("Failed to download image")
        else:
            print("No image found")
            
        # Sleep to respect API rate limits
        time.sleep(1)
    
    print("\nService image download process complete!")

if __name__ == "__main__":
    main() 