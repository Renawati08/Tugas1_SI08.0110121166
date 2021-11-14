def validMember():
  import re
  regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
  email = input("Masukkan Email anda: ")
  if (re.fullmatch(regex, email)):
    return validPass()
  else:
    print("Email Tidak Valid.")
    return False

def validPass():
  charSpec = ['@', '#', '$', '!']
  num = ["0","1","2","3","4","5","6","7","8","9"]
  passwd = input("Masukkan Password: ")
  if len(passwd) >= 8:
    if any(word.isnumeric() for word in passwd):
      if any(word.islower() for word in passwd):
        if any(word.isupper() for word in passwd):
          if any(word in charSpec for word in passwd):
            return True
          else:
            print("Email Tidak Valid")
            return validPass()
        else:
          print("Email Tidak Valid")
          return validPass()
      else:
        print("Email Tidak Valid")
        return validPass()
    else:
      print("Email Tidak Valid1")
      return validPass()
  else:
    print("Email Tidak Valid")
    return validPass()

def levPlayer(level):
  diskon = 0
  # level = input("Masukkan level kepesertaan Anda (Silver/Gold/Diamond): ")
  if level == 'Silver':
    if iterasi >= 5:
      diskon = diskon + 0.1
      print("Selamat! Anda mendapatkan potongan harga 10%")
      return diskon
  else:
    print("Masukkan tidak Valid")
    return False    

iterasi = 0
totalHarga = 0
print("Fitur Belanja")
while True:
  produk = input("Masukkan nama produk atau X untuk selesai: ")
  if produk == 'x' or produk == 'X':
    if iterasi > 0:
      print("Produk yang dibeli: "+str(iterasi))
      print("Total Harga: ", totalHarga)
      yorn = input("\nApakah anda seorang anggota (Y/T): ")
      if yorn == 't' or yorn == 'T':
        print("Total Harga: ", totalHarga)
      elif yorn == 'Y' or yorn == 'y':
        validMember()
        while True:
          level = input("Masukkan level kepesertaan Anda (Silver/Gold/Diamond): ")
          disk = levPlayer(level)
          if disk == False:
            continue
          else:
            break
        totalDiskon = totalHarga * disk
        totalHarga = totalHarga - totalDiskon
        print("Total harga yang harus dibayar Rp."+ str(round(totalHarga, 3)), "\nTerima kasih telah berbelanja di NFElectrics.") 
        break       
      else:
        print("Input tidak valid")
    else:
      print("Terima kasih telah berbelanja di NFEIelectrics.")
      break
  else:
    harga = int(input("Masukkan Harga Produk: "))
    print("Nama Produk: "+produk+" dengan harga "+str(harga))
    iterasi += 1
    totalHarga += harga