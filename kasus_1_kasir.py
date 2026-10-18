class TransaksiKasir:
    def __init__(self, pelanggan, barang, harga, jumlah):
        self.pelanggan = pelanggan
        self.barang = barang
        self.harga = harga
        self.jumlah = jumlah

    def hitung_subtotal(self):
        return self.harga * self.jumlah
    
    def hitung_diskon(self):
        subtotal = self.hitung_subtotal()

        if subtotal >= 500000:
            return 0.15
        elif subtotal >= 250000:
            return 0.10
        elif subtotal >= 100000:
            return 0.05
        else:
            return 0

    def hitung_total(self):
        subtotal =  self.hitung_subtotal()
        potongan = subtotal * self.hitung_diskon()
        return subtotal - potongan

    def tampilkan_struk (self):
        subtotal = self.hitung_subtotal()
        diskon = self.hitung_diskon()
        potongan = subtotal * diskon
        total = self.hitung_total()


        print ("\n=== STRUK PEMBAYARAN ===")
        print ("Pelanggan   :", self.pelanggan)
        print ("Barang      :", self.barang)
        print (f"Subtotal    : Rp {subtotal:,.0f}". replace (",", "."))
        print (f"Diskon      : {diskon * 100:.0f}%")
        print (f"Potongan    : Rp{potongan:,.0f}".replace(",", "."))
        print (f"Total bayar : Rp{total:,.0f}".replace(",", "."))
        print ("==========================")

def input_positif(pesan):
    while True:
        try:
            nilai = int(input(pesan))
            if nilai > 0:
                return nilai
            print("Input harus lebih dari 0.")
        except ValueError:
            print("Masukan angka bulat yang valid")

print ("===KASIR MINIMARKET===")

pelanggan = input ("Nama pelanggan : "). strip()
while not pelanggan:
    print("Nama pelanggan tidak boleh kosong.")
    pelanggan = input ("Nama pelanggan : ").strip()

barang = input ("Nama barang : ").strip()
while not barang: 
    print ("Nama barang tidak boleh kosong")
    barang = input("Nama barang  : ").strip()

harga = input_positif("Harga barang  :")
jumlah = input_positif("Jumlah barang  :")
transaksi = TransaksiKasir(pelanggan, barang, harga, jumlah)
transaksi.tampilkan_struk()
