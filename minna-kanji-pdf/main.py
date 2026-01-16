import os
import sys

# Add the current directory to sys.path to ensure local imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.data_loader import load_lesson_data
from src.pdf_renderer import render_html, generate_pdf

def main():
    # Configuration
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_FILE = os.path.join(BASE_DIR, 'data', 'lesson_26.json')
    OUTPUT_FILE = os.path.join(BASE_DIR, 'output', 'Bai_26_Minna.pdf')
    TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
    
    print(f"Starting Minna Kanji PDF Generator...")
    print(f"Base Directory: {BASE_DIR}")
    
    try:
        # 1. Load Data
        print(f"Loading data from {DATA_FILE}...")
        data = load_lesson_data(DATA_FILE)
        
        # 2. Render HTML
        print("Rendering HTML template...")
        html_content = render_html(data, 'lesson.html', TEMPLATES_DIR)
        
        # 3. Generate PDF
        # We pass TEMPLATES_DIR as base_url so WeasyPrint finds style.css
        generate_pdf(html_content, OUTPUT_FILE, base_url=TEMPLATES_DIR)
        
        print(f"Success! PDF saved to: {OUTPUT_FILE}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
