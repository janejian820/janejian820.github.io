import os
import requests
import json
from urllib.parse import quote_plus
import time

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# List of images needed for the website
images_list = [
    {
        "filename": "logo.png",
        "description": "Construction logo blue and orange modern",
        "search_term": "construction logo blue orange"
    },
    {
        "filename": "logo-white.png",
        "description": "White version of company logo for footer",
        "search_term": "construction logo white"
    },
    {
        "filename": "favicon.ico",
        "description": "Website favicon",
        "search_term": "construction icon"
    },
    {
        "filename": "hero-bg.jpg",
        "description": "Hero section background - Construction workers or construction site with modern building",
        "search_term": "modern construction site building workers skyline"
    },
    {
        "filename": "about-img.jpg",
        "description": "About section image - Team of construction professionals or company office",
        "search_term": "construction team professionals office"
    },
    {
        "filename": "counter-bg.jpg",
        "description": "Counter section background - Dark-tinted construction or architecture image",
        "search_term": "dark construction architecture modern"
    },
    {
        "filename": "services-banner.jpg",
        "description": "Services page banner - Wide construction site or building image",
        "search_term": "wide construction site modern building panorama"
    },
    {
        "filename": "projects-banner.jpg",
        "description": "Projects page banner - Wide construction site or completed building",
        "search_term": "completed modern building construction panorama"
    },
    {
        "filename": "cta-bg.jpg",
        "description": "Call-to-action background - Construction site or blueprint image",
        "search_term": "construction blueprint architect desk plans"
    },
    
    # Service Images
    {
        "filename": "service-commercial.jpg",
        "description": "Commercial construction service - Commercial building or office space",
        "search_term": "commercial building office tower modern glass"
    },
    {
        "filename": "service-residential.jpg",
        "description": "Residential construction service - Modern home or residential building",
        "search_term": "modern luxury home residential"
    },
    {
        "filename": "service-renovation.jpg",
        "description": "Renovation service - Home renovation or remodeling",
        "search_term": "home renovation remodeling interior"
    },
    {
        "filename": "service-project-management.jpg",
        "description": "Project management service - Construction manager with plans or team meeting",
        "search_term": "construction manager team meeting plans"
    },
    {
        "filename": "service-design.jpg",
        "description": "Design-build service - Architectural plans or design discussion",
        "search_term": "architect design discussion blueprint plans"
    },
    {
        "filename": "service-consultation.jpg",
        "description": "Consultation service - Client meeting or discussion of plans",
        "search_term": "client meeting architect discussion plans"
    },
    
    # Detailed Service Images
    {
        "filename": "commercial-construction.jpg",
        "description": "Commercial construction detail - Office building or commercial space",
        "search_term": "commercial building construction site"
    },
    {
        "filename": "residential-construction.jpg",
        "description": "Residential construction detail - Luxury home or residential property",
        "search_term": "luxury home construction residential property"
    },
    {
        "filename": "renovations.jpg",
        "description": "Renovations detail - Before/after renovation or remodeling work",
        "search_term": "home renovation remodeling work"
    },
    {
        "filename": "project-management.jpg",
        "description": "Project management detail - Construction manager on site",
        "search_term": "construction manager site supervisor"
    },
    {
        "filename": "design-build.jpg",
        "description": "Design-build detail - Architectural design process or blueprints",
        "search_term": "architectural design process blueprints"
    },
    {
        "filename": "consultation.jpg",
        "description": "Consultation detail - Meeting with clients or discussing plans",
        "search_term": "architect client meeting discussing plans"
    },
    
    # Project Images
    {
        "filename": "project1.jpg",
        "description": "Project 1 - Modern office building exterior",
        "search_term": "modern office building exterior glass"
    },
    {
        "filename": "project2.jpg",
        "description": "Project 2 - Luxury residential home",
        "search_term": "luxury residential home modern architecture"
    },
    {
        "filename": "project3.jpg",
        "description": "Project 3 - Retail shopping center",
        "search_term": "retail shopping center mall modern"
    },
    {
        "filename": "project4.jpg",
        "description": "Project 4 - Historic building renovation",
        "search_term": "historic building renovation restored"
    },
    {
        "filename": "project5.jpg",
        "description": "Project 5 - Multi-family apartment complex",
        "search_term": "multi family apartment complex modern"
    },
    {
        "filename": "project6.jpg",
        "description": "Project 6 - Restaurant renovation",
        "search_term": "restaurant renovation modern interior"
    },
    {
        "filename": "project7.jpg",
        "description": "Project 7 - Community center",
        "search_term": "community center modern building"
    },
    {
        "filename": "project8.jpg",
        "description": "Project 8 - Corporate headquarters",
        "search_term": "corporate headquarters modern building"
    },
    {
        "filename": "project9.jpg",
        "description": "Project 9 - School building",
        "search_term": "modern school building architecture"
    },
    
    # Project Detail Images for Project 1
    {
        "filename": "project1-1.jpg",
        "description": "Project 1 Detail 1 - Office building exterior angle",
        "search_term": "office building exterior angle modern"
    },
    {
        "filename": "project1-2.jpg",
        "description": "Project 1 Detail 2 - Office building interior lobby",
        "search_term": "office building interior lobby modern"
    },
    {
        "filename": "project1-3.jpg",
        "description": "Project 1 Detail 3 - Office building conference room",
        "search_term": "office conference room modern design"
    },
    {
        "filename": "project1-4.jpg",
        "description": "Project 1 Detail 4 - Office building workspace area",
        "search_term": "office workspace area modern design"
    }
]

def download_image(url, filename):
    """Download an image from a URL and save it to the specified filename."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        return True
    return False

def search_unsplash(query, filename):
    """Search Unsplash for an image matching the query and download it."""
    # Replace with your actual Unsplash API access key
    # Sign up at https://unsplash.com/developers to get an access key
    access_key = "YOUR_UNSPLASH_ACCESS_KEY"
    
    # For demo purposes, we'll use the demo API key, but this has very limited usage
    access_key = "demo"
    
    encoded_query = quote_plus(query)
    url = f"https://api.unsplash.com/search/photos?query={encoded_query}&per_page=1"
    
    headers = {
        "Authorization": f"Client-ID {access_key}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            image_url = data["results"][0]["urls"]["regular"]
            if download_image(image_url, os.path.join("images", filename)):
                print(f"Downloaded {filename}")
                return True
    
    print(f"Failed to download {filename}")
    return False

def download_images_from_unsplash():
    """Download all required images from Unsplash."""
    print("Starting to download images...")
    
    success_count = 0
    
    for image in images_list:
        print(f"Searching for: {image['description']}")
        
        if search_unsplash(image["search_term"], image["filename"]):
            success_count += 1
        
        # Avoid rate limiting
        time.sleep(1)
    
    print(f"\nDownloaded {success_count} out of {len(images_list)} images.")
    print("\nNOTE: This script uses the demo API key for Unsplash which has very limited usage.")
    print("To download all images properly, sign up for a free Unsplash developer account at:")
    print("https://unsplash.com/developers")
    print("Then replace 'YOUR_UNSPLASH_ACCESS_KEY' in the script with your actual access key.")

if __name__ == "__main__":
    download_images_from_unsplash() 