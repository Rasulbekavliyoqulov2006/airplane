import time

class Samalyot():
    def __init__(self, nom, narx, raqam, brend, kotarilish_tezlig=200, max_tezlig=900, rang="oq"):
        self.name = nom
        self.brend = brend
        self.price = narx
        self.kotarilish_tezligi = kotarilish_tezlig
        self.number = raqam
        self.max_speed = max_tezlig
        self.color = rang
        self.speed = 0




    def info(self):
        print(f"Nom: {self.name}, Narx: {self.price}, Rangi: {self.color}")



    def start(self):
        if self.speed > 0:
            print("\nSamolyot allaqachon havoga ko'tarilgan.\n")
            return
        print("\nSamolyot ishga tushdi!!\n")






    def stop(self):
        if self.speed == 0:
            print("Samolyot allaqachon to'xtagan.")
        elif self.speed >= self.kotarilish_tezligi:
            print("Samolyot havoda, uni to'xtata olmaysiz.")
        else:
            print("Samolyot yerga qo'ndi va to'xtadi.")
            self.speed = 0





    def tezlik_qoshish(self, speed):
        if speed < 0:
            print("Tezlik manfiy bo'lishi mumkin emas!")
            return
        if speed > self.max_speed:
            print(f"Kiritilgan tezlik {speed} maksimal tezlikdan ({self.max_speed}) yuqori. Cheklangan tezlik o'rnatiladi.")
            speed = self.max_speed

        old_speed = self.speed
        self.speed = min(self.speed + speed, self.max_speed)

        for i in range(old_speed, self.speed + 10, 40):
            print(i,end=" ")
            time.sleep(0.8)
            if i==self.kotarilish_tezligi:
                time.sleep(3)
                print("\nhavoga kotarilishingiz mumkin\n") 
        print()
        print(f"Tezlik oshdi: {self.speed}\n")





    def speedometr(self):
        if self.speed >= self.kotarilish_tezligi:
            print("\nSamolyot havoda harakatlanmoqda!!!\n")
        else:
            print("\nTezlik havoga ko'tarilish uchun yetarli emas!!!\n")





    def tezlik_pasaytirish(self, a):
        if self.speed <= 0:
            print("\nSamolyot allaqachon to'xtagan\n")
            return

        old_speed = self.speed
        self.speed = max(self.speed - a, 0)

        for i in range(old_speed, self.speed + 10, -50):
            print(i, end=" ")
            time.sleep(0.8)
        print()
        
        print(f"Tezlik kamaydi: {self.speed}")

        if self.speed == 0:
            print("\nSamolyot to'xtadi\n")



            

s1 = Samalyot("Boeing 747", 100000000, "S123456", "Boeing", 200, 900, "White")
s1.info()
s1.start()
time.sleep(3)

print(f"\nTezlik: {s1.speed}\n")
time.sleep(3)

while True:
    tanlov = input("Tezlikni oshirish (Oshir)\n\nTezlikni pasaytirish (Pasaytir)\n\nSamolyotni to'xtatish (Toxta)\n\nKiriting--> ").strip().lower()

    match tanlov:
        case 'oshir':
            try:
                tezlik = int(input("\nQancha tezlik qo'shishni kiriting: "))
                s1.tezlik_qoshish(tezlik)
                s1.speedometr()
            except ValueError:
                print("\nNoto'g'ri qiymat, iltimos, son kiriting!\n")
        case 'pasaytir':
            if s1.speed > 0:
                try:
                    pasaytirish = int(input("\nQancha tezlik pasaytirishni kiriting: "))
                    s1.tezlik_pasaytirish(pasaytirish)
                    s1.speedometr()
                except ValueError:
                    print("Noto'g'ri qiymat, iltimos, son kiriting!")
            else:
                print("Samolyot to'xtadi. Dastur to'xtatilmoqda...")
                break
        case "toxta":
            if s1.speed >= s1.kotarilish_tezligi:
                print("\nSamolyot havoda, uni to'xtata olmaysiz.\n")
            else:
                print("\nSamolyot to'xtadi\n")
                break
        case _:
            print("\nNoto'g'ri tanlov, iltimos, qayta urinib ko'ring.\n")