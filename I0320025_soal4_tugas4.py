# Syarat calon siswa kursus online:
# 1. Usia minimal 21 tahun
# 2. Lulus ujian kualifikasi

usia = int(input("Berapa usia kamu? = "))
ujian = input("Apakah Anda sudah lulus ujian kualifikasi(Y/T)? = ")

# output
if usia >= 21 and ujian == 'Y':
    print("Anda dapat mendaftar kursus.")
else:
    print("Anda tidak dapat mendaftar di kursus.")