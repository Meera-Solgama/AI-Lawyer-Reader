import streamlit as st

# Define stop words
STOP_WORDS = {
    'the', 'is', 'am', 'are', 'was', 'were', 'be', 'been', 'being',
    'this', 'that', 'those', 'these', 'by', 'of', 'at', 'to', 'from',
    'and', 'or', 'for', 'in', 'on', 'with', 'as', 'an', 'a', 'any', 'all',
    'into', 'shall', 'under', 'herein', 'out', 'against', 'it',
    'made', 'entered', 'effective', 'date'
}

# Define important words
HIGH_IMPORTANCE_WORDS = {
    'indemnify', 'indemnity', 'liability', 'damages', 'breach', 'arbitration',
    'jurisdiction', 'confidentiality', 'warranty', 'warranties', 'governing',
    'termination', 'enforceable', 'compliance', 'representation', 'obligations',
    'non-disclosure', 'force-majeure', 'infringement', 'assignability', 'patent',
    'copyright', 'statute', 'litigation', 'claimant', 'settlement', 'compensation',
    'fiduciary', 'limitation', 'promissory', 'mortgage', 'lien', 'covenant',
    'subrogation', 'undertaking', 'escrow', 'attorney', 'precedent', 'due-diligence',
    'guarantor', 'security-interest', 'liquidated', 'merger', 'acquisition',
    'disclosure', 'proprietary', 'undertaking', 'clause', 'novation'
}

# Define less important words
LOW_IMPORTANCE_WORDS = {
    'agreement', 'contract', 'parties', 'hereby', 'herein', 'herewith',
    'therefore', 'whereas', 'pursuant', 'forthwith', 'aforesaid', 'hereto',
    'hereunder', 'witnesseth', 'nonetheless', 'nevertheless', 'thereby',
    'thereof', 'wherein', 'thenceforth', 'henceforth', 'hereinabove',
    'therein', 'wherein', 'hereafter', 'whereby', 'hereunto', 'whenever',
    'wherever', 'whichever', 'therewith', 'thereafter', 'thereby', 'thereto',
    'thereunder', 'thereinbefore', 'whereinsoever', 'hereupon', 'amongst',
    'accordingly', 'moreover', 'furthermore', 'pursuant', 'thereby', 'thence',
    'henceforth', 'hereinbefore', 'hereinafter'
}

def highlight_important_words(paragraph: str) -> str:
    words = paragraph.split()
    highlighted = []
    
    for w in words:
        word_plain = ''.join([ch for ch in w if ch.isalpha()]).lower()
        if word_plain in HIGH_IMPORTANCE_WORDS:
            highlighted.append(f"<span style='background-color:#8B0000; color:white'>{w}</span>")  # Dark red
        elif word_plain in LOW_IMPORTANCE_WORDS:
            highlighted.append(f"<span style='background-color:#ffb6c1'>{w}</span>")  # Light red
        elif word_plain not in STOP_WORDS:
            highlighted.append(f"<span style='background-color:#ffcccb'>{w}</span>")  # Light light red
        else:
            highlighted.append(w)
    
    return ' '.join(highlighted)

# Streamlit UI
def main():
    st.title("Legal Paragraph Highlighter")
    st.markdown("""
    This tool highlights important words in legal paragraphs based on their significance:
    - 🔴 **High Importance Words**: Dark red background
    - 🟡 **Low Importance Words**: Light red background
    """)
    
    # Input paragraph
    paragraph = st.text_area("Enter English legal paragraph:", height=200)
    
    if st.button("Analyze"):
        if paragraph:
            # Highlight words
            html_out = highlight_important_words(paragraph)
            # Display highlighted output
            st.markdown(html_out, unsafe_allow_html=True)
        else:
            st.warning("Please enter a paragraph to highlight.")

if __name__ == "__main__":
    main()
