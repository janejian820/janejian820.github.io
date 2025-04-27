# Image Generation Instructions

This directory contains scripts to generate and download images for the Construction Company website. Follow the steps below to get all the necessary images.

## Prerequisites

You need Python 3.6+ installed on your system. You'll also need the following Python packages:

```
pip install Pillow requests
```

## Generating the Logo and Favicon

Run the following command to generate the company logo and favicon:

```
python generate_logo.py
```

This will create:
- `images/logo.png` - Blue and gold company logo for the header
- `images/logo-white.png` - White logo for the footer
- `images/favicon.ico` - Website favicon

## Downloading Stock Photos

To download all the required stock photos from Unsplash, you have two options:

### Option 1: Quick Demo (Limited Usage)

Run the script with the demo API key:

```
python download-images.py
```

This will attempt to download images using Unsplash's demo API key, but it is very limited and may not work for all images.

### Option 2: Get Your Own API Key (Recommended)

1. Sign up for a free Unsplash developer account at [https://unsplash.com/developers](https://unsplash.com/developers)
2. Create a new application to get an access key
3. Open `download-images.py` and replace `"YOUR_UNSPLASH_ACCESS_KEY"` with your actual access key
4. Run the script:
   ```
   python download-images.py
   ```

## Alternative: Manual Download

If the scripts don't work for you, you can manually download appropriate images from free stock photo sites:

1. Check the image list in `download-placeholder-images.js`
2. Download suitable images from:
   - [Unsplash](https://unsplash.com/)
   - [Pexels](https://www.pexels.com/)
   - [Pixabay](https://pixabay.com/)
3. Save them in the `images` directory with the specified filenames

## Image Requirements

The website design requires these types of images:
- Hero/banner backgrounds
- Service category images
- Project portfolio images
- Team and about section images
- Background images for CTA sections

Use the search terms: construction, building, architecture, contractor, renovation

## Next Steps

After generating all images, open the website in your browser to see the changes. The CSS has been updated with a more vibrant color scheme to make the site more visually appealing. 