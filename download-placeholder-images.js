/**
 * This script helps download placeholder images for the construction website.
 * It lists the required images that should be manually downloaded from free stock photo sites like:
 * - Unsplash (https://unsplash.com/)
 * - Pexels (https://www.pexels.com/)
 * - Pixabay (https://pixabay.com/)
 * 
 * Search terms: construction, building, architecture, contractor, renovation
 */

// List of images needed for the website
const imagesList = [
  {
    filename: "logo.png",
    description: "Company logo - Create a simple construction logo with blue and orange colors"
  },
  {
    filename: "logo-white.png",
    description: "White version of company logo for footer"
  },
  {
    filename: "favicon.ico",
    description: "Website favicon"
  },
  {
    filename: "hero-bg.jpg",
    description: "Hero section background - Construction workers or construction site with modern building"
  },
  {
    filename: "about-img.jpg",
    description: "About section image - Team of construction professionals or company office"
  },
  {
    filename: "counter-bg.jpg",
    description: "Counter section background - Dark-tinted construction or architecture image"
  },
  {
    filename: "services-banner.jpg",
    description: "Services page banner - Wide construction site or building image"
  },
  {
    filename: "projects-banner.jpg",
    description: "Projects page banner - Wide construction site or completed building"
  },
  {
    filename: "cta-bg.jpg",
    description: "Call-to-action background - Construction site or blueprint image"
  },
  
  // Service Images
  {
    filename: "service-commercial.jpg",
    description: "Commercial construction service - Commercial building or office space"
  },
  {
    filename: "service-residential.jpg",
    description: "Residential construction service - Modern home or residential building"
  },
  {
    filename: "service-renovation.jpg",
    description: "Renovation service - Home renovation or remodeling"
  },
  {
    filename: "service-project-management.jpg",
    description: "Project management service - Construction manager with plans or team meeting"
  },
  {
    filename: "service-design.jpg",
    description: "Design-build service - Architectural plans or design discussion"
  },
  {
    filename: "service-consultation.jpg",
    description: "Consultation service - Client meeting or discussion of plans"
  },
  
  // Detailed Service Images
  {
    filename: "commercial-construction.jpg",
    description: "Commercial construction detail - Office building or commercial space"
  },
  {
    filename: "residential-construction.jpg",
    description: "Residential construction detail - Luxury home or residential property"
  },
  {
    filename: "renovations.jpg",
    description: "Renovations detail - Before/after renovation or remodeling work"
  },
  {
    filename: "project-management.jpg",
    description: "Project management detail - Construction manager on site"
  },
  {
    filename: "design-build.jpg",
    description: "Design-build detail - Architectural design process or blueprints"
  },
  {
    filename: "consultation.jpg",
    description: "Consultation detail - Meeting with clients or discussing plans"
  },
  
  // Project Images
  {
    filename: "project1.jpg",
    description: "Project 1 - Modern office building exterior"
  },
  {
    filename: "project2.jpg",
    description: "Project 2 - Luxury residential home"
  },
  {
    filename: "project3.jpg",
    description: "Project 3 - Retail shopping center"
  },
  {
    filename: "project4.jpg",
    description: "Project 4 - Historic building renovation"
  },
  {
    filename: "project5.jpg",
    description: "Project 5 - Multi-family apartment complex"
  },
  {
    filename: "project6.jpg",
    description: "Project 6 - Restaurant renovation"
  },
  {
    filename: "project7.jpg",
    description: "Project 7 - Community center"
  },
  {
    filename: "project8.jpg",
    description: "Project 8 - Corporate headquarters"
  },
  {
    filename: "project9.jpg",
    description: "Project 9 - School building"
  },
  
  // Project Detail Images for Project 1
  {
    filename: "project1-1.jpg",
    description: "Project 1 Detail 1 - Office building exterior angle"
  },
  {
    filename: "project1-2.jpg",
    description: "Project 1 Detail 2 - Office building interior lobby"
  },
  {
    filename: "project1-3.jpg",
    description: "Project 1 Detail 3 - Office building conference room"
  },
  {
    filename: "project1-4.jpg",
    description: "Project 1 Detail 4 - Office building workspace area"
  }
];

// Print the list as a reference
console.log("Construction Website Image List");
console.log("==============================");
console.log("Download these images from free stock photo websites and save them to the 'images' folder:\n");

imagesList.forEach((image, index) => {
  console.log(`${index + 1}. ${image.filename}`);
  console.log(`   Description: ${image.description}`);
  console.log("");
});

console.log("Recommended sources:");
console.log("- Unsplash: https://unsplash.com/");
console.log("- Pexels: https://www.pexels.com/");
console.log("- Pixabay: https://pixabay.com/");
console.log("\nSearch terms: construction, building, architecture, contractor, renovation");
console.log("\nMake sure to save the images in the 'images' folder of your project."); 