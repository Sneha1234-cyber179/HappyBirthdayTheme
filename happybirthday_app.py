import streamlit as st

st.set_page_config(
    page_title="Happy Birthday Thejas Srivatsa 🎂",
    page_icon="🎂",
    layout="centered"
)

st.balloons()

st.markdown("""
<style>

.crystal-title{
    text-align:center;
    font-size:65px;
    font-weight:900;
    color:#ff69b4;
    text-shadow:
        0 0 5px #ffffff,
        0 0 10px #ffb6c1,
        0 0 20px #ff69b4,
        0 0 40px #ff1493;
    animation: glow 2s infinite alternate;
    margin-bottom:10px;
}

@keyframes glow{
    from{
        text-shadow:
            0 0 5px #ffffff,
            0 0 10px #ffb6c1,
            0 0 20px #ff69b4;
    }
    to{
        text-shadow:
            0 0 10px #ffffff,
            0 0 20px #ffb6c1,
            0 0 40px #ff69b4,
            0 0 70px #ff1493;
    }
}

.hearts{
    text-align:center;
    font-size:38px;
    animation:pulse 1.2s infinite;
}

@keyframes pulse{
    0%{
        transform:scale(1);
    }
    50%{
        transform:scale(1.25);
    }
    100%{
        transform:scale(1);
    }
}

.message-box{
    text-align:center;
    padding:10px;
}

.name{
    color:#ff1493;
    font-size:38px;
    font-weight:bold;
}

.wish{
    font-size:24px;
    line-height:1.8;
}

.footer{
    font-size:42px;
}

</style>

<div class="message-box">

<div class="hearts">
💖 💕 💗 💞 💘 💝 💘 💞 💗 💕 💖
</div>

<div class="crystal-title">
🎂 Happy Birthday 🎂
</div>

<div class="hearts">
💖 💕 💗 💞 💘 💝 💘 💞 💗 💕 💖
</div>

<br>

<div class="name">
💖 My Dear Thejas Srivatsa 💖
</div>

<br>

<div style="font-size:32px;">
🎈🎈🎈🎈🎈<br>
💖💖💖💖💖<br>
😘😘😘😘😘
</div>

<br>

<div class="wish">
❤️ Wishing you a day filled with happiness, laughter, and love! ❤️
<br><br>
🌟 May all your dreams come true. 🌟
<br><br>
🎁 Have an amazing year ahead! 🎁
<br><br>
💕 With lots of love 💕
</div>

<br>

<div style="font-size:36px;">
🎉🥳🎂❤️🎈🎁✨💖🌹🎊
</div>

<br>

<div class="name">
🎂❤️ Happy Birthday, Thejas Srivatsa! ❤️🎂
</div>

<br>

<div class="footer">
💋 💖 🎁 💝 🎀 💐 💘
</div>

</div>
""", unsafe_allow_html=True)

st.snow()
