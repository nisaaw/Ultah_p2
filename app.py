import streamlit as st
import time

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
# CSS TEMA PINK
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
st.markdown("# 🎀✨ SELAMAT ULANG TAHUN ✨🎀")
st.markdown("## 💖 Spesial Untuk Kamu 💖")

# =========================
# STEP 0 — MULAI
# =========================
if st.session_state.step == 0:
    if st.button("🎁 Mulai Kejutan 🎁"):
        st.session_state.step = 1

# =========================
# STEP 1 — UCAPAN PANJANG
# =========================
if st.session_state.step == 1:
    with st.spinner("Menyiapkan sesuatu yang spesial... 💗"):
        time.sleep(2)

    st.balloons()

    st.markdown("""
🌸 **Selamat ulang tahun yaaa** 🌸  

Hari ini bukan cuma tentang bertambahnya usia,  
tapi tentang semua proses yang sudah kamu lewati.  

Tentang kuat yang kadang kamu ragukan,  
tentang lelah yang sering kamu simpan sendiri,  
dan tentang senyum yang tetap kamu usahakan.  

Aku harap di umur baru ini,  
hatimu lebih tenang,  
langkahmu lebih yakin,  
dan kamu selalu ingat…  
**kamu berharga** 💗
""")

    if st.button("💌 Lanjut"):
        st.session_state.step = 2

# =========================
# STEP 2 — KLIK + VIDEO KEJUTAN
# =========================
if st.session_state.step == 2:
    st.markdown("## 💗 Klik Sampai Terbuka 💗")
    st.markdown("Setiap klik ada kejutan kecil 😆")

    if st.button("💗 Klik aku"):
        st.session_state.clicks += 1

    st.write(f"Klik: {st.session_state.clicks} / 7")
    st.progress(min(st.session_state.clicks / 7, 1.0))

    # 🎥 VIDEO KEJUTAN (MUNCUL SETIAP KLIK)
    if st.session_state.clicks >= 1:
        st.video("https://youtu.be/TDMf9sHhEYw")

    if st.session_state.clicks >= 7:
        st.balloons()
        st.success("🎉 KAMU BERHASIL 🎉")

        if st.button("🎬 Buka Kejutan Terakhir"):
            st.session_state.step = 3

# =========================
# STEP 3 — VIDEO PENUTUP
# =========================
if st.session_state.step == 3:
    st.markdown("## 🎉 Kejutan Terakhir 🎉")

    st.markdown("""
💗 you shine like a star 💗  

Terima kasih sudah sabar sampai sejauh ini.  
Video ini adalah penutup kecil  
yang semoga bikin kamu senyum hari ini ✨
""")

    # 🎬 VIDEO PENUTUP
    st.video("https://youtu.be/2_F6Oi9QnLM")

    st.markdown("""
🎂 Selamat ulang tahun 🎂  

Semoga hari-harimu ke depan  
selalu dipenuhi hal baik dan orang-orang yang tulus 💕
""")

    st.balloons()

# =========================
# FOOTER
# =========================
st.markdown("<br><p>Made with 💕 | Birthday Web Surprise 🎀</p>", unsafe_allow_html=True)
