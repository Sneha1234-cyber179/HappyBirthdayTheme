import streamlit as st
import time

st.set_page_config(
    page_title="Happy Birthday Thejas Srivatsa 🎂",
    page_icon="🎂",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: #ff1493;
    text-shadow: 3px 3px 10px #ffb6c1;
}

.card {
    text-align: center;
    padding: 30px;
    border-radius: 20px;
    font-size: 28px;
    font-weight: bold;
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    margin-top: 20px;
    box-shadow: 0px 0px 20px rgba(255,0,100,0.3);
}

.gift {
    text-align: center;
    padding: 30px;
    border-radius: 20px;
    font-size: 28px;
    font-weight: bold;
    background: linear-gradient(135deg, #a18cd1, #fbc2eb);
    margin-top: 20px;
    box-shadow: 0px 0px 20px rgba(100,0,255,0.3);
}
</style>
""", unsafe_allow_html=True)

# Balloons
st.balloons()

# Main Birthday Message
st.markdown(
    """
    <div class="main-title">
        🎂 Happy Birthday My Dear <br>
        Thejas Srivatsa 💖
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br><br>", unsafe_allow_html=True)

# Placeholder for popups
placeholder = st.empty()

surprises = [
    ('card', '💌 Love Card #1<br>❤️ You make every day brighter ❤️'),
    ('gift', '🎁 Gift Box #1 Opened!<br>✨ A year full of happiness ✨'),
    ('card', '💖 Love Card #2<br>🌹 Wishing you endless smiles 🌹'),
    ('gift', '🎁 Gift Box #2 Opened!<br>🎉 Lots of success ahead 🎉'),
    ('card', '💕 Love Card #3<br>🥰 Stay happy and blessed always 🥰'),
    ('gift', '🎁 Final Gift Box 🎁<br>💎 A lifetime of joy and love 💎')
]

for kind, message in surprises:
    if kind == "card":
        placeholder.markdown(
            f'<div class="card">{message}</div>',
            unsafe_allow_html=True
        )
    else:
        placeholder.markdown(
            f'<div class="gift">{message}</div>',
            unsafe_allow_html=True
        )

    time.sleep(2)

st.snow()

st.markdown("""
<div style='text-align:center; font-size:35px; font-weight:bold; color:#ff1493;'>
🎉🥳 Happy Birthday Thejas Srivatsa 🥳🎉
</div>
""", unsafe_allow_html=True)
