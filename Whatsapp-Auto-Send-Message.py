"""
- NASIL ÇALIŞIYOR ?
 + Açılan pencereden istersek 'Zamanla' butonuna basarak belirlediğimiz mesajı melirlediğimiz kişilere 'Gönder' butonuna basarak son bulan bir
   işlem olarak açıklayabilirim.

- KİŞİLERİ NEREYE KAYDEDİYOR ?
 + Açılan pencerede ortada bulunan iki adet alt alta kullanıcı inputları(kullanıcı girdileri) bulunuyor.
   Sırayla (boş bırakmamak üzere) girilen değerleri 'Numaralar' adlı .txt metin belgesi dosyası oluşturup
   bunun içerisine yazıyor

- KODLAR SANKİ GEREKSİZ UZAMIŞ GİBİ NEDEN ?
 + Her yiğidin yoğurt yiyişi farklı da ondan :)

- KAPANDIKTAN DOSYA BIRAKIYOR MU ?
 + Evet. Yalnızca 'Ekle' butonuna bastıktan sonra masaüstünüzde oluşan 'Numaralar.txt' metin belgesi dosyası.

- SADECE NUMARA MI YAZMAK ZORUNDAYIM ?
 + Hayır. Whatsapp'da kişiyi nasıl kaydettiysen öyle yazmalısın.

"""
__AUTHOR__ = "Arif-Helmsys"

import os                             # Sistem ile ilgili bir nevi kolaylıklar sağlaması açısından eklediğim modül
import webbrowser as web              # Varsayılan web browserimizi açmamızı sağlayacak modül
import pyautogui as pyg               # Ekranda belirlediğimiz yerlere tıklama yazma işlemlerini gerçekleştirecek modül
import time                           # Kısmi zamanlama ayarlamak için
from tkinter import *                 # GUI yapmak için, Bir kullanıcı arayüzüne sahip olabilmemizi sağlayan modül
from tkinter import messagebox as msg # Oluşturduğumuz arayüzde kullanıcılara uyarılar vermemizi sağlayan aynı modülün bir sınıfı
import getpass                        # Bilgisayarımızın kullanıcı adı herkeste farklı olduğundan ötürü bunu belirlemeye yaradığını düşündüğüm için kullandığım modül
from threading import Thread          # "while" döngüsüne girildiğinde kitlenmemesini sağlamak için eklediğim modül

