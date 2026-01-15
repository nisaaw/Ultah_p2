import streamlit as st
import time
import os

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="🎀 Birthday Surprise 🎀",
    page_icon="🎂",
    layout="centered"
)

# =========================
# CSS PINK LUCU
# =========================
st.markdown("""
<style>
body {
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
    border-radius: 25px;
    height: 3em;
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
st.markdown("## 💖 Spesial For You 💖")

# =========================
# MUSIK
# =========================
music_path = "birthday.mp3"
if os.path.exists(music_path):
    with open(music_path, "rb") as audio:
        st.audio(audio.read(), format="audio/mp3", loop=True)
else:
    st.info("🎵 Upload musik ke folder music/birthday.mp3")

# =========================
# STEP 1 – TOMBOL AWAL
# =========================
if "step" not in st.session_state:
    st.session_state.step = 0

if st.session_state.step == 0:
    if st.button("🎁 Mulai Kejutan 🎁"):
        st.session_state.step = 1

# =========================
# STEP 2 – UCAPAN PANJANG
# =========================
if st.session_state.step == 1:
    with st.spinner("Menyiapkan kata-kata manis... 💗"):
        time.sleep(2)

    st.balloons()

    st.markdown("""
🌸 **Selamat ulang tahun yaaa** 🌸  

Happy birthday to a superstar ✨

Today is your day! your happiest day ever, today you're one year older.
may happiness bloom in your heart all year long, may ur every wish come true.
Thank you for always being my source of happiness, thank you for your hard work.
i hope your special day will surrounded by happines, blessed with love, brightened with fun.
I'll always by your side. I wish the best for you, be better and just be yourself!

Selamat bertambah satu angka sayangg💕
""")

    if st.button("💌 Lanjut ke kejutan berikutnya 💌"):
        st.session_state.step = 2

# =========================
# STEP 3 – KEJUTAN EMOJI
# =========================
if "clicks" not in st.session_state.step:
    st.session_state.clicks = 0

if st.button("💗 Klik aku terus"):
    st.session_state.clicks += 1

st.write(f"Klik: {st.session_state.clicks}")

if st.session_state.clicks == 7:
    st.balloons()
    st.success("🎉 KEJUTAN TERBUKA 🎉")
    st.write("Selamat ulang tahun! Kamu sabar banget 💕")

    if st.button("✨ Klik aku ✨"):
        st.balloons()
        st.markdown("✨ 🎀 💕 🎂 💕 🎀 ✨")
        st.success("💖 ke ciamis bareng mamat selamat hari kamis buat kamu yang paling manis 💖")

    if st.button("🧠 Lanjut ke Teka-Teki 🧠"):
        st.session_state.step = 3

# =========================
# STEP 4 – TEKA-TEKI
# =========================
if st.session_state.step == 3:
    st.markdown("## 🧠 Teka-Teki Ulang Tahun 🎂")
    st.markdown("""
Aku selalu datang setahun sekali,  
aku tidak bisa dihindari,  
tapi selalu ditunggu.  

❓ **Siapakah aku?**
""")

    jawaban = st.text_input("Jawaban kamu:")

    if jawaban:
        if jawaban.lower() in ["ulang tahun", "birthday", "hari ulang tahun"]:
            st.success("🎉 BENAR! 🎉")
            st.balloons()
            st.markdown("""
💖 you shine like a star 💖  

Terima kasih sudah bertahan sejauh ini,  
sudah belajar, tumbuh, dan menjadi versi dirimu yang sekarang.  

🎂 Selamat ulang tahun 🎂✨
""")
        else:
            st.warning("🤏 Hampir benar, coba pikirkan lagi ya sayang~")

# =========================
# FOOTER
# =========================
st.markdown("<br><p>Made with 💕 | Tepung Sasha Serbaguna Kaya Vitamin 🎀</p>", unsafe_allow_html=True)
