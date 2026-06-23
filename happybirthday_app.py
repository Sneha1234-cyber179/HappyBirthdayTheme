import streamlit as st
import time
import random

messages = [
    "💖 You make every day brighter!",
    "🌹 Wishing you endless happiness!",
    "🥰 Stay blessed and smiling always!",
    "✨ May all your dreams come true!",
    "🎉 Success follows you everywhere!",
    "💝 You deserve all the happiness!",
    "🎂 Enjoy your special day!",
    "🌟 Shine brighter than the stars!",
    "💕 Lots of love for you today!",
    "🎁 May surprises fill your life!",
    "💌 You are truly amazing!",
    "🥳 Celebrate every moment!",
    "💖 Keep spreading joy!",
    "🌈 May your future be colorful!",
    "🎊 Happiness is waiting for you!",
    "💎 You are one of a kind!",
    "❤️ Sending you endless love!",
    "🎈 May this year be magical!",
    "🌺 Wishing you peace and joy!",
    "🎉 Happy Birthday, Thejas!"
]

st.markdown("""
<style>

.popup {
    animation: flyIn 1.2s ease-out;
    text-align:center;
    font-size:35px;
    font-weight:bold;
    padding:30px;
    margin-top:40px;
    border-radius:25px;
    background:rgba(255,255,255,0.9);
    box-shadow:0 0 30px rgba(255,105,180,0.5);
}

@keyframes flyIn {
    0% {
        transform: translateY(300px) scale(0.1) rotate(-20deg);
        opacity:0;
    }
    50% {
        transform: translateY(-20px) scale(1.1);
    }
    100% {
        transform: translateY(0px) scale(1);
        opacity:1;
    }
}

.float-heart {
    position: fixed;
    font-size: 50px;
    animation: floatUp 6s linear infinite;
}

@keyframes floatUp {
    0% {
        transform: translateY(100vh);
        opacity:0;
    }
    20% {
        opacity:1;
    }
    100% {
        transform: translateY(-100px);
        opacity:0;
    }
}

</style>
""", unsafe_allow_html=True)

# Floating hearts and gifts
for i in range(15):
    left = random.randint(0, 90)
    emoji = random.choice(["💖", "💕", "💝", "🎁", "🎀", "❤️"])
    st.markdown(
        f"""
        <div class="float-heart"
             style="left:{left}%; animation-delay:{i*0.4}s;">
             {emoji}
        </div>
        """,
        unsafe_allow_html=True
    )

placeholder = st.empty()

for msg in messages:
    emoji = random.choice(["💖", "💕", "💝", "🎁", "🎀", "❤️", "🌹"])

    placeholder.markdown(
        f"""
        <div class="popup">
            {emoji}<br><br>
            {msg}
        </div>
        """,
        unsafe_allow_html=True
    )

    time.sleep(3)

st.balloons()

st.markdown("""
<h1 style='text-align:center;
           color:#ff1493;
           font-size:70px;'>
🎂 Happy Birthday My Dear<br>
Thejas Srivatsa 💖
</h1>
""", unsafe_allow_html=True)
