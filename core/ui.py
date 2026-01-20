import streamlit as st

def apply_mobile_ui(theme: dict | None = None):
    """
    iPhone/telefon uyumlu, yüksek kontrastlı, büyük dokunma alanlı UI.
    theme: {"bg": "...", "card": "...", "text": "...", "muted": "...", "accent": "..."}
    """
    theme = theme or {}
    bg = theme.get("bg", "#FFF5FA")          # açık pembe arka plan
    card = theme.get("card", "#FFFFFF")      # kart beyaz
    text = theme.get("text", "#111827")      # koyu yazı
    muted = theme.get("muted", "#6B7280")    # gri yazı
    accent = theme.get("accent", "#EC4899")  # pembe vurgu

    st.markdown(
        f"""
        <style>
        /* Genel */
        html, body, [class*="css"] {{
            -webkit-text-size-adjust: 100%;
        }}

        .stApp {{
            background: {bg};
        }}

        /* Sayfa genişliği ve padding (mobil öncelikli) */
        section.main > div {{
            padding-top: 0.6rem;
        }}

        .main .block-container {{
            max-width: 520px;
            padding-left: 0.9rem;
            padding-right: 0.9rem;
            padding-bottom: 2rem;
        }}

        @media (max-width: 600px) {{
            .main .block-container {{
                max-width: 420px;
                padding-left: 0.75rem;
                padding-right: 0.75rem;
            }}
        }}

        /* Kartlar */
        .roza-hero {{
            background: linear-gradient(135deg, rgba(236,72,153,0.10), rgba(255,255,255,0.60));
            border: 1px solid rgba(17,24,39,0.08);
            border-radius: 18px;
            padding: 18px 16px;
            margin: 8px 0 12px 0;
        }}

        .roza-hero h1 {{
            color: {text};
            font-size: 34px;
            line-height: 1.15;
            margin: 0;
            font-weight: 800;
            letter-spacing: -0.5px;
        }}

        .roza-small {{
            color: {muted};
            font-size: 16px;
            margin-top: 8px;
            margin-bottom: 0;
        }}

        .roza-card {{
            background: {card};
            border: 1px solid rgba(17,24,39,0.08);
            border-radius: 18px;
            padding: 14px 14px;
            margin: 10px 0;
            box-shadow: 0 6px 18px rgba(17,24,39,0.06);
        }}

        .roza-accent {{
            color: {accent};
            font-weight: 800;
        }}

        /* Butonlar: iPhone dokunma hedefi büyük + yazı görünür + sol hizalı */
        .stButton > button {{
            width: 100% !important;
            border-radius: 18px !important;
            padding: 16px 16px !important;
            min-height: 58px !important;
            border: 1px solid rgba(17,24,39,0.10) !important;
            background: #FFFFFF !important;
            color: {text} !important;
            font-size: 18px !important;
            font-weight: 800 !important;

            display: flex !important;
            align-items: center !important;
            justify-content: flex-start !important;
            gap: 10px !important;
        }}

        /* Buton içindeki metin (Streamlit bazen <p> ile geliyor) */
        .stButton > button p, .stButton > button span {{
            color: {text} !important;
            font-size: 18px !important;
            font-weight: 800 !important;
            margin: 0 !important;
            opacity: 1 !important;
        }}

        .stButton > button:hover {{
            border-color: rgba(236,72,153,0.35) !important;
            box-shadow: 0 10px 22px rgba(236,72,153,0.10) !important;
            transform: translateY(-1px);
        }}

        /* Streamlit'in bazı ekstra boşluklarını azalt */
        div[data-testid="stVerticalBlock"] > div {{
            gap: 0.65rem;
        }}

        /* Şu "boş beyaz şerit" genelde boş bir container/markdown'dan geliyor.
           Mobilde bu tip spacer'ları görünmez yapıyoruz. */
        .roza-spacer {{
            display: none !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
