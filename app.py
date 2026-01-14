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
st.markdown("# 🎀✨ BESOK ULANG TAHUN NIH ✨🎀")
st.markdown("## 💖 Pink Interactive Birthday Page 💖")

# =========================
# MUSIK
# =========================
music_path = "music/birthday.mp3"
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
🌸 **Selamat bertambah usia** 🌸  

Hari ini bukan cuma tentang bertambahnya angka,  
tapi tentang semua proses yang sudah kamu lewati.  

Tentang lelah yang kamu simpan sendiri,  
tentang kuat yang kadang kamu ragukan,  
dan tentang senyum yang tetap kamu usahakan.  

✨ Semoga di umur baru ini:
- hatimu lebih tenang  
- langkahmu lebih yakin  
- mimpimu perlahan jadi nyata  
- dan kamu selalu dikelilingi orang baik  

🎀 Jangan pernah lupa…  
kamu itu cukup, berharga, dan pantas bahagia 💕
""")

    if st.button("💌 Lanjut ke kejutan berikutnya 💌"):
        st.session_state.step = 2

# =========================
# STEP 3 – KEJUTAN EMOJI
# =========================
if st.session_state.step == 2:
    st.markdown("## 🎉 KEJUTAN KECIL 🎉")
    st.markdown("Klik tombol di bawah ya 👇")

    if st.button("✨ Klik aku ✨"):
        st.snow()
        st.success("💖 Kamu berhasil membuka kejutan rahasia 💖")

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
💖 Karena hari ini adalah tentangmu 💖  

Terima kasih sudah bertahan sejauh ini,  
sudah belajar, tumbuh, dan menjadi versi dirimu yang sekarang.  

🎂 Selamat ulang tahun 🎂  
Semoga bahagiamu selalu lebih besar dari sedihmu ✨
""")
        else:
            st.warning("🤏 Hampir benar… coba pikirkan lagi ya~")

# =========================
# FOOTER
# =========================
st.markdown("<br><p>Made with 💕 | Interactive Birthday App 🎀</p>", unsafe_allow_html=True)
