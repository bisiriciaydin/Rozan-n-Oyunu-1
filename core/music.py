from pathlib import Path
import random
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent.parent
MUSIC_DIR = BASE_DIR / "assets" / "music"

TRACKS = ["aquarium.mp3", "baba.mp3", "mozart.mp3"]


def _read_mp3_bytes(filename: str) -> bytes | None:
    p = MUSIC_DIR / filename
    if not p.exists():
        st.warning(f"🎵 Müzik bulunamadı: {filename}")
        return None
    return p.read_bytes()


def music_controls():
    """
    iPhone uyumlu: Parça seç + görünür player.
    Not: iPhone'da sesi başlatmak için player'daki Play'e basmak gerekir.
    """
    if "music_track" not in st.session_state:
        st.session_state.music_track = TRACKS[0]

    with st.expander("🎵 Müzik", expanded=True):
        c1, c2 = st.columns([1, 2])

        with c1:
            if st.button("🎲 Yeni Parça", use_container_width=True):
                st.session_state.music_track = random.choice(TRACKS)
                st.rerun()

        with c2:
            st.session_state.music_track = st.selectbox(
                "Parça Seç",
                TRACKS,
                index=TRACKS.index(st.session_state.music_track),
                label_visibility="collapsed",
            )

        data = _read_mp3_bytes(st.session_state.music_track)
        if data:
            st.caption("🔊 iPhone’da ses için aşağıdaki oynatıcıdan **Play**’e bas 🙂")
            st.audio(data, format="audio/mpeg")
