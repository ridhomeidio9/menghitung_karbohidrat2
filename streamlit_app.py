import streamlit as st

# Tambahkan CSS untuk background
page_bg_img = """
<style>
body {
background-image: url("import streamlit as st

# Tambahkan CSS untuk background
page_bg_img = """
<style>
body {
background-image: url("https://www.google.com/url?sa=i&url=https%3A%2F%2Fdoktersehat.com%2Fgaya-hidup%2Fgizi-dan-nutrisi%2Fkarbohidrat%2F&psig=AOvVaw28mSJZ48O7S989_f6e5ddx&ust=1747468453287000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCICMj77Bp40DFQAAAAAdAAAAABAE");
background-size: cover;
background-repeat: no-repeat;
background-attachment: fixed;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Halaman 1: Pengertian Karbohidrat
def halaman_pengertian():
    st.title("Pengertian Karbohidrat 🍚")
    st.markdown("""
    **Karbohidrat** adalah salah satu jenis zat gizi yang berfungsi sebagai sumber energi utama bagi tubuh. Karbohidrat dapat ditemukan dalam berbagai jenis makanan, terutama yang berasal dari tanaman, seperti beras 🍚, gandum 🌾, kentang 🥔, jagung 🌽, dan buah-buahan 🍎.

    Karbohidrat dibagi menjadi dua jenis utama, yaitu:
    1. **Karbohidrat sederhana**: Ini adalah karbohidrat yang cepat dicerna tubuh dan dapat meningkatkan kadar gula darah dengan cepat. Contohnya adalah gula 🍬, madu 🍯, dan sirup.
    2. **Karbohidrat kompleks**: Ini adalah karbohidrat yang lebih lambat dicerna tubuh dan memberikan energi yang bertahan lebih lama. Contohnya adalah nasi 🍚, roti gandum 🍞, kentang 🥔, dan pasta 🍝.

    **Fungsi Karbohidrat**:
    - Sebagai sumber utama energi ⚡ untuk tubuh.
    - Membantu fungsi otak 🧠 dan sistem saraf.
    - Menyediakan serat 🌾 yang mendukung pencernaan.

    **Kebutuhan Karbohidrat Harian**:
    Kebutuhan karbohidrat setiap orang berbeda, tergantung pada faktor seperti usia, jenis kelamin, berat badan, tinggi badan, dan tingkat aktivitas fisik. Oleh karena itu, sangat penting untuk menghitung kebutuhan karbohidrat secara tepat.
    """)

# Halaman 2: Kalkulator Kebutuhan Karbohidrat
def halaman_kalkulator():
    st.title("Kalkulator Kebutuhan Karbohidrat Harian 🍽️")
    
    # Input Data Pengguna
    usia = st.number_input("Masukkan usia (tahun):", min_value=1, max_value=120, value=30)
    berat_badan = st.number_input("Masukkan berat badan (kg):", min_value=30, max_value=200, value=70)
    tinggi_badan = st.number_input("Masukkan tinggi badan (cm):", min_value=100, max_value=250, value=170)
    jenis_kelamin = st.selectbox("Pilih jenis kelamin:", ["Pria", "Wanita"])
    tingkat_aktivitas = st.selectbox(
        "Tingkat aktivitas fisik:",
        ["Rendah (tidak aktif)", "Sedang (olahraga ringan)", "Tinggi (olahraga intensif)"]
    )
    
    # Menghitung BMR (Basal Metabolic Rate)
    if jenis_kelamin == "Pria":
        bmr = 88.362 + (13.397 * berat_badan) + (4.799 * tinggi_badan) - (5.677 * usia)
    else:
        bmr = 447.593 + (9.247 * berat_badan) + (3.098 * tinggi_badan) - (4.330 * usia)
    
    # Menghitung TDEE (Total Daily Energy Expenditure)
    if tingkat_aktivitas == "Rendah (tidak aktif)":
        tdee = bmr * 1.2
    elif tingkat_aktivitas == "Sedang (olahraga ringan)":
        tdee = bmr * 1.55
    else:
        tdee = bmr * 1.9
    
    # Menghitung kebutuhan karbohidrat (sekitar 55% dari total kalori)
    kebutuhan_karbohidrat_kalori = tdee * 0.55
    kebutuhan_karbohidrat_gram = kebutuhan_karbohidrat_kalori / 4  # 1 gram karbohidrat = 4 kalori
    
    # Menampilkan hasil perhitungan
    st.subheader(f"Kebutuhan Karbohidrat Harian Anda:")
    st.write(f"Berdasarkan informasi yang Anda berikan, kebutuhan kalori harian Anda sekitar **{tdee:.2f} kalori**.")
    st.write(f"Dengan asumsi karbohidrat menyumbang 55% dari total kalori, kebutuhan karbohidrat Anda adalah sekitar **{kebutuhan_karbohidrat_gram:.2f} gram per hari**.")
    
    # Saran Makanan untuk Memenuhi Kebutuhan Karbohidrat
    st.subheader("Saran Makanan untuk Memenuhi Kebutuhan Karbohidrat Harian 🍴")
    st.write(f"Untuk memenuhi kebutuhan karbohidrat harian sebesar {kebutuhan_karbohidrat_gram:.2f} gram, Anda dapat mengonsumsi beberapa makanan berikut:")
    st.write("""
    1. **Nasi putih (1 porsi, 100 gram)** 🍚: 28 gram karbohidrat  
    2. **Roti gandum (1 potong, 30 gram)** 🍞: 15 gram karbohidrat  
    3. **Kentang rebus (100 gram)** 🥔: 17 gram karbohidrat  
    4. **Pasta (100 gram)** 🍝: 25 gram karbohidrat  
    5. **Oatmeal (1 cangkir, 240 gram)** 🥣: 27 gram karbohidrat  
    6. **Buah-buahan (misalnya pisang, 1 buah ukuran sedang)** 🍌: 25 gram karbohidrat  
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
    main()");
background-size: cover;
background-repeat: no-repeat;
background-attachment: fixed;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Halaman 1: Pengertian Karbohidrat
def halaman_pengertian():
    st.title("Pengertian Karbohidrat 🍚")
    st.markdown("""
    **Karbohidrat** adalah salah satu jenis zat gizi yang berfungsi sebagai sumber energi utama bagi tubuh. Karbohidrat dapat ditemukan dalam berbagai jenis makanan, terutama yang berasal dari tanaman, seperti beras 🍚, gandum 🌾, kentang 🥔, jagung 🌽, dan buah-buahan 🍎.

    Karbohidrat dibagi menjadi dua jenis utama, yaitu:
    1. **Karbohidrat sederhana**: Ini adalah karbohidrat yang cepat dicerna tubuh dan dapat meningkatkan kadar gula darah dengan cepat. Contohnya adalah gula 🍬, madu 🍯, dan sirup.
    2. **Karbohidrat kompleks**: Ini adalah karbohidrat yang lebih lambat dicerna tubuh dan memberikan energi yang bertahan lebih lama. Contohnya adalah nasi 🍚, roti gandum 🍞, kentang 🥔, dan pasta 🍝.

    **Fungsi Karbohidrat**:
    - Sebagai sumber utama energi ⚡ untuk tubuh.
    - Membantu fungsi otak 🧠 dan sistem saraf.
    - Menyediakan serat 🌾 yang mendukung pencernaan.

    **Kebutuhan Karbohidrat Harian**:
    Kebutuhan karbohidrat setiap orang berbeda, tergantung pada faktor seperti usia, jenis kelamin, berat badan, tinggi badan, dan tingkat aktivitas fisik. Oleh karena itu, sangat penting untuk menghitung kebutuhan karbohidrat secara tepat.
    """)

# Halaman 2: Kalkulator Kebutuhan Karbohidrat
def halaman_kalkulator():
    st.title("Kalkulator Kebutuhan Karbohidrat Harian 🍽️")
    
    # Input Data Pengguna
    usia = st.number_input("Masukkan usia (tahun):", min_value=1, max_value=120, value=30)
    berat_badan = st.number_input("Masukkan berat badan (kg):", min_value=30, max_value=200, value=70)
    tinggi_badan = st.number_input("Masukkan tinggi badan (cm):", min_value=100, max_value=250, value=170)
    jenis_kelamin = st.selectbox("Pilih jenis kelamin:", ["Pria", "Wanita"])
    tingkat_aktivitas = st.selectbox(
        "Tingkat aktivitas fisik:",
        ["Rendah (tidak aktif)", "Sedang (olahraga ringan)", "Tinggi (olahraga intensif)"]
    )
    
    # Menghitung BMR (Basal Metabolic Rate)
    if jenis_kelamin == "Pria":
        bmr = 88.362 + (13.397 * berat_badan) + (4.799 * tinggi_badan) - (5.677 * usia)
    else:
        bmr = 447.593 + (9.247 * berat_badan) + (3.098 * tinggi_badan) - (4.330 * usia)
    
    # Menghitung TDEE (Total Daily Energy Expenditure)
    if tingkat_aktivitas == "Rendah (tidak aktif)":
        tdee = bmr * 1.2
    elif tingkat_aktivitas == "Sedang (olahraga ringan)":
        tdee = bmr * 1.55
    else:
        tdee = bmr * 1.9
    
    # Menghitung kebutuhan karbohidrat (sekitar 55% dari total kalori)
    kebutuhan_karbohidrat_kalori = tdee * 0.55
    kebutuhan_karbohidrat_gram = kebutuhan_karbohidrat_kalori / 4  # 1 gram karbohidrat = 4 kalori
    
    # Menampilkan hasil perhitungan
    st.subheader(f"Kebutuhan Karbohidrat Harian Anda:")
    st.write(f"Berdasarkan informasi yang Anda berikan, kebutuhan kalori harian Anda sekitar **{tdee:.2f} kalori**.")
    st.write(f"Dengan asumsi karbohidrat menyumbang 55% dari total kalori, kebutuhan karbohidrat Anda adalah sekitar **{kebutuhan_karbohidrat_gram:.2f} gram per hari**.")
    
    # Saran Makanan untuk Memenuhi Kebutuhan Karbohidrat
    st.subheader("Saran Makanan untuk Memenuhi Kebutuhan Karbohidrat Harian 🍴")
    st.write(f"Untuk memenuhi kebutuhan karbohidrat harian sebesar {kebutuhan_karbohidrat_gram:.2f} gram, Anda dapat mengonsumsi beberapa makanan berikut:")
    st.write("""
    1. **Nasi putih (1 porsi, 100 gram)** 🍚: 28 gram karbohidrat  
    2. **Roti gandum (1 potong, 30 gram)** 🍞: 15 gram karbohidrat  
    3. **Kentang rebus (100 gram)** 🥔: 17 gram karbohidrat  
    4. **Pasta (100 gram)** 🍝: 25 gram karbohidrat  
    5. **Oatmeal (1 cangkir, 240 gram)** 🥣: 27 gram karbohidrat  
    6. **Buah-buahan (misalnya pisang, 1 buah ukuran sedang)** 🍌: 25 gram karbohidrat  
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
