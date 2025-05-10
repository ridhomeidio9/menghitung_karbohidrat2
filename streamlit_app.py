import streamlit as st
import base64

# Fungsi untuk menyisipkan background dari gambar lokal
def set_background(image_path):
    with open(image_path, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
        css = f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)

# Halaman 1: Pengertian Karbohidrat
def halaman_pengertian():
    st.title("Pengertian Karbohidrat 🍚")
    st.markdown("""
    **Karbohidrat** adalah salah satu jenis zat gizi yang berfungsi sebagai sumber energi utama bagi tubuh...

    (konten lainnya tetap seperti sebelumnya)
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
    
    kebutuhan_kalori = tdee * 0.55
    kebutuhan_karbo = kebutuhan_kalori / 4
    
    st.subheader("Kebutuhan Karbohidrat Harian Anda:")
    st.write(f"Total kebutuhan kalori: **{tdee:.2f} kalori**")
    st.write(f"Kebutuhan karbohidrat (55%): **{kebutuhan_karbo:.2f} gram/hari**")

# Fungsi utama
def main():
    set_background("C:/Users/User/Downloads/karbohidrat-doktersehat.jpg")
    st.sidebar.title("Menu")
    pilihan = st.sidebar.radio("Pilih Halaman", ["Pengertian Karbohidrat", "Kalkulator Karbohidrat"])
    
    if pilihan == "Pengertian Karbohidrat":
        halaman_pengertian()
    elif pilihan == "Kalkulator Karbohidrat":
        halaman_kalkulator()

if __name__ == "__main__":
    main()
