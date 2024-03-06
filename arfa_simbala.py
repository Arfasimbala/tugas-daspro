hari_kerja = 31
hari_kerja_perbulan = 30
gaji = 80000000
gaji_lembur = 100000

if hari_kerja > hari_kerja_perbulan:
    Total_gaji = (hari_kerja/hari_kerja_perbulan)* gaji + gaji_lembur
elif hari_kerja < hari_kerja_perbulan:
    Total_gaji = (hari_kerja/hari_kerja_perbulan)* gaji

Penghasilan = "{:,.2f}" .format( Total_gaji )
print (Penghasilan)
