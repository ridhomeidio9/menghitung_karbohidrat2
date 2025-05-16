import streamlit as st

# Fungsi untuk menambahkan background
def add_background():
    st.markdown(
        """
        <style>
        /* Background untuk seluruh halaman */
        .stApp {
            background: linear-gradient(to right, #e0f7fa, #fff3e0);
            background-size: cover;
        }

        /* Opsional: untuk membuat konten lebih transparan */
        .css-18e3th9 {
            background-color: rgba(255, 255, 255, 0.8);
            padding: 2rem;
            border-radius: 10px;
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
    add_background()
    st.title("Kalkulator Kebutuhan Karbohidrat Harian 🍽️")
    
    usia = st.number_input("Masukkan usia (tahun):", min_value=1, max_value=120, value=30)
    berat_badan = st.number_input("Masukkan berat badan (kg):", min_value=30, max_value=2
