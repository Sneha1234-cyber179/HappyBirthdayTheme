import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Happy Birthday Thejas Srivatsa 🎂",
    page_icon="🎂",
    layout="wide"
)

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>

body{
    margin:0;
    overflow:hidden;
    background:linear-gradient(-45deg,#ffe6f2,#fff0f5,#ffd1dc,#ffe4e1);
    background-size:400% 400%;
    animation:bg 10s ease infinite;
    font-family:Arial,sans-serif;
}

@keyframes bg{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

.title{
    text-align:center;
    margin-top:20px;
}

.title h1{
    color:#ff1493;
    font-size:70px;
    margin:0;
    animation:pulse 2s infinite;
}

.title h2{
    color:#ff1493;
    font-size:50px;
    margin-top:10px;
}

@keyframes pulse{
    50%{transform:scale(1.08);}
}

.float{
    position:absolute;
    animation:rise linear infinite;
}

@keyframes rise{
    from{
        transform:translateY(100vh);
        opacity:0;
    }
    20%{
        opacity:1;
    }
    to{
        transform:translateY(-100px);
        opacity:0;
    }
}

.gift{
    position:absolute;
    font-size:70px;
    animation:pop 1s forwards;
}

@keyframes pop{
    0%{
        transform:scale(0);
    }
    50%{
        transform:scale(1.8);
    }
    100%{
        transform:scale(1);
    }
}

.msg{
    position:absolute;
    background:white;
    border-radius:20px;
    padding:15px 25px;
    font-size:22px;
    font-weight:bold;
    color:#ff1493;
    box-shadow:0 0 20px pink;
    animation:floatmsg 3s forwards;
}

@keyframes floatmsg{
    0%{
        opacity:0;
        transform:translateY(50px);
    }
    20%{
        opacity:1;
    }
    100%{
        opacity:0;
        transform:translateY(-250px);
    }
}

</style>
</head>

<body>

<div class="title">
    <h1>🎂 Happy Birthday My Dear 🎂</h1>
    <h2>💖 Thejas Srivatsa 💖</h2>
</div>

<script>

const messages = [
"💖 You make every day brighter!",
"🌹 Wishing you endless happiness!",
"🥰 Stay blessed and smiling always!",
"✨ May all your dreams come true!",
"💕 You are loved more than words can say!",
"🎂 May this birthday be unforgettable!",
"💝 You deserve all the happiness in the world!",
"🌟 Shine brighter than every star!",
"🎉 Success follows you everywhere!",
"💌 Sending you a sky full of love!",
"❤️ You make hearts smile!",
"🎈 May this year be magical!",
"🌺 Stay happy and blessed!",
"💎 You are one of a kind!",
"🎁 Surprise! More happiness is coming!",
"🌈 Your future is beautiful!",
"🥳 Celebrate every moment!",
"💕 Endless love for you!",
"🎊 Joy is waiting around every corner!",
"🎉 Happy Birthday Thejas!"
];

const icons = ["💖","💕","💝","❤️","🌹","🎁","🎈","🎀","✨","🎊","🎉"];

function floatingItems(){
    let item=document.createElement("div");

    item.className="float";
    item.innerHTML=icons[Math.floor(Math.random()*icons.length)];

    item.style.left=Math.random()*100+"vw";
    item.style.fontSize=(25+Math.random()*35)+"px";
    item.style.animationDuration=(5+Math.random()*5)+"s";

    document.body.appendChild(item);

    setTimeout(()=>item.remove(),10000);
}

setInterval(floatingItems,200);

let i=0;

function giftBlast(){

    let left=Math.random()*80+10;
    let top=Math.random()*65+15;

    let gift=document.createElement("div");
    gift.className="gift";
    gift.innerHTML="🎁";

    gift.style.left=left+"vw";
    gift.style.top=top+"vh";

    document.body.appendChild(gift);

    setTimeout(()=>{

        gift.innerHTML="💥";

        setTimeout(()=>{

            gift.remove();

            let msg=document.createElement("div");
            msg.className="msg";
            msg.innerHTML=messages[i];

            msg.style.left=left+"vw";
            msg.style.top=top+"vh";

            document.body.appendChild(msg);

            setTimeout(()=>msg.remove(),3000);

            i=(i+1)%messages.length;

        },400);

    },1000);
}

setInterval(giftBlast,3500);

</script>

</body>
</html>
"""

components.html(html_code, height=900, scrolling=False)
