import pandas as pd
data = [
    [90, 80],  
    [50, 60],  
    [65, 70]  
]

df = pd.DataFrame(data, columns=['algoritma dan struktur Data 2', 'matematika numerik'], index=['Mahasiswa 1', 'Mahasiswa 2', 'Mahasiswa 3'])
total_algoritma = sum(df['algoritma dan struktur Data 2'])
total_matematika = sum(df['matematika numerik'])
algoritma = total_algoritma / len(df)
matematika = total_matematika / len(df)

print("\nrata-rata nilai stiap matkul:")
print(f"Algoritma dan Struktur Data 2: {algoritma}")
print(f"Matematika Numerik: {matematika}")

print("\nrata-rata nilai stiap mahasiswa:")
for i in df.index:
    total_mahasiswa = sum(df.loc[i])
    mahasiswa = total_mahasiswa / len(df.columns)
    print(f"{i}: {mahasiswa}")
