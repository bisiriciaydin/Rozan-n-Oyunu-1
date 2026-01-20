import streamlit as st

from core.state import init_state, go
from core.theme import pick_theme
from core.ui import apply_mobile_ui
from core.music import music_controls
from games.math_game import render as math_render
from games.turkish_game import render as turkish_render
from games.english_game import render as english_render


st.set_page_config(
    page_title="Roza'nın Oyunu",
    page_icon="🎮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def menu_page():
    theme = pick_theme()
    apply_mobile_ui(theme)

    music_controls()

    st.markdown(
        """
        <div class="roza-hero">
            <h1>Roza'nın Oyunu 🎮</h1>
            <p class="roza-small">Bir oyun seçelim mi? 😊</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="roza-card">', unsafe_allow_html=True)
    st.markdown("### 🎯 Oyunlar")
    st.button("🧮 Matematik", use_container_width=True, on_click=lambda: go("math"))
    st.button("📘 Türkçe", use_container_width=True, on_click=lambda: go("turkish"))
    st.button("🌍 İngilizce", use_container_width=True, on_click=lambda: go("english"))
    st.markdown("</div>", unsafe_allow_html=True)

def placeholder_page(title: str):
    theme = pick_theme()
    apply_mobile_ui(theme)

    st.markdown(
        f"<div class='roza-hero'><h1>{title}</h1></div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="roza-card">
            <h3>✨ Yakında!</h3>
            <p class="roza-small">
                Bu oyun birazdan hazır olacak. Şimdilik ana menüye dönebilirsin.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.button("🏠 Ana Menü", use_container_width=True, on_click=lambda: go("menu"))

def router():
    init_state()

    if st.session_state.page == "menu":
        menu_page()

    elif st.session_state.page == "math":
        theme = pick_theme()
        apply_mobile_ui(theme)
        math_render(go)

    elif st.session_state.page == "turkish":
        theme = pick_theme()
        apply_mobile_ui(theme)
        turkish_render(go)

    elif st.session_state.page == "english":
        theme = pick_theme()
        apply_mobile_ui(theme)
        english_render(go)

    else:
        go("menu")


router()
