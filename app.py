import streamlit as st
import joblib

# Load model
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

# Minimalist Grey Theme CSS
st.markdown("""
    <style>
    body, .stApp {
        background-color: #f1f1f1;
        font-family: "Segoe UI", sans-serif;
    }

    .header {
        text-align: center;
        padding: 2.5rem 1rem 1rem 1rem;
        margin-bottom: 1.5rem;
    }
    .header h1 {
        color: #333;
        font-size: 2.2rem;
        font-weight: 600;
        margin-bottom: 0.3rem;
    }
    .header p {
        color: #555;
        font-size: 1rem;
        margin: 0;
    }

    .card {
        background: #ffffff;
        padding: 1.7rem;
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        margin-bottom: 1.5rem;
    }

    .stTextArea textarea {
        background: #fafafa !important;
        border-radius: 10px !important;
        border: 1px solid #c9c9c9 !important;
        color: #333 !important;
        font-size: 0.95rem !important;
    }

    .stButton > button {
        background: #4f4f4f !important;
        color: white !important;
        font-size: 1rem !important;
        border-radius: 8px !important;
        padding: 0.6rem 1rem !important;
        border: none !important;
        transition: 0.2s ease-in-out;
    }
    .stButton > button:hover {
        background: #3a3a3a !important;
    }

    .result-title {
        font-weight: 600;
        color: #333;
        font-size: 1.3rem;
        padding-top: 0.5rem;
        margin-bottom: 0.8rem;
    }

    .spam-label {
        color: #c62828;
        font-size: 1.6rem;
        font-weight: 700;
        text-align: center;
        margin: 0.7rem 0;
    }
    .ham-label {
        color: #2e7d32;
        font-size: 1.6rem;
        font-weight: 700;
        text-align: center;
        margin: 0.7rem 0;
    }

    .confidence-box {
        background: #efefef;
        padding: 0.8rem;
        border-radius: 8px;
        border: 1px solid #d8d8d8;
        text-align: center;
        color: #333;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    .footer {
        text-align: center;
        color: #777;
        font-size: 0.85rem;
        margin-top: 2rem;
        padding: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="header">
        <h1>📧 Spam Email Classifier</h1>
        <p>Minimalist Machine Learning for Email Screening</p>
    </div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# Input card with instructions INSIDE
# -------------------------------------------------------------------
with st.container():
    st.markdown("""
        <div class="card">
            <div style="margin-bottom: 1rem;">
                <strong style="color:#333; font-size:1rem;">ℹ️ How to use:</strong>
                <ul style="color:#555; font-size:0.95rem; margin-top:0.5rem;">
                    <li>Insert email text you want to check</li>
                    <li>Press "Analyze Email"</li>
                    <li>System will show the result</li>
                </ul>
            </div>
    """, unsafe_allow_html=True)

    email_text = st.text_area(
        "Email Text",
        height=180,
        placeholder="Paste email content here..."
    )

    st.markdown("</div>", unsafe_allow_html=True)

# Prediction
if st.button("Analyze Email"):
    if email_text.strip() == "":
        st.warning("Email text cannot be empty.")
    else:
        with st.spinner("Analyzing..."):
            pred = model.predict([email_text])[0]
            proba = model.predict_proba([email_text])[0][1]

        st.markdown('<div class="result-title">Analysis Result</div>', unsafe_allow_html=True)

        if pred == 1:
            st.markdown('<div class="spam-label">SPAM</div>', unsafe_allow_html=True)
            st.markdown(
                f'<div class="confidence-box">Confidence: <strong>{proba:.2%}</strong></div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown('<div class="ham-label">HAM (Not Spam)</div>', unsafe_allow_html=True)
            st.markdown(
                f'<div class="confidence-box">Confidence: <strong>{1 - proba:.2%}</strong></div>',
                unsafe_allow_html=True
            )

# Footer
st.markdown("""
    <div class="footer">
        Spam Email Classifier • © 2025
    </div>
""", unsafe_allow_html=True)
