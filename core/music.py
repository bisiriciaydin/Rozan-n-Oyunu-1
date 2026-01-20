# core/music.py
from pathlib import Path
import random
import streamlit as st
from core.settings import load_settings, save_settings

BASE_DIR = Path(__file__).resolve().parents[1]   # proje kökü
MUSIC_DIR = BASE_DIR / "assets" / "music"

SUPPORTED = (".mp3", ".wav", ".ogg")


def _music_files():
    if not MUSIC_DIR.exists():
        return []
    files = [p.name for p in MUSIC_DIR.iterdir() if p.suffix.lower() in SUPPORTED]
    files.sort()
    return files


def init_music():
    if st.session_state.get("music_ready"):
        return

    settings = load_settings()
    st.session_state.music_on = bool(settings.get("music_on", True))
    st.session_state.music_file = settings.get("music_file", None)

    files = _music_files()
    if files:
        # ilk açılışta rastgele seç
        st.session_state.music_file = random.choice(files)
    else:
        st.session_state.music_file = None

    st.session_state.music_ready = True

    save_settings({
        "music_on": st.session_state.music_on,
        "music_file": st.session_state.music_file
    })


def music_controls():
    init_music()
    files = _music_files()

    if not files:
        st.info("🎵 Müzik klasöründe mp3 bulunamadı: assets/music")
        return

    with st.expander("🎵 Müzik", expanded=False):
        st.session_state.music_on = st.toggle("Müzik Aç/Kapat", value=st.session_state.music_on)

        if st.button("🎲 Yeni Parça", use_container_width=True):
            st.session_state.music_file = random.choice(files)
            save_settings({
                "music_on": st.session_state.music_on,
                "music_file": st.session_state.music_file
            })
            st.rerun()

        st.caption(f"Seçili parça: **{st.session_state.music_file}**")


def play_music():
    init_music()
    if not st.session_state.music_on:
        return
    if not st.session_state.music_file:
        return

    path = MUSIC_DIR / st.session_state.music_file
    if not path.exists():
        st.warning("Müzik dosyası bulunamadı.")
        return

    audio_bytes = path.read_bytes()
    st.audio(audio_bytes)  # tarayıcı Play butonu gösterir (autoplay engeline takılmaz)
