def get_font_style(run):
    return {
        "text": run.text,
        "bold": run.bold,
        "italic": run.italic,
        "underline": run.underline,
        "font_size": run.font.size.pt if run.font.size else None,
        "color": run.font.color.rgb if run.font.color else None
    }

def get_cell_background(cell):
    try:
        return cell._element.tcPr.shd.fill  # returns hex color
    except:
        return None
