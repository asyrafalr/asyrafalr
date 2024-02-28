# Program Tabung Gas Delivery Service

## Context

Program ini adalah aplikasi CRUD (Create,Read,Update dan Delete) sederhana  yang terkait mengenai pemesanan tabung gas yang di pesan secara daring dan diinput menggunakan Python. Program CRUD ini adalah Program yang dapat membantu user untuk menambahkan pesanan tabung gas, 
melihat data pesanan, mengubah data pesanan dan menghapus data pesanan dan menunjukkan jumlah harga sebelum dikenakan biaya pengiriman. 
Tujuan program ini untuk memudahkan user dalam mengolah data pesanan yang sudah dipesan secara daring kepada Customer Service.

## Business Tasks
## Key Features
-	Menampilkan seluruh Data pesanan  yang sudah diinput
-	Menampilkan Data pesanan berdasarkan kode pesanan tertentu
-	Menambahkan Data pesanan
-	Merubah Data pesanan
-	Mengurutkan Data pesanan Berdasarkan Tanggal Pemesanan
-	Menunjukkan jumlah biaya berdasarkan jumlah tabung gas dan jenis tabung gas

## Objectives
Memberikan kemudahan serta solusi bagi pihak agen tabung gas dalam mengolah pesanan yang dipesan secara daring. 
Program ini bertujuan meningkatkan efektivitas dalam pengolahan data pesanan tabung gas.

## Stakeholders
1. End Users: tim entry data yang berkaitan dengan pengolahan data pesanan sebelum datanya digunakan oleh pihak agen gas.
2. Business Owners: 
3. Developers: Tim Developer yang bertugas membangun aplikasi, dan pemeliharaan aplikasi .
4. Investors : Investor yang memilki hubungan dengan . 

## Limitations
Projek ini memiliki beberapa keterbatasan:
1.	Limited Data: Data yang digunakan dalam program ini hanya dummy
2.	Limited Entry : Program ini hanya digunakan untuk pemesanan dalam satu jenis tabung gas untuk setiap data. Apabila ingin memesan 2 jenis tabung gas maka diperlukan memasukkan dua kali data dalam kode pesanan yang berbeda.
3.	No Shipping Cost Data: Program ini hanya menunjukkan data yang diperlukan oleh pihak agen gas sebelum dikenakan biaya pengiriman kepada pemesan  
4.	No Automatic Updates: Program ini tidak bisa di otomatisasi dan tetap memerlukan penambahan atau perubahan secara manual.
5.	Temporary Data : Data yang baru diinput dalam program ini tidak akan tersimpan apabila program sudah berhenti

## Data Summary
Data Pesanan Tabung Gas yang digunakan dalam program ini yakni :
-	Kode Pesanan
-	No HP pemesan
-	Nama Pemesan
-	Alamat Tujuan
-	Jumlah Tabung Gas yang dipesan
-	Jenis Tabung gas
-	Tanggal Pemesanan
-	Jumlah Biaya sebelum biaya pengiriman

## User Instructions
Installation
Untuk menggunakan program ini, harus menginstall beberepa module. Silahkan ikuti instruksi:
- pip install tabulate
- pip install datetime
