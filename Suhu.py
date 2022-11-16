def calculatingTrue(a,nilai):
    if a == 1:
        reamour =  (4 * nilai) / 5
        farenheit = (9 * nilai) / 5 + 32
        kelvin = nilai + 273
        print("Nilai dari",nilai,"°C = ",reamour,"°R ,",farenheit,"°F ,",kelvin,"°K")
    elif a ==2:
        celcius = (5 * nilai) / 4
        farenheit = (9 * nilai ) / 4 + 32
        kelvin = (5 * nilai) / 4 + 273
        print("Nilai dari",nilai,"°R =",celcius,"°C ,",farenheit,"°F ,",kelvin,"°K")
    elif a ==3:
        celcius = ((5 * (nilai - 32))/9)
        reamour = ((4 * (nilai - 32))/9)
        print("Nilai dari",nilai,"°F =",celcius,"°C ,",reamour,"°R")
    elif a ==4:
        celcius = nilai - 273
        reamour = ((4 * (nilai - 273))/9)
        print("Nilai dari",nilai,"°K =",celcius,"°C ,",reamour,"°R")

def calculating(satuan):
    if satuan == 'C':
        nilai = float(input("Masukkan nilai suhu :"))
        calculatingTrue(1,nilai)
    elif satuan == 'R':
        nilai = float(input("Masukkan nilai suhu :"))
        calculatingTrue(2,nilai)    
    elif satuan == 'F':
        nilai = float(input("Masukkan nilai suhu :"))
        calculatingTrue(3,nilai)    
    elif satuan == 'K':
        nilai = float(input("Masukkan nilai suhu :"))
        calculatingTrue(4,nilai)    

def start():
    inputAwal = input("""[C] Celcius 
[R] Reamour
[F] Farenheit
[K] Kelvin
Suhu awal yang ingin diubah [C/R/F/K] : """)
    inputAwal = inputAwal.upper()
    if inputAwal == 'C':
        calculating("C")
    elif inputAwal == 'R':
        calculating("R")
    elif inputAwal == 'F':
        calculating("F")
    elif inputAwal == 'K':
        calculating("K")

start()