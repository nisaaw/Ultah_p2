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
st.markdown("## 💖 Spesial pake karet 2 💖")

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
    if st.button("🎁 Sudah Siap? 🎁"):
        st.session_state.step = 1

# =========================
# STEP 1 – UCAPAN PANJANG
# =========================
if st.session_state.step == 1:
    with st.spinner("Sedang Memasak Mohon Bersabar... 💗"):
        time.sleep(2)

    st.balloons()

    st.markdown("""
🌸 **Selamat ulang tahun yaaa** 🌸  

Happy birthday to my favorite boy ✨  

Today is your day, your happiest day ever, today you're one year older
may happiness bloom in your heart all year long, may ur every wish come true, 
thank you for being a part of my life <3 thank you for always being my source of happiness, 
thank you for your hard work, thank you for always share a positive words and smile to people around you. 
I hope your special day will surrounded by happiness, blessed with love, brightened with fun.

I'll always be by your side.  
Be yourself, be happy, and keep shining 💕

Selamat bertambah satu angka sayang 💗
""")

    if st.button("💌 Lanjut ke Tahap ke 2 💌"):
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

        if st.button("🎬 Buka Tahap ke 3"):
            st.session_state.step = 3

# =========================
# STEP 3 – VIDEO PERTAMA
# =========================
if st.session_state.step == 3:
    st.markdown("## 🎉 apa hayo? 🎉")

    st.markdown("""
💗 you shine like a star 💗  

good job! beneran di klik sampe 7 kali

kamu penasaran kan? Eh... tapi tunggu dulu
video nya?..tonton aja deh, udah nonton? HAHAH maaf yaa,
soalnya lucuu liat kamu kepeleset terus✨
""")

    st.video("https://youtu.be/TDMf9sHhEYw")

    st.balloons()

    if st.button("💖 Apa lagi ini ya ?"):
        st.session_state.step = 4

# =========================
# STEP 4 – VIDEO PENUTUP (GANTI TEKA-TEKI)
# =========================
if st.session_state.step == 4:
    st.markdown("## 💖 video apa lagi?? 💖")

    st.markdown("""
Aku nggak mau ini berakhir tapi capeee ngodingnya..hehe bercanda :)

Terima kasih sudah menjadi kamu,  
dengan semua kelebihan dan kekuranganmu.  

Video ini adalah penutup kecil dari akuu,  
 Ooh iya ada pesan dari sari sama siti, katanya Happy Milad Barakallahu Fii Umrik 💗
 okeyy segitu dulu ajaa, babayy!💕
""")

    # 🔴 GANTI LINK VIDEO KEDUA DI SINI
    st.video("https://youtu.be/2_F6Oi9QnLM")

    st.balloons()

    st.markdown("""
🎂 **Selamat ulang tahun yaa broow ** 🎂  

""")

# =========================
# FOOTER
# =========================
st.markdown("<br><p>Made with 💕 | Tepung Sasha Serbaguna Kaya Vitamin 🎀</p>", unsafe_allow_html=True)
