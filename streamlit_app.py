import streamlit as st

# Fungsi untuk menambahkan background dan memperjelas font
def add_background():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://tribratanews.polri.go.id/web/image/blog.post/61345/image");
            background-attachment: fixed;
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            color: #000000; /* warna teks */
        }

        /* Ubah warna dan ukuran font di seluruh halaman */
        html, body, [class*="css"] {
            color: #000000;
            font-size: 18px;
            font-weight: 500;
        }

        /* Untuk komponen judul */
        h1, h2, h3, h4 {
            color: #000000;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Halaman 1: Pengertian Karbohidrat
def halaman_pengertian():
    add_background()
    st.title("Pengertian Karbohidrat 🍚")
    st.markdown("""
    **Karbohidrat** adalah salah satu jenis zat gizi yang berfungsi sebagai sumber energi utama bagi tubuh. Karbohidrat dapat ditemukan dalam berbagai jenis makanan, terutama yang berasal dari tanaman, seperti beras 🍚, gandum 🌾, kentang 🥔, jagung 🌽, dan buah-buahan 🍎.

    Karbohidrat dibagi menjadi dua jenis utama, yaitu:
    1. **Karbohidrat sederhana**: Cepat dicerna dan meningkatkan kadar gula darah dengan cepat. Contohnya adalah gula 🍬, madu 🍯, dan sirup.
    2. **Karbohidrat kompleks**: Dicerna lebih lambat dan memberikan energi yang bertahan lebih lama. Contohnya nasi 🍚, roti gandum 🍞, kentang 🥔, dan pasta 🍝.

    **Fungsi Karbohidrat**:
    - Sumber utama energi ⚡
    - Membantu fungsi otak 🧠 dan saraf
    - Menyediakan serat 🌾 untuk pencernaan

    **Kebutuhan Karbohidrat Harian**:
    Tergantung usia, jenis kelamin, berat badan, tinggi badan, dan tingkat aktivitas.
    """)

# Halaman 2: Kalkulator Kebutuhan Karbohidrat
def halaman_kalkulator():
    add_background()
    st.title("Kalkulator Kebutuhan Karbohidrat Harian 🍽️")
    
    usia = st.number_input("Masukkan usia (tahun):", min_value=1, max_value=120, value=30)
    berat_badan = st.number_input("Masukkan berat badan (kg):", min_value=30, max_value=200, value=70)
    tinggi_badan = st.number_input("Masukkan tinggi badan (cm):", min_value=100, max_value=250, value=170)
    jenis_kelamin = st.selectbox("Pilih jenis kelamin:", ["Pria", "Wanita"])
    tingkat_aktivitas = st.selectbox(
        "Tingkat aktivitas fisik:",
        ["Rendah (tidak aktif)", "Sedang (olahraga ringan)", "Tinggi (olahraga intensif)"]
    )
    
    if jenis_kelamin == "Pria":
        bmr = 88.362 + (13.397 * berat_badan) + (4.799 * tinggi_badan) - (5.677 * usia)
    else:
        bmr = 447.593 + (9.247 * berat_badan) + (3.098 * tinggi_badan) - (4.330 * usia)
    
    if tingkat_aktivitas == "Rendah (tidak aktif)":
        tdee = bmr * 1.2
    elif tingkat_aktivitas == "Sedang (olahraga ringan)":
        tdee = bmr * 1.55
    else:
        tdee = bmr * 1.9
    
    kebutuhan_karbohidrat_kalori = tdee * 0.55
    kebutuhan_karbohidrat_gram = kebutuhan_karbohidrat_kalori / 4
    
    st.subheader("Kebutuhan Karbohidrat Harian Anda:")
    st.write(f"Kebutuhan kalori harian: **{tdee:.2f} kalori**")
    st.write(f"Kebutuhan karbohidrat: **{kebutuhan_karbohidrat_gram:.2f} gram per hari**")
    
    st.subheader("Saran Makanan Harian 🍴")
    st.write(f"Untuk memenuhi {kebutuhan_karbohidrat_gram:.2f} gram karbohidrat, Anda bisa mengonsumsi:")
    st.markdown("""
    1. **Nasi putih (100g)** 🍚: 28g karbohidrat  
    2. **Roti gandum (30g)** 🍞: 15g karbohidrat  
    3. **Kentang rebus (100g)** 🥔: 17g karbohidrat  
    4. **Pasta (100g)** 🍝: 25g karbohidrat  
    5. **Oatmeal (240g)** 🥣: 27g karbohidrat  
    6. **Pisang (1 buah sedang)** 🍌: 25g karbohidrat  
    """)

# Halaman 3: Tentang Kelompok
def halaman_tentang_kelompok():
    add_background()
    st.title("Tentang Kelompok 👥")
    
    st.subheader("👨‍👩‍👧‍👦 KELOMPOK 10:")
    st.write("Kelompok 10 - Kalkulator Kebutuhan Karbohidrat Harian")

    st.subheader("📋 Anggota Kelompok:")
    st.markdown("""
    1. **Afiqah Siva Chandra-2420564**  
    2. **Erina Astriningtyas-2420594**  
    3. **Muhammad Ridho Meidioputra-2420625**  
    4. **Putri Paramita-2420641**  
    5. **Zahra Aliya Chairunnisa-2420681**
    """)

    st.subheader("🖼️ Foto Kelompok:")
    
    # Upload gambar
    uploaded_image = st.file_uploader("Unggah foto kelompok atau anggota:", type=["jpg", "jpeg", "png"])
    if uploaded_image is not None:
        st.image(uploaded_image, caption="Foto Kelompok", use_column_width=True)
    
    # Tampilkan gambar dari URL jika ingin
    st.markdown("Atau gambar dari URL:")
    st.image("blob:https://web.whatsapp.com/829beba0-a7cc-4d9a-a20a-71f20c6dddec,blob:https://web.whatsapp.com/c900d45e-f32b-422e-91ad-42a0d70ff9f7", caption="foto kelompok", use_column_width=True)

# Menu Navigasi
def main():
    st.sidebar.title("Menu")
    pilihan = st.sidebar.radio("Pilih Halaman", ["Pengertian Karbohidrat", "Kalkulator Karbohidrat", "Tentang Kelompok"])
    
    if pilihan == "Pengertian Karbohidrat":
        halaman_pengertian()
    elif pilihan == "Kalkulator Karbohidrat":
        halaman_kalkulator()
    elif pilihan == "Tentang Kelompok":
        halaman_tentang_kelompok()

if __name__ == "__main__":
    main()
