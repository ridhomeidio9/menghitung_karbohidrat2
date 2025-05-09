import streamlit as st

# Halaman 1: Pengertian Karbohidrat
def halaman_pengertian():
    st.title("Pengertian Karbohidrat")
    st.markdown("""
    **Karbohidrat** adalah salah satu jenis zat gizi yang berfungsi sebagai sumber energi utama bagi tubuh. Karbohidrat dapat ditemukan dalam berbagai jenis makanan, terutama yang berasal dari tanaman, seperti beras, gandum, kentang, jagung, dan buah-buahan.

    Karbohidrat dibagi menjadi dua jenis utama, yaitu:
    1. **Karbohidrat sederhana**: Ini adalah karbohidrat yang cepat dicerna tubuh dan dapat meningkatkan kadar gula darah dengan cepat. Contohnya adalah gula, madu, dan sirup.
    2. **Karbohidrat kompleks**: Ini adalah karbohidrat yang lebih lambat dicerna tubuh dan memberikan energi yang bertahan lebih lama. Contohnya adalah nasi, roti gandum, kentang, dan pasta.

    **Fungsi Karbohidrat**:
    - Sebagai sumber utama energi untuk tubuh.
    - Membantu fungsi otak dan sistem saraf.
    - Menyediakan serat yang mendukung pencernaan.

    **Kebutuhan Karbohidrat Harian**:
    Kebutuhan karbohidrat setiap orang berbeda, tergantung pada faktor seperti usia, jenis kelamin, berat badan, tinggi badan, dan tingkat aktivitas fisik. Oleh karena itu, sangat penting untuk menghitung kebutuhan karbohidrat secara tepat.
    """)

# Halaman 2: Kalkulator Kebutuhan Karbohidrat
def halaman_kalkulator():
    st.title("Kalkulator Kebutuhan Karbohidrat Harian")
    
    # Input Data Pengguna
    usia = st.number_input("Masukkan usia (tahun):", min_value=1, max_value=120, value=30)
    berat_badan = st.number_input("Masukkan berat badan (kg):", min_value=30, max_value=200, value=70)
    tinggi_badan = st.number_input("Masukkan tinggi badan (cm):", min_value=100, max_value=250, value=170)
    tingkat_aktivitas = st.selectbox(
        "Tingkat aktivitas fisik:",
        ["Rendah (tidak aktif)", "Sedang (olahraga ringan)", "Tinggi (olahraga intensif)"]
    )
    
    # Menghitung kebutuhan karbohidrat (menyesuaikan dengan faktor aktivitas)
    if tingkat_aktivitas == "Rendah (tidak aktif)":
        faktor_aktivitas = 30  # gram karbohidrat per kg berat badan
    elif tingkat_aktivitas == "Sedang (olahraga ringan)":
        faktor_aktivitas = 40
    else:
        faktor_aktivitas = 50
    
    # Menghitung kebutuhan karbohidrat berdasarkan berat badan
    kebutuhan_karbohidrat = berat_badan * faktor_aktivitas
    
    # Menampilkan hasil perhitungan
    st.subheader(f"Kebutuhan Karbohidrat Harian Anda:")
    st.write(f"Berdasarkan berat badan Anda yang {berat_badan} kg, tinggi badan {tinggi_badan} cm, "
             f"usia {usia} tahun, dan tingkat aktivitas {tingkat_aktivitas}, "
             f"Anda membutuhkan sekitar **{kebutuhan_karbohidrat} gram karbohidrat per hari**.")
    
    # Saran Makanan untuk Memenuhi Kebutuhan Karbohidrat
    st.subheader("Saran Makanan untuk Memenuhi Kebutuhan Karbohidrat Harian")
    st.write(f"Untuk memenuhi kebutuhan karbohidrat harian sebesar {kebutuhan_karbohidrat} gram, Anda dapat mengonsumsi beberapa makanan berikut:")
    st.write("""
    1. **Nasi putih (1 porsi, 100 gram)**: 28 gram karbohidrat
    2. **Roti gandum (1 potong, 30 gram)**: 15 gram karbohidrat
    3. **Kentang rebus (100 gram)**: 17 gram karbohidrat
    4. **Pasta (100 gram)**: 25 gram karbohidrat
    5. **Oatmeal (1 cangkir, 240 gram)**: 27 gram karbohidrat
    6. **Buah-buahan (misalnya pisang, 1 buah ukuran sedang)**: 25 gram karbohidrat
    
    Cobalah untuk mengonsumsi makanan ini secara teratur, sambil memperhatikan variasi dan keseimbangan gizi lainnya.
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

