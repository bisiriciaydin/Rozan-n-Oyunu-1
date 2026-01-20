import random
import streamlit as st
from core.sfx import queue as sfx_queue

DOGRU_SOZLER = [
    "Harika! ⭐",
    "Süpersin Roza! 🌸",
    "Çok iyi gidiyorsun! 🎉",
    "Mükemmel cevap! 🥳",
    "Aferin! Devam! 🚀",
]

YANLIS_SOZLER = [
    "Olabilir 😊 Bir daha deneyelim!",
    "Yaklaştın! Hadi tekrar 💪",
    "Sorun değil 🌈 Tekrar dene!",
    "Denemek çok güzel! Bir kez daha ✨",
]

def show_success():
    sfx_queue("success")
    st.session_state.toast = ("success", random.choice(DOGRU_SOZLER))

def show_try_again():
    sfx_queue("wrong")
    st.session_state.toast = ("info", random.choice(YANLIS_SOZLER))

def render_toast():
    """Sayfanın üst kısmında çağır."""
    toast = st.session_state.get("toast")
    if not toast:
        return

    kind, msg = toast
    if kind == "success":
        st.balloons()
        st.success(msg)
    else:
        st.info(msg)

    st.session_state.toast = None
