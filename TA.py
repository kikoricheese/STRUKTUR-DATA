import os
import queue

class myQueue:
    def __init__ (self):
        self.items = queue.Queue()

    def isEmpty(self):
        return self.items.empty()

    def qAdd(self, item):
        self.items.put(item)

    def qOut(self):
        if not self.items.empty():
            return self.items.get()
        else:
            return "Data Antrian Kosong"

    def mainMenu(self):
        pilih = "y"
        while (pilih== "y"):
            os.system("cls")
            print("==========================")
            print("| SERVIS MOTOR VISCOTION |")
            print("1. Masuk Antrian")
            print("2. Keluar Antrian")
            print("3. Cek Antrian")
            print("4. Banyak Antrian")
            print("5. Keluar Program")
            print("==========================")
            pilihan= str(input("Silahkan masukkan pilihan anda : "))
            if(pilihan == "1"):
                os.system("cls")
                obj = str(input("Masukkan nomor kendaraan yang ingin anda tambahkan : "))
                self.qAdd(obj)
                print("Nomor kendaraan "+obj+" berhasil masuk antrian")
                x = input("")
            elif(pilihan == "2"):
                os.system("cls")
                temp = self.qOut()
                if temp != "Data Antrian Kosong":
                    print("Kendaraan "+temp+" keluar dari antrian")
                else:
                    print("Antrian Kosong")
            elif(pilihan == "3"):
                os.system("cls")
                print(self.isEmpty())
                x = input("")
            elif(pilihan == "4"):
                os.system("cls")
                print("Panjang dari queue adalah : " +str(self.size()))
                x = input("")
            elif(pilihan == "5"):
                os.system("cls")
                print("Terima kasih sudah menggunakan program ini")
                print("Silahkan tekan Enter untuk keluar dari program")
                print("Semoga harimu menyenangkan :)")
                print(quit())
            else:
                pilih="n"

if __name__ == "__main__":
    q = myQueue()
    q.mainMenu()