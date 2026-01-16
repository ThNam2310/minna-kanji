import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS

def render_html(data: dict, template_name: str, templates_dir: str) -> str:
    """
    Renders data into an HTML string using a Jinja2 template.
    
    Args:
        data (dict): The data to render.
        template_name (str): The name of the template file (e.g., 'lesson.html').
        templates_dir (str): Path to the templates directory.
        
    Returns:
        str: The rendered HTML string.
    """
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template(template_name)
    return template.render(**data)

def generate_pdf(html_content: str, output_path: str, base_url: str):
    """
    Generates a PDF from an HTML string using WeasyPrint.
    
    Args:
        html_content (str): The HTML content to render.
        output_path (str): The path to save the PDF.
        base_url (str): Base URL for resolving relative links (like CSS).
    """
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    print(f"Generating PDF to {output_path}...")
    HTML(string=html_content, base_url=base_url).write_pdf(output_path)
    print("PDF generation complete.")
