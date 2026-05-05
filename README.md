# Kalkulator Harga Obligasi (*Bond Price Calculator*)

Aplikasi GUI berbasis Python untuk menghitung harga obligasi secara otomatis. Dibuat menggunakan pustaka bawaan `tkinter`.

## 📌 Fitur
*   **Kalkulasi Otomatis:** Menghitung harga obligasi menggunakan formula anuitas dan diskonto.
*   **Frekuensi Pembayaran Fleksibel:** Mendukung pembayaran *Annually* (Tahunan), *Semiannually* (Semesteran), *Quarterly* (Kuartalan), dan *Monthly* (Bulanan).
*   **Error Handling:** Aman dari *crash* jika pengguna salah memasukkan input (huruf, kosong, atau *Yield Rate* 0).


## 🚀 Cara Menjalankan
1. Simpan kode ke dalam file (contoh: `main.py`).
2. Buka Terminal atau *Command Prompt*.
3. Arahkan ke folder tempat file disimpan.
4. Jalankan perintah berikut:
   ```bash
   python main.py
   ```

## 💡 Cara Penggunaan
1. Masukkan angka pada form **Face Value** dan **Redemption Value**.
2. Masukkan persentase **Yield Rate** dan **Coupon Rate** (Cukup ketik angkanya saja. Contoh: ketik `5` untuk 5%).
3. Masukkan lama waktu jatuh tempo pada kolom **Tahun**.
4. Pilih **Frekuensi Pembayaran** yang diinginkan.
5. Klik tombol **"Hitung!"** untuk melihat hasilnya pada *pop-up*.
