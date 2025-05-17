import streamlit as st

# Fungsi untuk menambahkan font & background
def add_background():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        html, body, [class*="css"] {
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
    **Karbohidrat** adalah zat gizi makro yang berperan sebagai sumber energi utama bagi tubuh manusia. Hampir semua aktivitas tubuh, termasuk fungsi otak, otot, dan organ internal, membutuhkan karbohidrat dalam bentuk glukosa sebagai bahan bakar utama.

    ### 🧬 Struktur Kimia
    Karbohidrat tersusun dari atom karbon (C), hidrogen (H), dan oksigen (O). Tiga golongan utama:
    - **Monosakarida**: Glukosa, fruktosa
    - **Disakarida**: Sukrosa (gula meja), laktosa
    - **Polisakarida**: Pati, selulosa

    ### 🍽️ Jenis Karbohidrat
    1. **Sederhana**: Cepat dicerna, meningkatkan gula darah dengan cepat
       - Contoh: Gula, madu, permen
    2. **Kompleks**: Mengandung serat, dicerna perlahan
       - Contoh: Nasi merah, oat, jagung, ubi, roti gandum

    ### 💡 Fungsi Karbohidrat
    - Sumber energi cepat ⚡
    - Menjaga keseimbangan metabolik
    - Mendukung sistem saraf pusat
    - Membantu fungsi otak 🧠
    - Mengandung serat untuk pencernaan 🌾

    ### 🛑 Kekurangan Karbohidrat
    - Lemas, pusing
    - Gangguan pencernaan
    - Ketosis (jika ekstrem)

    ### ⚠️ Kelebihan Karbohidrat
    - Kenaikan berat badan
    - Risiko diabetes tipe 2
    - Fluktuasi energi

    > Karbohidrat bukan musuh, tapi sahabat jika dikonsumsi dengan bijak.
    """)

# Halaman 2: Kalkulator Karbohidrat
def halaman_kalkulator():
    add_background()
    st.title("Kalkulator Kebutuhan Karbohidrat Harian 🍽️")

    usia = st.number_input("Usia (tahun):", 1, 120, 25)
    berat = st.number_input("Berat badan (kg):", 30, 200, 60)
    tinggi = st.number_input("Tinggi badan (cm):", 100, 250, 170)
    kelamin = st.selectbox("Jenis Kelamin", ["Pria", "Wanita"])
    aktivitas = st.selectbox("Tingkat Aktivitas", ["Rendah", "Sedang", "Tinggi"])

    # Hitung BMR
    if kelamin == "Pria":
        bmr = 88.362 + (13.397 * berat) + (4.799 * tinggi) - (5.677 * usia)
    else:
        bmr = 447.593 + (9.247 * berat) + (3.098 * tinggi) - (4.330 * usia)

    # Hitung TDEE
    tdee = bmr * (1.2 if aktivitas == "Rendah" else 1.55 if aktivitas == "Sedang" else 1.9)
    karbo_kalori = tdee * 0.55
    karbo_gram = karbo_kalori / 4

    st.subheader("Hasil Perhitungan")
    st.markdown(f"""
    <div style='color: #90EE90; font-size: 20px;'>
        ✅ Total kebutuhan kalori: <strong>{tdee:.2f} kalori</strong><br>
        ✅ Kebutuhan karbohidrat: <strong>{karbo_gram:.2f} gram/hari</strong>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🍴 Saran Makanan untuk Memenuhi Kebutuhan Karbohidrat")
    st.markdown("""
    <div style="background-color: white; color: black; padding: 15px; border-radius: 10px;">
    Berikut ini adalah beberapa makanan sumber karbohidrat beserta kandungannya:

    <table>
    <tr><th>Makanan</th><th>Karbohidrat (gram) per porsi</th></tr>
    <tr><td>Nasi putih (1 centong = 100g)</td><td>28g</td></tr>
    <tr><td>Roti gandum utuh (1 lembar)</td><td>15g</td></tr>
    <tr><td>Kentang rebus (100g)</td><td>17g</td></tr>
    <tr><td>Pasta matang (100g)</td><td>25g</td></tr>
    <tr><td>Oatmeal (1 mangkuk = 240g)</td><td>27g</td></tr>
    <tr><td>Pisang sedang (1 buah)</td><td>25g</td></tr>
    <tr><td>Jagung rebus (1 tongkol = 100g)</td><td>19g</td></tr>
    <tr><td>Ubi jalar rebus (100g)</td><td>20g</td></tr>
    <tr><td>Apel sedang (1 buah)</td><td>20g</td></tr>
    <tr><td>Kacang merah matang (100g)</td><td>21g</td></tr>
    </table>

    <br>
    💡 <strong>Tips:</strong> Gabungkan beberapa makanan di atas untuk memenuhi total kebutuhan harianmu!
    </div>
    """, unsafe_allow_html=True)

# Halaman 3: Kelompok & Dokumentasi
def halaman_kelompok_dokumentasi():
    add_background()
    st.title("👥 Kelompok & 📸 Dokumentasi")

    st.subheader("KELOMPOK 10")
    st.write("*Kalkulator Kebutuhan Karbohidrat Harian*")

    st.subheader("Anggota Kelompok 10:")
    st.markdown("""
    <ul style="line-height: 1.8;">
        <li><strong>Afiqah Siva Chandra</strong> - 2420564</li>
        <li><strong>Erina Astriningtyas</strong> - 2420594</li>
        <li><strong>Muhammad Ridho Meidioputra</strong> - 2420625</li>
        <li><strong>Putri Paramita</strong> - 2420641</li>
        <li><strong>Zahra Aliya Chairunnisa</strong> - 2420681</li>
    </ul>
    """, unsafe_allow_html=True)

    st.subheader("📸 Dokumentasi Proyek")
    st.markdown("""
    Proses pembuatan aplikasi ini dilakukan melalui:
    - Pengumpulan informasi ilmiah tentang karbohidrat
    - Perancangan tampilan
    - Pembuatan kalkulator menggunakan Streamlit
    - Pengujian fungsionalitas dan tampilan
    """)
    
    # Pakai gambar dari URL yang valid
    st.image(""C:\Users\User\Downloads\WhatsApp Image 2025-05-09 at 16.25.36.jpeg"", caption="Dokumentasi Proyek", use_column_width=True)

# Menu Navigasi
def main():
    st.sidebar.title("🍽️ Kebutuhan Karbohidrat Harian")
    pilihan = st.sidebar.radio("Pilih Halaman:", [
        "Pengertian Karbohidrat", 
        "Kalkulator Karbohidrat", 
        "Kelompok & Dokumentasi"
    ])

    if pilihan == "Pengertian Karbohidrat":
        halaman_pengertian()
    elif pilihan == "Kalkulator Karbohidrat":
        halaman_kalkulator()
    elif pilihan == "Kelompok & Dokumentasi":
        halaman_kelompok_dokumentasi()

if __name__ == "__main__":
    main()
