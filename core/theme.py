import streamlit as st

THEMES = {
    "Pembe 🌸": {"bg": "#FFF5FB", "card": "#FFFFFF", "text": "#111827", "accent": "#FF4DA6"},
    "Mavi 🌈":  {"bg": "#F3F7FF", "card": "#FFFFFF", "text": "#111827", "accent": "#3B82F6"},
    "Yeşil 🍀": {"bg": "#F4FFF7", "card": "#FFFFFF", "text": "#111827", "accent": "#22C55E"},
}

def pick_theme():
    if "theme_name" not in st.session_state:
        st.session_state.theme_name = "Pembe 🌸"

    with st.sidebar:
        st.markdown("### 🎨 Tema")
        st.session_state.theme_name = st.selectbox(
            "Seç:",
            list(THEMES.keys()),
            index=list(THEMES.keys()).index(st.session_state.theme_name)
        )

    return THEMES[st.session_state.theme_name]
