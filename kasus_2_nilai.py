class penilaianmahasiswa:
    def __init__(self, nim, nama, tugas, uts, uas):
        self.nim = nim
        self.nama = nama
        self.tugas = tugas
        self.uts = uts
        self.uas = uas

    def hitung_nilai_akhir(self):
        return (
            self.tugas * 0.30
            + self.uts * 0.30
            + self.uas * 0.40
        )

    def tentukan_grade(self):
        nilai = self.hitung_nilai_akhir()

        if nilai >= 85:
            return "A"
        elif nilai >= 75:
            return "B"
        elif nilai >= 65:
            return "C"
        elif nilai >= 50:
            return "D"
        else:
            return "E"

    def tentukan_kelulusan(self):
        if self.hitung_nilai_akhir() >=65:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def tampilkan_hasil(self):
        nilai = self.hitung_nilai_akhir()

        print ("\n=== HASIL AKADEMIK===")
        print ("NIM          :", self.nim)
        print ("Nama         :", self.nama)
        print (f"Nilai akhir  :{nilai:.2f}")
        print ("Grade        :", self.tentukan_grade())
        print ("Status       :", self.tentukan_kelulusan())
        print ("========================")

def input_nilai(pesan):
    while True:
        try:
            nilai = float(input(pesan))

            if 0 <= nilai <= 100:
                return nilai
            print ("Nilai harus berada antar 0 sampai 100.")

        except ValueError:
            print("Input tidak valid. masukkan angka.")

print ("=== SISTEM PENILAIAN")
nim  = input ("NIM             :").strip()
nama = input ("Nama            :").strip()

while not nim:
    print("NIM tidak boleh kosong.")
    nim = input("NIM       :").strip()

while not nama: 
    print("Nama tidak boleh kosong.")
    nama = input("Nama     :").strip()

tugas = input_nilai("Nilai tugas     :")
uts = input_nilai  ("Nilai UTS       :")
uas = input_nilai  ("Nilai UAS       :")

mahasiswa = penilaianmahasiswa(
    nim, nama, tugas, uts, uas
)

mahasiswa.tampilkan_hasil()



        
