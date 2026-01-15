import streamlit as st
import time
import os

# =========================
# INIT SESSION STATE
# =========================
if "step" not in st.session_state:
    st.session_state.step = 0

if "clicks" not in st.session_state:
    st.session_state.clicks = 0

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="🎀 Birthday Surprise 🎀",
    page_icon="🎂",
    layout="centered"
)

# =========================
# CSS PINK
# =========================
st.markdown("""
<style>
body { background-color: #ffe6f0; }
h1, h2, h3 { color: #ff4d88; text-align: center; }
p { color: #ff6699; font-size: 18px; text-align: center; }
.stButton > button {
    background-color: #ff80bf;
    color: white;
    border-radius: 25px;
    height: 3em;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# JUDUL
# =========================
st.markdown("# 🎀✨ SELAMAT ULANG TAHUN SAYANG ✨🎀")
st.markdown("## 💖 Spesial For You 💖")

# =========================
# MUSIK
# =========================
music_path = "birthday.mp3"
if os.path.exists(music_path):
    with open(music_path, "rb") as audio:
        st.audio(audio.read(), format="audio/mp3", loop=True)

# =========================
# STEP 0 – MULAI
# =========================
if st.session_state.step == 0:
    if st.button("🎁 Mulai Kejutan 🎁"):
        st.session_state.step = 1

# =========================
# STEP 1 – UCAPAN PANJANG
# =========================
if st.session_state.step == 1:
    with st.spinner("Menyiapkan kata-kata manis... 💗"):
        time.sleep(2)

    st.balloons()

    st.markdown("""
🌸 **Selamat ulang tahun yaaa** 🌸  

Happy birthday to a superstar ✨  

Today is your day, your happiest day ever.  
May happiness bloom in your heart all year long.  
Thank you for your hard work, your kindness, and your love.  

I'll always be by your side.  
Be yourself, be happy, and keep shining 💕

Selamat bertambah satu angka sayang 💗
""")

    if st.button("💌 Lanjut ke kejutan berikutnya 💌"):
        st.session_state.step = 2

# =========================
# STEP 2 – CLICK TO UNLOCK
# =========================
if st.session_state.step == 2:
    st.markdown("## 💗 Klik Sampai Terbuka 💗")

    if st.button("💗 Klik aku terus"):
        st.session_state.clicks += 1

    st.write(f"Klik: {st.session_state.clicks} / 7")
    st.progress(min(st.session_state.clicks / 7, 1.0))

    if st.session_state.clicks >= 7:
        st.balloons()
        st.success("🎉 BERHASIL! 🎉")

        if st.button("🎬 Buka Kejutan Terakhir"):
            st.session_state.step = 3

# =========================
# STEP 3 – VIDEO PERTAMA
# =========================
if st.session_state.step == 3:
    st.markdown("## 🎉 Kejutan Pertama 🎉")

    st.markdown("""
💗 you shine like a star 💗  

Terima kasih sudah sabar sampai di sini.  
Masih ada satu kejutan lagi buat kamu ✨
""")

    st.video("https://youtu.be/TDMf9sHhEYw")

    st.balloons()

    if st.button("💖 Lihat Kejutan Terakhir"):
        st.session_state.step = 4

# =========================
# STEP 4 – VIDEO PENUTUP (GANTI TEKA-TEKI)
# =========================
if st.session_state.step == 4:
    st.markdown("## 💖 Video Terakhir Buat Kamu 💖")

    st.markdown("""
Aku nggak mau ini berakhir tanpa bilang satu hal penting…  

Terima kasih sudah menjadi kamu,  
dengan semua kelebihan dan kekuranganmu.  

Video ini adalah penutup kecil,  
tapi rasa sayangnya besar 💗
""")

    # 🔴 GANTI LINK VIDEO KEDUA DI SINI
    st.video("https://www.youtube.com/watch?v=VIDEO_ID_KEDUA")

    st.balloons()

    st.markdown("""
🎂 **Selamat ulang tahun** 🎂  

Semoga kamu selalu bahagia,  
dan semua doa baik pelan-pelan jadi nyata 💕
""")

# =========================
# FOOTER
# =========================
st.markdown("<br><p>Made with 💕 | Tepung Sasha Serbaguna Kaya Vitamin 🎀</p>", unsafe_allow_html=True)
