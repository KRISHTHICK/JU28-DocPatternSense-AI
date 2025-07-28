from utils.word_utils import load_docx, extract_paragraphs
import json

def parse_using_approved(doc_path):
    with open("patterns/approved_pattern.json") as f:
        patterns = json.load(f)

    doc = load_docx(doc_path)
    output = {"headings": [], "tables": []}

    for para in extract_paragraphs(doc):
        if para.text.strip() in patterns["headings"]:
            output["headings"].append(para.text)

    for table in doc.tables:
        rows = [[cell.text for cell in row.cells] for row in table.rows]
        output["tables"].append(rows)

    with open("output/structured_output.json", "w") as f:
        json.dump(output, f, indent=2)

    return output
