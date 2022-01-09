# Tugas Deployment Sistem Informasi Lanjut
## Prediksi Asuransi Kesehatan

### Folder "backend"
Menggunakan flask untuk menyambungkan data python yang sudah di pickle, lalu membuat API dari data tersebut yang dideploy ke heroku dan akan digunakan untuk pemanggilan API pada sisi frontend.

### Folder "frontend"
Menggunakan vue.js untuk menampilkan tampilan website. Secara umum ada 2 page yang dibuat yaitu:
- First Page (Home.vue) : Halaman untuk memasukkan input dari pengguna. Untuk inputnya ada Nama, Umur, Jenis Kelamin, Tinggi dan Berat yang akan diubah menjadi BMI, lalu Jumlah Anak, Perokok atau Tidak, dan terkahir adalah Asal Daerah.
- Second Page (Result.vue) : Halaman untuk menampilkan output berupa prediksi jumlah biaya asuransi kesehatan yang harus dikeluarkan dalam USD.

### Link Deployment
Untuk mengakses hasil deployment bisa melalui [Link Berikut](http://insurance-prediction-sil.herokuapp.com/) atau bisa langsung melalui :
```
http://insurance-prediction-sil.herokuapp.com/
```