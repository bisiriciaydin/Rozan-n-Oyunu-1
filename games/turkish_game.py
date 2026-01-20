import random
import streamlit as st

from games.tr_words import SYNONYMS, ANTONYMS

TARGET_SCORE = 100
POINT = 10


def _init_state():
    if "tr_score" not in st.session_state:
        st.session_state.tr_score = 0
    if "tr_mode" not in st.session_state:
        st.session_state.tr_mode = "menu"  # "menu" | "syn" | "ant"
    if "tr_item" not in st.session_state:
        st.session_state.tr_item = None
    if "tr_msg" not in st.session_state:
        st.session_state.tr_msg = None


def _pick_pair(mode: str):
    if mode == "syn":
        return random.choice(SYNONYMS)
    return random.choice(ANTONYMS)


def _build_question(mode: str):
    a, b = _pick_pair(mode)

    # Soruyu baz kelime üzerinden soralım
    base = a
    answer = b

    # Şıkları diğer çiftlerin "b" taraflarından üretelim
    pool = [x[1] for x in (SYNONYMS if mode == "syn" else ANTONYMS)]
    pool = [p for p in pool if p != answer]

    wrong = random.sample(pool, k=3)
    choices = wrong + [answer]
    random.shuffle(choices)

    prompt = "Eş anlamlısını seç" if mode == "syn" else "Zıt anlamlısını seç"
    st.session_state.tr_item = {
        "mode": mode,
        "base": base,
        "answer": answer,
        "choices": choices,
        "prompt": prompt,
    }


def _new_question():
    mode = st.session_state.tr_mode
    if mode in ("syn", "ant"):
        _build_question(mode)

def _norm(text: str) -> str:
    return text.strip().casefold()

def _answer(choice: str):
    item = st.session_state.tr_item
    correct = (_norm(choice) == _norm(item["answer"]))

    if correct:
        st.session_state.tr_score += POINT
        st.session_state.tr_msg = ("success", "Harika! ⭐ Doğru bildin!")
        st.balloons()
    else:
        st.session_state.tr_score = max(0, st.session_state.tr_score - POINT)
        st.session_state.tr_msg = ("info", "Sorun değil 😊 Bir daha deneyelim!")

    _new_question()
    st.rerun()


def _reset_game():
    st.session_state.tr_score = 0
    st.session_state.tr_msg = None
    _new_question()
    st.rerun()


def _go_mode(mode: str):
    st.session_state.tr_mode = mode
    st.session_state.tr_msg = None
    st.session_state.tr_item = None
    if mode in ("syn", "ant"):
        _new_question()
    st.rerun()


def render(go_menu):
    _init_state()

    score = st.session_state.tr_score

    # 🎉 100 puan kutlama
    if score >= TARGET_SCORE:
        st.markdown(
            """
            <div class="roza-hero" style="text-align:center;">
                <h1>🎉 HARİKASIN ROZA! 🎉</h1>
                <p class="roza-small">100 puana ulaştın! ⭐⭐⭐</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.balloons()
        st.markdown(
            f"""
            <div class="roza-card" style="text-align:center;">
                <h2>🏆 Toplam Puan: {score}</h2>
                <p class="roza-small">İstersen tekrar oynayabilir ya da menüye dönebilirsin.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.button("🔁 Baştan Oyna", use_container_width=True, on_click=_reset_game)
        st.button("🏠 Ana Menü", use_container_width=True, on_click=lambda: go_menu("menu"))
        return

    # Üst başlık
    st.markdown(
        """
        <div class="roza-hero">
            <h1>📘 Türkçe Oyunu</h1>
            <p class="roza-small">Bir bölüm seçelim mi? ✨</p>
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

    # Üst butonlar
    c_top1, c_top2 = st.columns(2)
    with c_top1:
        st.button("🏠 Ana Menü", use_container_width=True, on_click=lambda: go_menu("menu"))
    with c_top2:
        if st.session_state.tr_mode in ("syn", "ant"):
            st.button("🔄 Yeni Soru", use_container_width=True, on_click=lambda: (_new_question(), st.rerun()))
        else:
            st.button("🧼 Puan Sıfırla", use_container_width=True, on_click=_reset_game)

    # Bölüm seçme menüsü
    if st.session_state.tr_mode == "menu":
        st.markdown('<div class="roza-card">', unsafe_allow_html=True)
        st.markdown("### 📌 Bölüm Seç")
        st.button("📗 Eş Anlamlı", use_container_width=True, on_click=lambda: _go_mode("syn"))
        st.button("📙 Zıt Anlamlı", use_container_width=True, on_click=lambda: _go_mode("ant"))
        st.markdown("</div>", unsafe_allow_html=True)
        return

    # Geri bildirim
    if st.session_state.tr_msg:
        kind, text = st.session_state.tr_msg
        if kind == "success":
            st.success(text)
        else:
            st.info(text)
        st.session_state.tr_msg = None

    # Soru ekranı
    item = st.session_state.tr_item
    if item is None:
        _new_question()
        item = st.session_state.tr_item

    st.markdown(
        f"""
        <div class="roza-card" style="text-align:center;">
            <h3>{item["prompt"]}: <span class="roza-accent">{item["base"]}</span></h3>
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
                key=f"tr_{item['mode']}_{score}_{i}",
                on_click=lambda x=val: _answer(x)
            )

    st.button("⬅️ Bölüm Seçimine Dön", use_container_width=True, on_click=lambda: _go_mode("menu"))
