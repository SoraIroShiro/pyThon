uss = ['SUJOKO','SORA SORARI','SRIYANTI'] #list untuk menampung username
pas = ["ASIA2023"] #list untuk menampung password

print('=' * 30) #teks aksessoris (memanfaatkan operator aritmatika *)
print('Selamat datang di program PENCATAT PENGELUARAN HARIAN')
print('Username yang tersedia: SUJOKO, SORA SORARI, SRIYANTI ')
print('Password yang tersedia: ASIA2023')

username = input('Masukkan username anda (kapital):') #inputan username
password = input('Masukkan password (kapital):') #inputan password


if (username in uss) and (password in pas): #kondisi if berkolaborasi dengan operator and untuk menentukan uss dan pass
  print('Selamat datang') #jika uss dan pass benar
  print('=' * 30) #teks aksessoris (memanfaatkan operator aritmatika *)

  out = [] #menggunakan list untuk menampung inputan pengeluaran dan pemanfaatan variabel
  nom = [] #menggunakan list untuk menampung inputan nominal juga pemanfaatan variabel

  i = 0 #untuk menampung value penambahan item

  hari = input('Silakan masukkan hari:') #inputan hari
  tanggal = (input('Masukkan Tanggal - Bulan - Tahun')) #inputan tanggal (boleh input string, simbol, atau int)

  berhenti = False #sebagai start awal looping while


  while(not berhenti): #looping while
    t = i +1 #untuk deklarasi pengeluaran yang ke- (memanfaatkan increment)

    out_baru = input("Masukkan nama pengeluaran yang ke-{}: ".format(t)) #inputan nama pengeluaran dan deklarasi pengeluaran ke-
    out.append(out_baru) #memasukkan pengeluaran ke penampungan (list)

    nominal_baru = int(input("Masukkan nominal pengeluaran yang ke-{}: ".format(t))) #inputan nama pengeluaran dan deklarasi nominal pengeluaran ke-
    nom.append(nominal_baru) #memasukkan nominal pengeluaran ke penampungan (list)

    i += 1 #menggunkan increment untuk menambah item

    bertanya = input("Mau tambah pengeluaran lagi? (Y/T): ") #pertanyaan untuk menentukan kelanjutan looping
    if(bertanya == 'T'): #kondisi untuk looping
      berhenti = True #looping berakhir

  print('=' * 30) #teks aksessoris (memanfaatkan operator aritmatika *)

  print('Pengeluaran anda pada hari', hari,'tanggal', tanggal , ' adalah: ') #print deklarasi hari dan tanggal dari inputan
  for total_out in out: #mengiterasikan anggota list pengeluaran
    print('- {}'.format(total_out)) #print apa saja pengeluaran yang ada di list

  print('dengan nominal pengeluaran masing-masing:')
  for total_nominal in nom: #mengiterasikan anggota list nominal
    print('- {}'.format(total_nominal)) #print nominal masing-masing didalam list

  print('total pengeluaran yang anda beli adalah {} pengeluaran'.format(i)) #print total semua item/pengeluaran yang diinputkan
  print('dengan total nominal {}'.format(sum(nom))) #disini saya menggunakan keyword sum untuk menjumlahkan semua integer di inputan list nom

  print('=' * 30) #teks aksessoris (memanfaatkan operator aritmatika *)

  def sisa(totalmsk, totalklr): #menggunakan fungsi untuk menghitung sisa pemasukan - pengeluaran
    totalsisa = (totalmsk - totalklr) #menggunakan operator aritmatika -
    print("Jadi, sisa uang anda hari ini adalah " , totalsisa) #print hasil
  sisa(int(input("Total pemasukan hari ini:")),sum(nom)) #proses inputan total pemasukan yang nantinya dikurangi total pengeluaran
  print('Ditabung ya kak uangnya, jangan malah dipakai jajan :)') #tambahan text string :)


if username not in uss: #membuat kondisi username salah
  print('Username anda salah. Silakan diulang lagi :)')
if password not in pas: #mebuat kondisi password salah
  print('Password anda salah. Silakan diulang lagi :)')
elif (username and password) not in (uss and pas): #memanfaatkan operator and, or, not untuk membuat kondisi
  print('ups, ada yang salah. Silakan diulang lagi :)')