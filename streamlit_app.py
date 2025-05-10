import streamlit as st
import base64

# Fungsi untuk menambahkan background dari file lokal
def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Halaman 1: Pengertian Karbohidrat
def halaman_pengertian():
    st.title("Pengertian Karbohidrat 🍚")
    st.markdown("""
    **Karbohidrat** adalah salah satu jenis zat gizi yang berfungsi sebagai sumber energi utama bagi tubuh. Karbohidrat dapat ditemukan dalam berbagai jenis makanan, terutama yang berasal dari tanaman, seperti beras 🍚, gandum 🌾, kentang 🥔, jagung 🌽, dan buah-buahan 🍎.

    Karbohidrat dibagi menjadi dua jenis utama, yaitu:
    1. **Karbohidrat sederhana**: cepat dicerna dan meningkatkan kadar gula darah dengan cepat. Contoh: gula 🍬, madu 🍯, dan sirup.
    2. **Karbohidrat kompleks**: dicerna lebih lambat dan memberikan energi lebih tahan lama. Contoh: nasi 🍚, roti gandum 🍞, kentang 🥔, pasta 🍝.

    **Fungsi Karbohidrat**:
    - Sumber utama energi ⚡
    - Mendukung fungsi otak 🧠 dan sistem saraf
    - Menyediakan serat 🌾 untuk pencernaan

    **Kebutuhan Harian**:
    Tergantung usia, jenis kelamin, berat, tinggi, dan aktivitas. Penting untuk menghitungnya secara akurat.
    """)

# Halaman 2: Kalkulator Kebutuhan Karbohidrat
def halaman_kalkulator():
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
    st.write(f"Total kalori harian: **{tdee:.2f} kalori**")
    st.write(f"Kebutuhan karbohidrat: **{kebutuhan_karbohidrat_gram:.2f} gram/hari**")
    
    st.subheader("Saran Makanan 🍴")
    st.write(f"""
    1. Nasi putih (100g): 28g karbohidrat🍚  
    2. Roti gandum (30g): 15g karbohidrat🍞  
    3. Kentang rebus (100g): 17g karbohidrat🥔  
    4. Pasta (100g): 25g karbohidrat🍝  
    5. Oatmeal (240g): 27g karbohirat🥣  
    6. Pisang (1 buah): 25g karbohidrat🍌  
    """)

# Main
def main():
    set_background("/mnt/data/0454753b-d9a3-433d-9f79-71241f3741f6.jpg")
    st.sidebar.title("Menu")
    pilihan = st.sidebar.radio("Pilih Halaman", ["Pengertian Karbohidrat", "Kalkulator Karbohidrat"])
    
    if pilihan == "Pengertian Karbohidrat":
        halaman_pengertian()
    elif pilihan == "Kalkulator Karbohidrat":
        halaman_kalkulator()

if __name__ == "__main__":
    main()
