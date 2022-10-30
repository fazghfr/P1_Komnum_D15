from ast import Str
from sys import stdin
from typing import Type
import numpy as np
import matplotlib.pyplot as plt


#define list untuk menyimpan data f(x2)
listArray=[]
isiArray=[]
listArray.append(0)
isiArray.append(0)

def bolzano(func, a, b):

    def f(x):
        f = eval(func)
        return f

    #error handling for f(X)
    try :
        f(a)
    except (SyntaxError, NameError, TypeError, ZeroDivisionError) :
        print('fungsi yang dimasukkan tidak dapat diproses')
        return
    
    #checking the guessed root
    if(f(a)*f(b) >= 0):
        print(f"tidak bisa menggunakan titik {a} and {b} untuk fungsi tersebut\nuntuk mencari akar dengan metode bolzano")
        return

    isContinue = True
    count  = 1

    print('\n======= TABEL BOLZANO / BISECTION METHOD =======')
    print("\n\nno \t x0 \t\t x1 \t\t x2 \t\t f(x2)")
    while isContinue:
        c = (a+b)/2
        isiArray.append(c)
        listArray.append({f(c)})
        x0 = round(a,3)
        x1 = round(b,3)
        x2 =round(c,3)
        fx2=round(f(c),3)
        print(f"{count} \t {x0} \t\t {x1}\t\t {x2} \t\t {fx2}")

        count = count + 1

        if(f(a)*f(c) < 0):
            b = c
        
        elif(f(a)*f(c) > 0):
            a = c
        
        elif(f(a)*f(c) == 0):
            isContinue = False
        
        if(isiArray[count-1]==isiArray[count-2]): 
            # jika output yang diberikan sama dengan iterasi sebelumnya
            isContinue = False
        elif(fx2 == 0):
            # jika nilai dari y ditemukan sama dengan 0
            isContinue = False
        elif(count > 200):
            # agar tidak looping infinity
            isContinue = False
    print(f"\nakarnya adalah {c} dengan {count-1} iteration\n")

def fungsi(x):
    fungsi = eval(function)
    return fungsi


    

#user input
print('CTRL + Z untuk Keluar')
for line in stdin :
    function = (input("masukkan fungsi : "))
    lower = (float)(input("masukkan batas bawah : "))
    upper = (float)(input("masukkan batas atas : "))

    bolzano(function, lower, upper)
    
    # grafik bolzano
    X= np.linspace(-upper,upper)
    Y = fungsi(X)
    data_Terakhir = len(isiArray)-1
    yes = isiArray[data_Terakhir]
    #PLOT UNTUK GRAFIK FUNGSI
    plt.plot(X,Y,'r-')
    #Garis saat Y = 0 atau mendekati
    plt.vlines(x=yes, ymin=-5,
                   ymax=upper*3, color='y')
    plt.title("Tampilan Grafik Bolzano")
    plt.xlabel("X")
    plt.ylabel("Y/F(x2)")
    plt.hlines(y=0, xmin=-4,
                   xmax=upper*3, color='black')
    plt.vlines(x=0, ymin=-4,
                   ymax=upper*3, color='black')
    plt.show()

    