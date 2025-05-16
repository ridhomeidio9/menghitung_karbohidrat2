import streamlit as st
import plotly.graph_objects as go

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
    **Karbohidrat** adalah salah satu dari tiga makronutrien utama selain protein dan lemak yang sangat dibutuhkan tubuh. Karbohidrat berfungsi sebagai **sumber energi utama** karena mudah diubah menjadi glukosa (gula darah), yang digunakan oleh sel-sel tubuh untuk beraktivitas.

    ### 🧬 Struktur Kimia
    Karbohidrat terdiri dari karbon (C), hidrogen (H), dan oksigen (O) dengan rumus umum \( (CH_2O)_n \). Berdasarkan strukturnya, karbohidrat dibagi menjadi:
    - **Monosakarida**: gula sederhana seperti glukosa, fruktosa
    - **Disakarida**: dua molekul gula, misalnya sukrosa (gula pasir)
    - **Polisakarida**: rantai panjang, seperti pati dan serat

    ### 🍽️ Jenis-Jenis Karbohidrat
    1. **Karbohidrat Sederhana**:
       - Cepat dicerna & cepat meningkatkan gula darah
       - Contoh: gula putih, kue manis, minuman bersoda

    2. **Karbohidrat Kompleks**:
       - Dicerna perlahan, mengandung serat tinggi
       - Contoh: nasi merah, roti gandum, ubi, kacang-kacangan

    ### 💡 Fungsi Karbohidrat
    - Memberikan energi instan ⚡
    - Membantu metabolisme lemak
    - Membantu fungsi otak dan sistem saraf 🧠
    - Mengandung serat untuk pencernaan 🌾

    ### 🛑 Dampak Kekurangan Karbohidrat
    - Tubuh menjadi lemas
    - Penurunan konsentrasi
    - Potensi gangguan pencernaan

    ### ⚠️ Dampak Kelebihan Karbohidrat
    - Peningkatan berat badan
    - Risiko diabetes tipe 2
    - Kadar gula darah tidak stabil

    ### ✅ Tips Memilih Karbohidrat Sehat
    - Pilih makanan tinggi serat
    - Kurangi makanan olahan
    - Perhatikan indeks glikemik
    - Kombinasikan dengan protein & lemak sehat

    > "Karbohidrat bukan musuh, tapi sahabat energi jika dikonsumsi dengan bijak."

    ---    
    """)

    st.subheader("📊 Perbandingan Karbohidrat Sederhana vs Kompleks")

    fig = go.Figure(data=[
        go.Bar(name='Karbohidrat Sederhana', x=['Cepat Dicerna', 'Gula Darah Naik Cepat', 'Serat Rendah'], y=[10, 9, 3], marker_color='crimson'),
        go.Bar(name='Karbohidrat Kompleks', x=['Cepat Dicerna', 'Gula Darah Naik Cepat', 'Serat Rendah'], y=[4, 3, 10], marker_color='limegreen')
    ])
    fig.update_layout(barmode='group', title="Karakteristik Karbohidrat", xaxis_title="Fitur", yaxis_title="Skala (1–10)")
    st.plotly_chart(fig)

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
    st.write(f"Total kebutuhan kalori: **{tdee:.2f} kalori**")
    st.write(f"Kebutuhan karbohidrat: **{karbo_gram:.2f} gram/hari**")

# Halaman 3: Kelompok & Dokumentasi
def halaman_kelompok_dokumentasi():
    add_background()
    st.title("👥 Kelompok & 📸 Dokumentasi")

    st.subheader("Judul Proyek")
    st.write("*Aplikasi Edukasi dan Kalkulasi Kebutuhan Karbohidrat*")

    st.subheader("Anggota Kelompok:")
    st.markdown("""
    1. Aulia Rahmawati  
    2. Budi Santoso  
    3. Citra Lestari  
    4. Dimas Pratama  
    5. Eka Nurhaliza  
    """)

    st.subheader("📸 Dokumentasi Proyek")
    st.markdown("""
    Proses pembuatan aplikasi ini dilakukan melalui:
    - Pengumpulan informasi tentang karbohidrat
    - Desain UI/UX
    - Pengembangan kalkulator interaktif
    - Review dan evaluasi hasil
    """)

    uploaded_file = st.file_uploader("Unggah Gambar Dokumentasi", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption="Dokumentasi Proyek", use_column_width=True)

# Navigasi
def main():
    st.sidebar.title("🍽️ Edukasi Karbohidrat")
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
