from PIL import Image, ImageDraw, ImageFont
import os

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

def generate_logo(filename, background_color, text_color):
    """Generate a simple logo for the construction company."""
    width, height = 300, 100
    image = Image.new('RGBA', (width, height), background_color)
    draw = ImageDraw.Draw(image)
    
    # Try to use a nice font if available, otherwise use default
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except IOError:
        font = ImageFont.load_default()
    
    # Company name
    draw.text((20, 20), "CDS", fill=text_color, font=font)
    draw.text((110, 40), "CONTRACTORS", fill=text_color, font=ImageFont.truetype("arial.ttf", 20) if 'arial.ttf' in ImageFont.truetype.__annotations__ else ImageFont.load_default())
    
    # Draw a building icon
    draw.rectangle([(200, 30), (215, 70)], fill=text_color)
    draw.rectangle([(225, 40), (240, 70)], fill=text_color)
    draw.rectangle([(250, 25), (265, 70)], fill=text_color)
    
    # Draw a line under the text
    draw.line([(20, 80), (265, 80)], fill=text_color, width=3)
    
    # Save the image
    image.save(os.path.join('images', filename))
    print(f"Generated {filename}")

def main():
    """Generate both logo versions."""
    # Generate blue logo with orange accents
    generate_logo("logo.png", (30, 86, 160, 255), (247, 179, 43, 255))
    
    # Generate white logo with transparent background
    generate_logo("logo-white.png", (0, 0, 0, 0), (255, 255, 255, 255))
    
    # Generate favicon (small version of the logo)
    width, height = 32, 32
    image = Image.new('RGBA', (width, height), (30, 86, 160, 255))
    draw = ImageDraw.Draw(image)
    
    # Draw a simple "C" for the favicon
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except IOError:
        font = ImageFont.load_default()
    
    draw.text((8, 0), "C", fill=(247, 179, 43, 255), font=font)
    
    # Save as ICO
    image.save(os.path.join('images', 'favicon.ico'), format='ICO')
    print("Generated favicon.ico")

if __name__ == "__main__":
    main()
    print("\nLogo files have been created in the 'images' directory.")
    print("You can now use them in your website.") 