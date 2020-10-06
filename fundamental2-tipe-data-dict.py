"""
Tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
dictionary = kamus
"""

kamus_ind_eng = {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])

print('\nData ini kirim oleh server Gojek, untuk memberikan info driver disekitar pemakai aplikasi ')
data_dari_servr_gojek = {
    'tanggal': '2020-10-06',
    'driver_list': [
        {'nama': 'Eko', 'jarak': 10},
        {'nama': 'Dwi', 'jarak': 30},
        {'nama': 'Tri', 'jarak': 100},
        {'nama': 'Catur', 'jarak': 1000}
    ]
}

print(data_dari_servr_gojek)
print(f"\ndriver sekitar sini{data_dari_servr_gojek['driver_list']}")
print(f"driver pertama {data_dari_servr_gojek['driver_list'][0]}")
print(f"driver empat {data_dari_servr_gojek['driver_list'][3]}")
print(f"Driver terdekat berjarak {data_dari_servr_gojek['driver_list'][0]['jarak']} meter")
