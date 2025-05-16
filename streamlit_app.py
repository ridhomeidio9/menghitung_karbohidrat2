import streamlit as st

# Fungsi untuk menambahkan background dan Google Font
def add_background():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Poppins', sans-serif;
            background-image: url("https://doktersehat.com/wp-content/uploads/2019/10/karbohidrat-doktersehat.jpg");
            background-size: cover;
            background-attachment: fixed;
            color: #ffffff;
            font-size: 18px;
        }

        .stApp {
            background-color: rgba(0, 0, 0, 0.6);
            padding: 1rem;
            border-radius: 10px;
        }

        h1, h2, h3, .stTitle {
            color: #ffffff;
            text-shadow: 2px 2px 4px #000000;
        }

        .css-1d391kg, .css-ffhzg2 {
            background-color: rgba(0, 0, 0, 0.6) !important;
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

# Menu Navigasi
def main():
    st.sidebar.title("Menu")
    pilihan = st.sidebar.radio("Pilih Halaman", ["Pengertian Karbohidrat", "Kalkulator Karbohidrat"])
    
    if pilihan == "Pengertian Karbohidrat":
        halaman_pengertian()
    elif pilihan == "Kalkulator Karbohidrat":
        halaman_kalkulator()

if __name__ == "__main__":
    main()
