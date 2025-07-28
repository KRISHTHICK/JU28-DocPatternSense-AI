import json
import streamlit as st

def review_patterns():
    st.title("🧠 Approve Extracted Patterns")
    with open("patterns/auto_pattern.json") as f:
        patterns = json.load(f)

    updated = {}
    for key, items in patterns.items():
        st.subheader(f"{key.upper()}")
        updated[key] = st.text_area(f"Edit {key}", value=json.dumps(items, indent=2))

    if st.button("✅ Save Approved Pattern"):
        with open("patterns/approved_pattern.json", "w") as f:
            json.dump({k: json.loads(v) for k, v in updated.items()}, f, indent=2)
        st.success("Pattern saved!")
