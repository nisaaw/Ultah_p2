import streamlit as st
import time
import os

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
st.markdown("# 🎀✨ SELAMAT ULANG TAHUN SAYANG ✨🎀")
st.markdown("## 💖 Pink Birthday Surprise 💖")

# =========================
# MUSIK
# =========================
st.markdown("### 🎵 Musik Ulang Tahun 🎵")

music_path = "music/birthday.mp3"

if os.path.exists(music_path):
    with open(music_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3", loop=True)
else:
    st.warning("🎵 File musik belum ditemukan. Pastikan ada di folder music!")

# =========================
# TOMBOL KEJUTAN
# =========================
if st.button("🎂 Klik untuk Kejutan Imut 🎂"):
    with st.spinner("Menyiapkan kejutan pink... 🎀"):
        time.sleep(2)

    st.balloons()

    st.markdown("## 🎉 HAPPY BIRTHDAY 🎉")
    st.markdown("""
    💕💗💖

    🌸 Semoga di umur yang baru ini 🌸  
    ✨ langkahmu selalu dimudahkan  
    ✨ hatimu selalu tenang  
    ✨ rezekimu dilancarkan  
    ✨ dan senyummu nggak pernah hilang  

    🎀 Ingat ya…  
    kamu itu **berharga**,  
    **cukup**,  
    dan **pantas bahagia** 💗  

    🎂💐✨
    """)

    st.markdown("### 💖 Semoga harimu semanis warna pink 💖")

# =========================
# FOOTER
# =========================
st.markdown("""
<br><br>
<p>Made with 💕 | Pink Birthday App 🎀</p>
""", unsafe_allow_html=True)
