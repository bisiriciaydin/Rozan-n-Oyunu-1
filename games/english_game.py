import random
import streamlit as st

TARGET_SCORE = 100
POINT = 10


# İngilizce → Türkçe + Emoji
WORDS = [
    # Meyveler
    ("Apple", "Elma", "🍎"),
    ("Banana", "Muz", "🍌"),
    ("Orange", "Portakal", "🍊"),
    ("Grape", "Üzüm", "🍇"),
    ("Strawberry", "Çilek", "🍓"),
    ("Watermelon", "Karpuz", "🍉"),

    # Yiyecek – içecek
    ("Water", "Su", "💧"),
    ("Milk", "Süt", "🥛"),
    ("Bread", "Ekmek", "🍞"),
    ("Cheese", "Peynir", "🧀"),
    ("Cake", "Pasta", "🎂"),
    ("Ice cream", "Dondurma", "🍦"),

    # Hayvanlar
    ("Cat", "Kedi", "🐱"),
    ("Dog", "Köpek", "🐶"),
    ("Bird", "Kuş", "🐦"),
    ("Fish", "Balık", "🐟"),
    ("Horse", "At", "🐴"),

    # Doğa
    ("Sun", "Güneş", "☀️"),
    ("Moon", "Ay", "🌙"),
    ("Star", "Yıldız", "⭐"),
    ("Tree", "Ağaç", "🌳"),
    ("Flower", "Çiçek", "🌸"),

    # Ev – okul
    ("House", "Ev", "🏠"),
    ("School", "Okul", "🏫"),
    ("Book", "Kitap", "📘"),
    ("Pencil", "Kalem", "✏️"),
    ("Bag", "Çanta", "🎒"),

    # Renkler
    ("Red", "Kırmızı", "🔴"),
    ("Blue", "Mavi", "🔵"),
    ("Green", "Yeşil", "🟢"),
    ("Yellow", "Sarı", "🟡"),
    ("Black", "Siyah", "⚫"),
    ("White", "Beyaz", "⚪"),

    # 🔹 EYLEMLER (Fiiller)
    ("Go", "Gitmek", "➡️"),
    ("Come", "Gelmek", "⬅️"),
    ("Choose", "Seçmek", "✅"),
    ("See", "Görmek", "👀"),
    ("Look", "Bakmak", "🔎"),
    ("Listen", "Dinlemek", "👂"),
    ("Speak", "Konuşmak", "🗣️"),
    ("Read", "Okumak", "📖"),
    ("Write", "Yazmak", "✍️"),
    ("Draw", "Çizmek", "🎨"),
    ("Run", "Koşmak", "🏃"),
    ("Walk", "Yürümek", "🚶"),
    ("Jump", "Zıplamak", "🤾"),
    ("Play", "Oynamak", "🎮"),
    ("Eat", "Yemek", "🍽️"),
    ("Drink", "İçmek", "🥤"),
    ("Sleep", "Uyumak", "😴"),
    ("Wake up", "Uyanmak", "⏰"),
    ("Open", "Açmak", "📬"),
    ("Close", "Kapatmak", "🔒"),
    ("Give", "Vermek", "🎁"),
    ("Take", "Almak", "🖐️"),
    ("Help", "Yardım etmek", "🤝"),
    ("Love", "Sevmek", "❤️"),
]


def _init_state():
    if "en_score" not in st.session_state:
        st.session_state.en_score = 0
    if "en_item" not in st.session_state:
        st.session_state.en_item = None
    if "en_msg" not in st.session_state:
        st.session_state.en_msg = None


def _new_question():
    en, tr, emoji = random.choice(WORDS)

    pool = [t for (_, t, _) in WORDS if t != tr]
    wrong = random.sample(pool, k=3)
    choices = wrong + [tr]
    random.shuffle(choices)

    st.session_state.en_item = {
        "en": en,
        "tr": tr,
        "emoji": emoji,
        "choices": choices,
    }


def _answer(choice: str):
    item = st.session_state.en_item
    correct = (choice == item["tr"])

    if correct:
        st.session_state.en_score += POINT
        st.session_state.en_msg = ("success", "Aferim Kizima ⭐")
        st.balloons()
    else:
        st.session_state.en_score = max(0, st.session_state.en_score - POINT)
        st.session_state.en_msg = ("info", "Mal Roza Yanliss Yaptin 😊")

    _new_question()
    st.rerun()


def _reset_game():
    st.session_state.en_score = 0
    st.session_state.en_msg = None
    _new_question()
    st.rerun()


def render(go_menu):
    _init_state()
    if st.session_state.en_item is None:
        _new_question()

    score = st.session_state.en_score

    # 🎉 100 puan kutlama
    if score >= TARGET_SCORE:
        st.markdown(
            """
            <div class="roza-hero" style="text-align:center;">
                <h1>🎉 AMAZING! 🎉</h1>
                <p class="roza-small">100 puana ulaştın!</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.balloons()
        st.markdown(
            f"""
            <div class="roza-card" style="text-align:center;">
                <h2>🏆 Puan: {score}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.button("🔁 Play Again", use_container_width=True, on_click=_reset_game)
        st.button("🏠 Ana Menü", use_container_width=True, on_click=lambda: go_menu("menu"))
        return

    item = st.session_state.en_item

    st.markdown(
        """
        <div class="roza-hero">
            <h1>🌍 English Word Game</h1>
            <p class="roza-small">Doğru Türkçe anlamı seç!</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="roza-card">
            <b>🏆 Puan:</b> {score} / {TARGET_SCORE}
        </div>
        """,
        unsafe_allow_html=True
    )

    c_top1, c_top2 = st.columns(2)
    with c_top1:
        st.button("🏠 Ana Menü", use_container_width=True, on_click=lambda: go_menu("menu"))
    with c_top2:
        st.button("🔄 New Word", use_container_width=True, on_click=lambda: (_new_question(), st.rerun()))

    if st.session_state.en_msg:
        kind, text = st.session_state.en_msg
        if kind == "success":
            st.success(text)
        else:
            st.info(text)
        st.session_state.en_msg = None

    st.markdown(
        f"""
        <div class="roza-card" style="text-align:center;">
            <div style="font-size:64px; line-height:1;">
                {item["emoji"]}
            </div>
            <h2>{item["en"]}</h2>
            <p class="roza-small">Türkçesi hangisi?</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)
    for i, val in enumerate(item["choices"]):
        col = c1 if i % 2 == 0 else c2
        with col:
            st.button(
                val,
                use_container_width=True,
                key=f"en_{score}_{i}",
                on_click=lambda x=val: _answer(x)
            )
