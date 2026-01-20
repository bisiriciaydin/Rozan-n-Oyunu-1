import streamlit as st

def apply_mobile_ui(theme: dict):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: {theme["bg"]};
            color: {theme["text"]};
        }}
        .block-container {{
            max-width: 520px;
            padding-top: 0.8rem;
            padding-bottom: 2.2rem;
        }}
        .roza-card {{
            background: {theme["card"]};
            border: 1px solid rgba(0,0,0,0.06);
            border-radius: 18px;
            padding: 14px;
            box-shadow: 0 10px 24px rgba(0,0,0,0.06);
            margin-bottom: 12px;
        }}
        .roza-hero {{
            border-radius: 18px;
            padding: 14px;
            background: linear-gradient(135deg, {theme["accent"]}22, rgba(255,255,255,0.6));
            border: 1px solid rgba(0,0,0,0.05);
            margin-bottom: 12px;
        }}
        .roza-small {{
            opacity: 0.85;
            font-size: 14px;
        }}
        div.stButton > button {{
            width: 100%;
            min-height: 54px;
            border-radius: 16px;
            font-size: 18px;
            font-weight: 800;
            border: none;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
