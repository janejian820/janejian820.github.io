# Construction-Company-Website
![Screenshot 2025-04-26 225820](https://github.com/user-attachments/assets/694ad709-c87d-4843-b9cb-1c5ff9753dca)
![Screenshot 2025-04-26 225835](https://github.com/user-attachments/assets/6f4b8514-8626-4468-a467-8f717a98ce7a)
![Screenshot 2025-04-26 231631](https://github.com/user-attachments/assets/0c2ee63c-d51b-49e6-8b9c-ffa18f533e84)
![Screenshot 2025-04-26 225944](https://github.com/user-attachments/assets/af2d3ce6-3cb8-446f-a824-3a5a669bbe9a)
![Screenshot 2025-04-26 230012](https://github.com/user-attachments/assets/544c4615-54d3-4648-bf1b-fa466a5bd099)
![Screenshot 2025-04-27 000439](https://github.com/user-attachments/assets/ec133ddb-c030-4ce9-bd36-0e2e96281a13)
![Screenshot 2025-04-26 230027](https://github.com/user-attachments/assets/d60bc3ac-deb8-4bf1-8092-dc79d72ad81c)
# Modern Construction Company Website

A 2025-style construction industry website built with HTML, CSS, and JavaScript. This project features a responsive design, modern UI components, and construction-themed aesthetics.

## Features

- Responsive, mobile-first design
- Modern construction industry aesthetics with vibrant color scheme
- Interactive components (navbar, sliders, galleries)
- Smooth scrolling and animations
- SEO optimized
- Project filtering system
- Testimonial carousel
- Contact form with validation
- Back-to-top button
- Newsletter subscription form
- Enhanced visual elements with gradients and effects

## Pages Included

1. **Home** (`index.html`) - Main landing page with all key sections
2. **Services** (`services.html`) - Detailed information about construction services
3. **Projects** (`projects.html`) - Portfolio of construction projects with filtering
4. **About** (`about.html`) - Company information and team
5. **Careers** (`careers.html`) - Job listings and application
6. **Contact** (`contact.html`) - Extended contact information

## Getting Started

### Prerequisites

- Basic web server or hosting platform
- Python 3.6+ (for generating images)

### Setup Instructions

1. **Clone this repository**
   ```
   git clone <repository-url>
   ```

2. **Generate Images**
   - For logo generation: Install Python with Pillow and run the generator script
     ```
     pip install Pillow
     python generate_logo.py
     ```
   - For downloading stock photos:
     ```
     pip install requests
     python download-images.py
     ```
   - See `image-generation-readme.md` for detailed instructions

3. **Open the website**
   - Open `index.html` in your browser to view the website
   - For a better experience, use a local server:
     ```
     # If you have Node.js installed:
     npx serve
     
     # If you have Python installed:
     # Python 3.x
     python -m http.server
     # Python 2.x
     python -m SimpleHTTPServer
     ```

## Customization

### Enhanced Color Scheme

The website uses a vibrant color palette that can be easily modified:

```css
:root {
  /* Color Palette */
  --primary: #1e56a0;       /* Deeper, more vibrant blue */
  --primary-dark: #163172;
  --secondary: #f7b32b;     /* Brighter, golden yellow */
  --accent: #d72323;        /* Bold accent red for highlights */
  --light: #f8f9fa;
  --dark: #242b40;          /* Darker blue-grey for depth */
  --gray: #6c757d;
  --light-gray: #e9ecef;
}
```

### Button Styles

The buttons have been enhanced with hover effects and additional styles:

- `.btn-primary` - Blue buttons for primary actions
- `.btn-secondary` - Gold buttons for secondary actions
- `.btn-accent` - Red buttons for attention-grabbing elements
- `.btn-outline` - Outlined buttons with hover effects

### Content

- Replace placeholder text with your actual company information
- Update services and project details to match your offerings
- Replace placeholder images with your actual project photos
- Add your company logo

### Adding New Pages

To add a new page:

1. Copy the structure from an existing page (e.g., `services.html`)
2. Keep the header and footer sections
3. Modify the main content as needed
4. Update navigation links in all pages to include the new page

## Browser Compatibility

The website is compatible with:
- Google Chrome (latest)
- Mozilla Firefox (latest)
- Microsoft Edge (latest)
- Safari (latest)
- Opera (latest)
- Mobile browsers (iOS Safari, Android Chrome)

## Technologies Used

- HTML5
- CSS3 (with Flexbox and Grid)
- JavaScript (ES6+)
- Font Awesome (for icons)
- Google Fonts (Montserrat and Open Sans)
- Python (for image generation scripts)

## Extending the Website

### Adding Blog Functionality

To add a blog section:
1. Create a `blog.html` page for the blog listing
2. Create individual blog post pages in a `/blog` folder
3. Add pagination for the blog listings
4. Update navigation to include the blog section

### Adding a Project CMS

For dynamic project management:
1. Convert the static HTML to templates (e.g., using Handlebars, EJS, etc.)
2. Set up a backend server (Node.js, PHP, etc.)
3. Create a database to store project information
4. Add admin functionality to manage projects

## License

This project is open-source and available under the MIT License.

## Credits

- Font Awesome for icons
- Google Fonts for typography
- Unsplash, Pexels, and Pixabay for stock photo references

## Author
Developed by Jeremy Martinez-Quinones.
