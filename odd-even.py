# Submitted by: Daniel Kessie

# Fungsi pemisah ganjil genap
def ganjilgenap(list_angka):
    temp_genap = []
    temp_ganjil = []
    for angka in list_angka:
        if angka % 2 == 0:
            temp_genap.append(angka)
        else :
            temp_ganjil.append(angka)

    print("Genap : ")
    for angka in temp_genap:
        if temp_genap.index(angka) < len(temp_genap)-1:
            print(angka, end=", ")
        else:
            print(angka, end=" ")

    print("\n\nGanjil : ")
    for angka in temp_ganjil:
        if temp_ganjil.index(angka) < len(temp_ganjil)-1:
            print(angka, end=", ")
        else:
            print(angka, end=" ")

# Proses input data untuk diproses 
print("=== Pemisah Angka Ganjil Genap ===")
jumlah_input = int(input("Jumlah input : "))
list_angka = [] 
print("----------------------")
for input_ in range(jumlah_input): 
    input_angka = int(input(f"Masukkan angka {input_+1}: "))
    list_angka.append(input_angka)

print("\n---Hasil Pemisahan Angka---")
ganjilgenap(list_angka)


    

