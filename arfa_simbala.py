hari_kerja = 30
hari_kerja_perbulan = 30
gaji = 80000000

Total_Gaji = (hari_kerja/hari_kerja_perbulan) *gaji
Total_Gaji = int (Total_Gaji)
Penghasilan = "{:,.2f}" .format(Total_Gaji)
print (Penghasilan)
