import streamlit as st
import requests

BASE_URL = "http://localhost:5000"

st.title("📚 Aplikasi Perpustakaan")

menu = st.sidebar.selectbox("Menu", ["Lihat Semua Buku", "Tambah Buku", "Ubah Buku", "Hapus Buku"])

if menu == "Lihat Semua Buku":
    response = requests.get(BASE_URL + "/books")
    if response.status_code == 200:
        books = response.json()
        for book in books:
            st.write(f"📖 **{book['judul']}** oleh *{book['penulis']}* (ID: {book['id']})")
    else:
        st.error("Gagal mengambil data.")

elif menu == "Tambah Buku":
    judul = st.text_input("Judul Buku")
    penulis = st.text_input("Penulis")
    if st.button("Tambah"):
        data = {"judul": judul, "penulis": penulis}
        response = requests.post(BASE_URL + "/books", json=data)
        st.success("Buku berhasil ditambahkan!" if response.status_code == 201 else "Gagal menambah buku")

elif menu == "Ubah Buku":
    id_buku = st.number_input("ID Buku", min_value=1)
    judul = st.text_input("Judul Baru")
    penulis = st.text_input("Penulis Baru")
    if st.button("Ubah"):
        data = {"judul": judul, "penulis": penulis}
        response = requests.put(BASE_URL + f"/books/{id_buku}", json=data)
        st.success("Berhasil diubah" if response.status_code == 200 else "Gagal mengubah")

elif menu == "Hapus Buku":
    id_buku = st.number_input("ID Buku", min_value=1)
    if st.button("Hapus"):
        response = requests.delete(BASE_URL + f"/books/{id_buku}")
        st.success("Berhasil dihapus" if response.status_code == 200 else "Gagal menghapus")
