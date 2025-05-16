import streamlit as st

# Tambahkan background dan font
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

        h1, h2, h3 {
            color: #ffffff;
            text-shadow: 1px 1px 3px #000000;
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
    **Karbohidrat** adalah salah satu jenis zat gizi makro yang berfungsi sebagai sumber energi utama bagi tubuh. Karbohidrat dapat ditemukan dalam berbagai jenis makanan, terutama yang berasal dari tanaman seperti beras 🍚, gandum 🌾, kentang 🥔, jagung 🌽, dan buah-buahan 🍎.

    ### Jenis Karbohidrat:
    1. **Karbohidrat sederhana**: Cepat dicerna dan meningkatkan kadar gula darah dengan cepat. Contoh: gula 🍬, madu 🍯, sirup.
    2. **Karbohidrat kompleks**: Dicerna lebih lambat dan memberikan energi yang bertahan lebih lama. Contoh: nasi 🍚, roti gandum 🍞, kentang 🥔, pasta 🍝.

    ### Struktur Kimia Karbohidrat:
    - **Monosakarida**: Glukosa, fruktosa, galaktosa.
    - **Disakarida**: Sukrosa, laktosa, maltosa.
    - **Polisakarida**: Pati, glikogen, selulosa.

    ### Fungsi Karbohidrat:
    - Sumber utama energi ⚡
    - Menjaga fungsi otak 🧠 dan sistem saraf
    - Menyediakan serat 🌾 untuk kesehatan pencernaan
    - Mengatur metabolisme protein dan lemak

    ### Proses Pencernaan:
    Karbohidrat dicerna menjadi glukosa oleh enzim, diserap oleh usus halus, dan digunakan tubuh sebagai energi atau disimpan sebagai glikogen di hati dan otot.

    ### Contoh Makanan Sumber Karbohidrat:
    - **Alami**: Beras, ubi, jagung, pisang, apel, oat
    - **Olahan**: Roti, mi, pasta, sereal, biskuit

    ### Risiko Kekurangan & Kelebihan:
    - Kekurangan: Lemas, penurunan fokus, ketosis
    - Kelebihan: Obesitas, diabetes tipe 2, karies gigi

    > Kebutuhan karbohidrat ideal: sekitar **45–65% dari total kalori harian**
    """)

# Halaman 2: Kalkulator Karbohidrat
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
    
    # Hitung BMR
    if jenis_kelamin == "Pria":
        bmr = 88.362 + (13.397 * berat_badan) + (4.799 * tinggi_badan) - (5.677 * usia)
    else:
        bmr = 447.593 + (9.247 * berat_badan) + (3.098 * tinggi_badan) - (4.330 * usia)
    
    # Hitung TDEE
    if tingkat_aktivitas == "Rendah (tidak aktif)":
        tdee = bmr * 1.2
    elif tingkat_aktivitas == "Sedang (olahraga ringan)":
        tdee = bmr * 1.55
    else:
        tdee = bmr * 1.9
    
    # Hitung kebutuhan karbohidrat
    kebutuhan_karbohidrat_kalori = tdee * 0.55
    kebutuhan_karbohidrat_gram = kebutuhan_karbohidrat_kalori / 4
    
    st.subheader("Kebutuhan Karbohidrat Harian Anda:")
    st.write(f"Kebutuhan kalori harian: **{tdee:.2f} kalori**")
    st.write(f"Kebutuhan karbohidrat: **{kebutuhan_karbohidrat_gram:.2f} gram per hari**")
    
    st.subheader("Saran Makanan Harian 🍴")
    st.markdown(f"""
    Untuk memenuhi sekitar **{kebutuhan_karbohidrat_gram:.2f} gram** karbohidrat, Anda bisa konsumsi:

    1. **Nasi putih (100g)** 🍚: 28g  
    2. **Roti gandum (30g)** 🍞: 15g  
    3. **Kentang rebus (100g)** 🥔: 17g  
    4. **Pasta (100g)** 🍝: 25g  
    5. **Oatmeal (240g)** 🥣: 27g  
    6. **Pisang sedang (1 buah)** 🍌: 25g  
    """)

# Menu Utama
def main():
    st.sidebar.title("Menu")
    pilihan = st.sidebar.radio("Pilih Halaman", ["Pengertian Karbohidrat", "Kalkulator Karbohidrat"])
    
    if pilihan == "Pengertian Karbohidrat":
        halaman_pengertian()
    elif pilihan == "Kalkulator Karbohidrat":
        halaman_kalkulator()

if __name__ == "__main__":
    main()
