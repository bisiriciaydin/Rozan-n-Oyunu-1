from pathlib import Path
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent.parent  # proje kökü
MUSIC_DIR = BASE_DIR / "assets" / "music"


def play_music(filename: str = "aquarium.mp3"):
    """
    Arka plan müziğini güvenli şekilde çalar.
    iPhone + Streamlit Cloud uyumlu.
    """
    music_path = MUSIC_DIR / filename

    if not music_path.exists():
        st.warning(f"Müzik bulunamadı: {filename}")
        return

    audio_bytes = music_path.read_bytes()

    st.audio(audio_bytes, format="audio/mpeg", loop=True)


def music_controls():
    """
    Çocuk için basit müzik seçici.
    """
    with st.expander("🎵 Müzik"):
        choice = st.radio(
            "Müzik Seç",
            ["aquarium.mp3", "baba.mp3", "mozart.mp3"],
            horizontal=True
        )

        play_music(choice)
