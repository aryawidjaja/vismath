import pytesseract
import cv2
from PIL import Image, ImageDraw, ImageFont
from .graph_generator import generate_graph

def put_text_on_image(image_path, text_lines, output_path, category, graphable, equation, roi):
    # Load the image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    
    # Dynamically determine font size based on the height of the bounding box
    font_size = roi.y2 - roi.y1
    font_path = "NanumPenScript-Regular.ttf"
    font = ImageFont.truetype(font_path, size=font_size)

    if category in ['addition', 'subtraction', 'multiplication', 'division']:  # Simple math operations
        # Place the answer directly after the equation
        answer = text_lines[1]
        draw.text((roi.x2 + 10, roi.y1 + (roi.y2 - roi.y1) / 2), answer, font=font, fill="black")
    else:  # Complex math operations
        # Place the steps and answer below the equation
        y_offset = roi.y2 + font_size + 10
        for line in text_lines:
            draw.text((roi.x1, y_offset), line, font=font, fill="black")
            y_offset += font.getbbox(line)[3] + 5  # Increment y for the next line of text

    if graphable == 'yes':
        # Generate and insert graph
        graph_path = "temp_graph.png"
        generate_graph(equation, graph_path, font_path)
        graph_img = Image.open(graph_path)
        image.paste(graph_img, (roi.x1 - graph_img.width - 10, roi.y1 - graph_img.height // 2))

    # Save the image
    image.save(output_path)
