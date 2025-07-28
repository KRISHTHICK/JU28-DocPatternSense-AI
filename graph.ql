doc-pattern-sense/
├── app.py                     # Streamlit UI
├── pattern_extractor.py       # AI + rule-based pattern extractor
├── pattern_approver.py        # Human approval interface
├── doc_parser.py              # Apply patterns to extract structured data
├── utils/
│   ├── word_utils.py          # Word file utilities
│   └── style_utils.py         # Helpers for colors, font, size, etc.
├── patterns/
│   └── approved_pattern.json  # Human-approved extraction patterns
├── samples/
│   └── complex_sample.docx    # Complex MS Word file
├── output/
│   └── structured_output.json # Final structured data
├── requirements.txt
