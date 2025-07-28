from utils.word_utils import load_docx, extract_paragraphs, extract_tables
from utils.style_utils import get_font_style, get_cell_background
import json

def auto_detect_patterns(path):
    doc = load_docx(path)
    patterns = {"headings": [], "tables": []}

    for para in extract_paragraphs(doc):
        styles = [get_font_style(run) for run in para.runs if run.text.strip()]
        if styles:
            size = styles[0]["font_size"]
            if size and size > 14:
                patterns["headings"].append(para.text)

    for table in extract_tables(doc):
        table_pattern = []
        for row in table.rows:
            row_pattern = []
            for cell in row.cells:
                row_pattern.append({
                    "text": cell.text,
                    "bg_color": get_cell_background(cell),
                })
            table_pattern.append(row_pattern)
        patterns["tables"].append(table_pattern)

    with open("patterns/auto_pattern.json", "w") as f:
        json.dump(patterns, f, indent=2)

    return patterns
