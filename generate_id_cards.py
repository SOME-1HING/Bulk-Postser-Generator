import os
from PIL import Image, ImageDraw, ImageFont

def generate_posters(poster_template, output_folder, num_posters=10):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    processed_count = 0

    for number in range(26, num_posters + 1):  
        # Load the poster template
        poster = Image.open(poster_template)
        
        # Add number text
        draw = ImageDraw.Draw(poster)
        
        # Use ARIALBD.TTF font
        font_path = "./ARIALBD.TTF" 
        
        # Try to use ARIALBD font, fall back to Arial if not available
        try:
            if os.path.exists(font_path):
                name_font = ImageFont.truetype(font_path, 180) 
            else:
                name_font = ImageFont.truetype("arial.ttf", 180) 
        except Exception as e:
            print(f"Error loading font: {e}")
            name_font = ImageFont.load_default()
        
        # Add the number text with leading zeros
        number_text = f"{number:02d}"
        
        # Get text bounding box to calculate center position
        bbox = draw.textbbox((0, 0), number_text, font=name_font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Get image dimensions
        img_width, img_height = poster.size
        
        # Calculate center position
        name_x = (img_width - text_width) // 2  # Center horizontally
        name_y = 975  # Keep the same Y position (adjust as needed)
        
        draw.text((int(name_x), int(name_y)), number_text, fill="#ffffff", font=name_font)
        
        # Save the generated poster
        output_path = os.path.join(output_folder, f"{number:02d}_poster.jpg")
        poster.save(output_path)
        processed_count += 1
        print(f"Generated poster for number {number}")
        
    # Print summary
    print("\n" + "="*50)
    print(f"SUMMARY: Generated {processed_count} posters")
    print("="*50)


if __name__ == "__main__":
    # Define paths
    poster_template = "./Visitor.jpg"
    output_folder = "./visitor"

    # Generate 200 numbered posters (01 to 200) using Maintenance.jpg as template
    generate_posters(poster_template, output_folder, num_posters=999)
    
