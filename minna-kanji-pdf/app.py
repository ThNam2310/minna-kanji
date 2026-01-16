import os
import sys
from flask import Flask, render_template, abort, send_file, request

# Add the current directory to sys.path to ensure local imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.data_loader import get_all_lessons, get_lesson_by_id

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

@app.route('/')
def index():
    lessons = get_all_lessons(DATA_DIR)
    return render_template('index.html', lessons=lessons)

@app.route('/lesson/<int:lesson_id>')
def lesson_detail(lesson_id):
    try:
        lesson_data = get_lesson_by_id(lesson_id, DATA_DIR)
        return render_template('lesson.html', **lesson_data)
    except FileNotFoundError:
        abort(404)

@app.route('/lesson/<int:lesson_id>/pdf')
def download_pdf(lesson_id):
    try:
        # 1. Get Data
        lesson_data = get_lesson_by_id(lesson_id, DATA_DIR)
        
        # 2. Render HTML for PDF
        from src.pdf_renderer import render_html
        from weasyprint import HTML
        from io import BytesIO
        
        html_content = render_template('practice_sheet.html', **lesson_data)
        
        # 3. Generate PDF in memory
        pdf_io = BytesIO()
        HTML(string=html_content).write_pdf(pdf_io)
        pdf_io.seek(0)
        
        # 4. Check for download query param
        should_download = request.args.get('download') == 'true'
        
        # 5. Return response
        return send_file(
            pdf_io,
            as_attachment=should_download,
            download_name=f"Tap_Viet_Bai_{lesson_id}.pdf",
            mimetype='application/pdf'
        )
        
    except FileNotFoundError:
        abort(404)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