class MainWindow():                   # MainWindow adında her olayın gerçekleştiği sınıf tanımladım
    def __init__(self) -> None:       # Sınıf ilk çağrıldığında bu __init__ methodu çalışıyor
        self.gui()
        if not os.path.exists("C:\\Users\\"+getpass.getuser()+"\\Desktop\\Numaralar.txt"): # Eğer belirlenen yolda "Numaralar.txt" adlı .txt dosyası yoksa falanca işlemi yap
            self.send.config(state="disabled")
        else:                                                                              # Böyle bir dosya varsa falanca işlemi yap
            self.send.config(state="normal")

    def clock(self):                                                                       # Kullanıcı arayüzünde görünen saati oluşturuyorum
        self.zaman = time.strftime("%H:%M:%S")
        self.time.config(text=self.zaman)
        self.time.after(1000,self.clock)
        
    def config(self):                                                                      # "config" adında bir method oluşturdum
        if self.zero_one.get() == 1:                                                       # "zamanla" adlı CheckButtona tıklanıp tıklanmadığını yakalamak için
            self.e1 = int(self.entry1__e.get())                                            # "localtime" fonksiyonu ile işlem yapabilmek için
            self.e2 = int(self.entry2__e.get())
        else:
            pass
    
    def cmd(self):                                                                        # "cmd" adında bir method oluşturdum
        e1_var = self.entry1.get()
        e2_var = self.entry2.get()
        if e1_var == "":
            msg.showinfo("Ups!","Girdiler Boş bırakılamaz")
        elif e2_var == "":
            msg.showinfo("Ups!","Kime Gönderileceğini Belirtmediniz")
        else:
            try:
                self.send.config(state="normal")
                with open("C:\\Users\\"+getpass.getuser()+"\\Desktop\\Numaralar.txt","x") as f: # "x" kipi, eğer kullanıcının bilgisayarında belirtilen adreste "Numaralar.txt" adlı dosya yoksa oluşturur
                    f.seek(0)
                    f.write(e2_var+"\n")
                    self.entry2.delete(0,END)
            except FileExistsError:                                                             # oluşturulan dosya bilgisayarda zaten varsa bu blok çalışır
                with open("C:\\Users\\"+getpass.getuser()+"\\Desktop\\Numaralar.txt","a") as g: # "a" kipi, "ekleme" kipinde dosya açılır
                    g.seek(0)
                    g.write(e2_var+"\n")
                    self.entry2.delete(0,END)

    def sendmsg(self):                                                                          # Ekrana tıklatılıp çalışacak(mesaj yazma, kişi arama, gönderme) komutlarının bulunduğu metod
        e1_var = self.entry1.get()
        self.boolean = self.zero_one.get()
        if e1_var == "":
            msg.showinfo("Ups!","Mesajı unuttunuz")
        else:
            if self.boolean == 1:
                while True:
                    self.local_time = time.localtime(time.time())
                    if self.e1 == self.local_time.tm_hour and self.e2 == self.local_time.tm_min:
                        break
                    else:
                        pass
                web.open("https://web.whatsapp.com")
                time.sleep(10)
                pyg.click(214,216)                                                              # ismi arat (whatsapp entry)
                with open("C:\\Users\\"+getpass.getuser()+"\\Desktop\\Numaralar.txt","r") as q: # "r" kipi, "okuma" kipinde açılır
                    sayac = 0
                    doc = q.read().split("\n")
                    if doc.index(""):
                        doc.remove("")
                        time.sleep(5)
                        while sayac <= len(doc):
                            time.sleep(2)
                            pyg.typewrite(doc[sayac])          # kişi adı yazma
                            sayac += 1             
                            time.sleep(3)                  
                            pyg.click(162,345)                 # kişi
                            time.sleep(1)
                            pyg.click(817,980)                 # Mesaj yazma bölümü
                            time.sleep(1)
                            pyg.typewrite(e1_var)              # Mesaj
                            time.sleep(1)
                            pyg.click(1809,973)                # Gönder tuşu
                            time.sleep(1)
                            pyg.click(214,216)                 # isim arama
                            if sayac == len(doc):
                                msg.showinfo("Bilgi","Mesaj Gönderme İşlemi Sonlandırıldı")
                                break
                            else:
                                 pass
            else: ### "Else" bloğunda aynı kodları kullanmamın sebebi kullanıcı zamanlayıcı kullanmak istemezse çalışmasını sağlamak için ###
                web.open("https://web.whatsapp.com")
                time.sleep(10)
                pyg.click(214,216)                                                                 # isim arama                                             
                with open("C:\\Users\\"+getpass.getuser()+"\\Desktop\\Numaralar.txt","r") as q:
                    sayac = 0
                    doc = q.read().split("\n")
                    if doc.index(""):
                        doc.remove("")
                        time.sleep(5)
                        while sayac <= len(doc):
                            time.sleep(2)
                            pyg.typewrite(doc[sayac])                                             # kişi adı yazma
                            sayac += 1             
                            time.sleep(3)                  
                            pyg.click(162,345)                                                    # kişi
                            time.sleep(1)
                            pyg.click(817,980)                                                    # Mesaj yazma bölümü
                            time.sleep(1)
                            pyg.typewrite(e1_var)                                                 # Mesaj
                            time.sleep(1)
                            pyg.click(1809,973)                                                   # Gönder tuşu
                            time.sleep(1)
                            pyg.click(214,216)                                                    # İsim arama
                            if sayac == len(doc):
                                msg.showinfo("Bilgi","Mesaj Gönderme İşlemi Sonlandırıldı")
                                break
                            else:
                                 pass
    def gui(self):          # Kullanıcı arayüzünü oluşturduğum method
        self.root = Tk()
        self.root.geometry("450x350")
        self.root.resizable(False,False)
        self.root.config(bg="green")
        self.root.title("Otomatik Whatsapp")
        self.variable = IntVar()
        self.variable2 = IntVar()
        self.zero_one = IntVar()
        Button(self.root,text="Ekle",activebackground="white",activeforeground="green",
                background="green",foreground="white",width=15,cursor="hand2",overrelief=SUNKEN,command=self.cmd).place(x=168,y=300)
        self.send=Button(self.root,text="Gönder",activebackground="white",activeforeground="green",
                background="green",foreground="white",width=10,cursor="hand2",overrelief=SUNKEN,command=lambda:Thread(target=self.sendmsg).start())
        self.send.place(x=350,y=300)
        self.timer=Checkbutton(self.root,text="Zamanla",variable=self.zero_one,onvalue=1,offvalue=0,
                cursor="hand2",background="green",activebackground="green",command=self.config)
        self.timer.place(x=10,y=300)
        Label(self.root,text="WhatsApp",bg="green",fg="white",font=("arial",20,"bold")).pack() # Başlık
        Label(self.root,text="Mesaj",bg="green",fg="white",font=("arial",13,"bold")).place(x=195,y=100)
        Label(self.root,text="Numara(örn:533xxxyyzz)\nVeya\nİsim",bg="green",fg="white",font=("arial",10,"bold")).place(x=140,y=190)
        Label(self.root,text="Saat\n-\nDakika",bg="green",fg="white",font=("arial",10,"bold")).place(x=30,y=190)
        self.time = Label(self.root,bg="green",fg="white",font=("arial",10))
        self.time.place(x=370,y=12)
        self.clock() # Saati çağırıyorum
        self.entry1__e = Entry(self.root,justify="center",font=("arial",10),
                            bg="green",highlightthickness=2,
                            highlightbackground="white",
                            fg="white",highlightcolor="white",insertbackground="white",width=5,textvariable=self.variable)
        self.entry1__e.place(x=30,y=150)
        self.entry2__e = Entry(self.root,justify="center",font=("arial",10),
                            bg="green",highlightthickness=2,
                            highlightbackground="white",
                            fg="white",highlightcolor="white",insertbackground="white",width=5,textvariable=self.variable2)
        self.entry2__e.place(x=30,y=260)
        self.entry1 = Entry(self.root,justify="center",font=("arial",10),
                            bg="green",highlightthickness=2,
                            highlightbackground="white",
                            fg="white",highlightcolor="white",insertbackground="white")
        self.entry1.place(x=135,y=150)
        self.entry2 = Entry(self.root,justify="center",font=("arial",10),
                            bg="green",highlightthickness=2,
                            highlightbackground="white",
                            fg="white",highlightcolor="white",insertbackground="white")
        self.entry2.place(x=135,y=260)

if __name__ == "__main__": # Scriptimizin çalışacağı bölüm
    MainWindow()           # Oluşturduğumuz sınıfı çağırıyorum
    mainloop()             # Kullanıcı arayüzü aktif olabilmesi için "tkinter" modülündeki fonksiyonu çağırıyorum
