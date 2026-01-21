import random
import streamlit as st

TARGET_SCORE = 100
POINT = 10


def _init_state():
    if "math_score" not in st.session_state:
        st.session_state.math_score = 0
    if "math_q" not in st.session_state:
        st.session_state.math_q = None
    if "math_choices" not in st.session_state:
        st.session_state.math_choices = []
    if "math_answer" not in st.session_state:
        st.session_state.math_answer = None
    if "math_msg" not in st.session_state:
        st.session_state.math_msg = None


def _new_question():
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    answer = a * b

    wrong = set()
    while len(wrong) < 3:
        delta = random.choice([-10, -5, -3, -2, -1, 1, 2, 3, 5, 10])
        cand = answer + delta
        if cand > 0 and cand != answer:
            wrong.add(cand)

    choices = list(wrong) + [answer]
    random.shuffle(choices)

    st.session_state.math_q = (a, b)
    st.session_state.math_answer = answer
    st.session_state.math_choices = choices


def _answer(choice: int):
    if choice == st.session_state.math_answer:
        st.session_state.math_score += POINT
        st.session_state.math_msg = ("success", "AFERİM LAN!! ⭐ Doğru bildin!")
        st.balloons()
    else:
        # Yanlışta 10 puan düş, 0'ın altına inmesin
        st.session_state.math_score = max(
            0, st.session_state.math_score - POINT
        )
        st.session_state.math_msg = ("info", "KERİZİM 😊 Bir daha deneyelim!")

    _new_question()
    st.rerun()


def _reset_game():
    st.session_state.math_score = 0
    st.session_state.math_msg = None
    _new_question()
    st.rerun()


def render(go_menu):
    _init_state()
    if st.session_state.math_q is None:
        _new_question()

    score = st.session_state.math_score

    # 🎉 100 PUAN KUTLAMA
    if score >= TARGET_SCORE:
        st.markdown(
            """
            <div class="roza-hero" style="text-align:center;">
                <h1>🎉 HARİKASIN ASLAN KIZIM ROZA! 🎉</h1>
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
                <p class="roza-small">
                    İstersen tekrar oynayabilir ya da menüye dönebilirsin.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.button("🔁 Baştan Oyna", use_container_width=True, on_click=_reset_game)
        st.button("🏠 Ana Menü", use_container_width=True, on_click=lambda: go_menu("menu"))
        return

    a, b = st.session_state.math_q

    # ÜST BAŞLIK
    st.markdown(
        """
        <div class="roza-hero">
            <h1>🧮 Çarpma Oyunu</h1>
            <p class="roza-small">Doğru seçeneğe dokun! 🌟</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # PUAN + BUTONLAR
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
        st.button("🔄 Yeni Soru", use_container_width=True, on_click=lambda: (_new_question(), st.rerun()))

    # GERİ BİLDİRİM
    if st.session_state.math_msg:
        kind, text = st.session_state.math_msg
        if kind == "success":
            st.success(text)
        else:
            st.info(text)
        st.session_state.math_msg = None

    # SORU
    st.markdown(
        f"""
        <div class="roza-card" style="text-align:center;">
            <h2>{a} × {b} = ?</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ŞIKLAR (2x2, büyük)
    c1, c2 = st.columns(2)
    for i, val in enumerate(st.session_state.math_choices):
        col = c1 if i % 2 == 0 else c2
        with col:
            st.button(
                str(val),
                use_container_width=True,
                key=f"math_{score}_{i}",
                on_click=lambda x=val: _answer(x)
            )
