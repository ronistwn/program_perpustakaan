import streamlit as st
import requests

class LibraryClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_books(self):
        return requests.get(f"{self.base_url}/books")

    def add_book(self, judul, penulis):
        data = {"judul": judul, "penulis": penulis}
        return requests.post(f"{self.base_url}/books", json=data)

    def update_book(self, book_id, judul, penulis):
        data = {"judul": judul, "penulis": penulis}
        return requests.put(f"{self.base_url}/books/{book_id}", json=data)

    def delete_book(self, book_id):
        return requests.delete(f"{self.base_url}/books/{book_id}")

# ===================== Streamlit ======================

BASE_URL = "http://localhost:5000"
client = LibraryClient(BASE_URL)

st.title("📚 Aplikasi Perpustakaan")

menu = st.sidebar.selectbox("Menu", ["Lihat Semua Buku", "Tambah Buku", "Ubah Buku", "Hapus Buku"])

if menu == "Lihat Semua Buku":
    response = client.get_books()
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
        response = client.add_book(judul, penulis)
        st.success("Buku berhasil ditambahkan!" if response.status_code == 201 else "Gagal menambah buku")

elif menu == "Ubah Buku":
    id_buku = st.number_input("ID Buku", min_value=1)
    judul = st.text_input("Judul Baru")
    penulis = st.text_input("Penulis Baru")
    if st.button("Ubah"):
        response = client.update_book(id_buku, judul, penulis)
        st.success("Berhasil diubah" if response.status_code == 200 else "Gagal mengubah")

elif menu == "Hapus Buku":
    id_buku = st.number_input("ID Buku", min_value=1)
    if st.button("Hapus"):
        response = client.delete_book(id_buku)
        st.success("Berhasil dihapus" if response.status_code == 200 else "Gagal menghapus")
