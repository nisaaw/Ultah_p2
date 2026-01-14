import streamlit as st
import time

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="🎀 Happy Birthday 🎀",
    page_icon="🎂",
    layout="centered"
)

# =========================
# CSS TEMA PINK
# =========================
st.markdown("""
<style>
body {
    background-color: #ffe6f0;
}
.main {
    background-color: #ffe6f0;
}
h1, h2, h3 {
    color: #ff4d88;
    text-align: center;
}
p {
    color: #ff6699;
    font-size: 18px;
    text-align: center;
}
.stButton > button {
    background-color: #ff80bf;
    color: white;
    border-radius: 20px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
.stButton > button:hover {
    background-color: #ff4d94;
}
</style>
""", unsafe_allow_html=True)

# =========================
# JUDUL
# =========================
st.markdown("## 🎀✨ BESOK ULANG TAHUN NIH ✨🎀")
st.markdown("### 💖 Special Pink Birthday Page 💖")

# =========================
# MUSIK
# =========================
st.markdown("🎵 **Putar musik dulu biar makin vibes~** 🎵")
audio_file = open("music/birthday.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3", loop=True)

# =========================
# PESAN ANIMASI
# =========================
if st.button("🎂 Klik untuk kejutan 🎂"):
    with st.spinner("Menyiapkan kejutan imut... 🧸🎀"):
        time.sleep(2)

    st.balloons()

    st.markdown("""
    ## 🎉 HAPPY BIRTHDAY 🎉  
    💗💗💗
    """)

    st.markdown("""
    🌸 Semoga di umur yang baru ini 🌸  

    ✨ kamu selalu dikelilingi hal-hal baik  
    ✨ langkahmu dimudahkan  
    ✨ hatimu selalu tenang  
    ✨ dan senyummu nggak pernah hilang  

    🎀 Jangan lupa…  
    kamu itu **berharga**,  
    **cukup**,  
    dan **pantas bahagia** 💕

    🎂💐✨
    """)

    st.markdown("### 💕 Have a lovely birthday & a sweeter life 💕")

# =========================
# FOOTER
# =========================
st.markdown("""
<br><br>
<p>Made with 💖 | Pink Birthday App 🎀</p>
""", unsafe_allow_html=True)
