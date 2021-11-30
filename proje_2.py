
import os
from tkinter import *
import threading
import time
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import numpy as np
sudoku_gui = Tk()
start = time.time()
sudoku_gui.geometry('650x650')
sol_ust={}
sag_ust={}
sag_alt={}
sol_alt={}
orta={}
thread_kontrol=0
ters_sol_ust={}
ters_sag_ust={}
ters_sag_alt={}
ters_sol_alt={}
ters_orta={}
matris1=[["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"]]
matris2=[["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"]]
matris3=[["*","*","*","*","*","*","*","*","*"],["","","","","","","","",""],["","","","","","","","",""],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"]]
matris4=[["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"]]
matris5=[["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"]]
axis_x=[]
axis_y=[]
axis_x1=[]
axis_y1=[]
class ara_yuz():

    
    
    def __init__(self, master):
        self.master = master
        self.gui(master)
        
        

    def gui(self, master):

       
        self.master = master
        master.title("Samuray Solver")
        master.config(bg="#FFE4E1")
        font = ('Arial', 18)
        color = 'white'
        px, py = 0, 0

        x = 0
        y = 0
        xsayac = 0
        ysayac = 0
        x1 = 180
        y1 = 180
        xsayac1 = 0
        ysayac1 = 0
        x2 = 360
        y2 = 360
        xsayac2 = 0
        ysayac2 = 0
        x3 = 360
        y3 = 0
        xsayac3 = 0
        ysayac3 = 0
        x4 = 0
        y4 = 360
        xsayac4 = 0
        ysayac4 = 0

        self._tablo = []
        self._tablo1 = []
        self._tablo2 = []
        self._tablo3 = []
        self._tablo4 = []
        for i in range(1, 10):
            self._tablo += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
            self._tablo1 += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
            self._tablo2 += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
            self._tablo3 += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
            self._tablo4 += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
        
        for i in range(0, 9):
            for j in range(0, 9):

                if (i < 3 or i > 5) and (j < 3 or j > 5):
                    #color = "#00CDCD"
                    color ='#ffff89'
                elif i in [3, 4, 5] and j in [3, 4, 5]:
                    color = "#ffff89"
                else:
                    color = '#ec8464'

                self._tablo[i][j] = Label(master, width=2, font=font, bg=color, cursor='arrow', borderwidth=0,
                                           highlightcolor='yellow', highlightthickness=1, highlightbackground='black',
                                           text=matris1[i][j])

                self._tablo[i][j].grid(row=i, column=j)
                self._tablo[i][j].place(x=x, y=y)
                self._tablo1[i][j] = Label(master, width=2, font=font, bg=color, cursor='arrow', borderwidth=0,
                                            highlightcolor='yellow', highlightthickness=1, highlightbackground='black',
                                            text=matris2[i][j])
                self._tablo1[i][j].grid(row=i, column=j)
                self._tablo1[i][j].place(x=x3, y=y3)
                self._tablo2[i][j] = Label(master, width=2, font=font, bg=color, cursor='arrow', borderwidth=0,
                                            highlightcolor='yellow', highlightthickness=1, highlightbackground='black',
                                            text=matris3[i][j])

                self._tablo2[i][j].grid(row=i, column=j)
                self._tablo2[i][j].place(x=x2, y=y2)
                self._tablo3[i][j] = Label(master, width=2, font=font, bg=color, cursor='arrow', borderwidth=0,
                                            highlightcolor='yellow', highlightthickness=1, highlightbackground='black',
                                            text=matris4[i][j])

                self._tablo3[i][j].grid(row=i, column=j)
                self._tablo3[i][j].place(x=x4, y=y4)
                # 3 3
                if( matris5[i][j]!="*"):
                    self._tablo4[i][j] = Label(master, width=2, font=font, bg=color, cursor='arrow', borderwidth=0,
                                                highlightcolor='yellow', highlightthickness=1, highlightbackground='black',
                                                text=matris5[i][j])

                    self._tablo4[i][j].grid(row=i, column=j)
                    self._tablo4[i][j].place(x=x1, y=y1)
                xsayac += 1
                ysayac += 1
                if (xsayac % 9 == 0):
                    x = 0
                    y += 30
                else:
                    x += 30
                xsayac1 += 1
                ysayac1 += 1
                if (xsayac1 % 9 == 0):
                    x1 = 180
                    y1 += 30
                else:
                    x1 += 30
                xsayac2 += 1
                ysayac2 += 1
                if (xsayac2 % 9 == 0):
                    x2 = 360
                    y2 += 30
                else:
                    x2 += 30
                xsayac3 += 1
                ysayac3 += 1
                if (xsayac3 % 9 == 0):
                    x3 = 360
                    y3 += 30
                else:
                    x3 += 30
                xsayac4 += 1
                ysayac4 += 1
                if (xsayac4 % 9 == 0):
                    x4 = 0
                    y4 += 30
                else:
                    x4 += 30
def satir_birlestir(A, B, c = ''):
    
    return [a+b+c for a in A for b in B]

digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits

id_var = 'a' 
satir_a = satir_birlestir(rows, cols, id_var)

sutun_a = ([satir_birlestir(rows, c, id_var) for c in cols] +
            [satir_birlestir(r, cols, id_var) for r in rows] +
            [satir_birlestir(rs, cs, id_var) for rs in ('ABC','DEF','GHI')
             for cs in ('123','456','789')])      
print(sutun_a)
id_var = 'b'
satir_b = satir_birlestir(rows, cols, id_var)
sutun_b = ([satir_birlestir(rows, c, id_var) for c in cols] +
            [satir_birlestir(r, cols, id_var) for r in rows] +
            [satir_birlestir(rs, cs, id_var) for rs in ('ABC','DEF','GHI')
             for cs in ('123','456','789')])
            
id_var = 'c' 
satir_c = satir_birlestir(rows, cols, id_var)
sutun_c = ([satir_birlestir(rows, c, id_var) for c in cols] +
            [satir_birlestir(r, cols, id_var) for r in rows] +
            [satir_birlestir(rs, cs, id_var) for rs in ('ABC','DEF','GHI')
             for cs in ('123','456','789')])
            
id_var = 'd' 
satir_d = satir_birlestir(rows, cols, id_var)
sutun_d = ([satir_birlestir(rows, c, id_var) for c in cols] +
            [satir_birlestir(r, cols, id_var) for r in rows] +
            [satir_birlestir(rs, cs, id_var) for rs in ('ABC','DEF','GHI')
             for cs in ('123','456','789')])
            
def repl(c):
    a = b = 0
    s = ""
    if c[0] in 'ABCGHI' and c[1] in '123789':
        if c[0] in 'ABC':
            s += chr(ord(c[0]) + 6)
            a = 1
        elif c[0] in 'GHI':
            s += chr(ord(c[0]) - 6)
            a = 2
        if c[1] in '123':
            s += chr(ord(c[1]) + 6)
            b = 1
        elif c[1] in '789':
            s += chr(ord(c[1]) - 6)
            b = 2
    else: return c
    if a == 1 and b == 1:
        s += 'a'
    elif a == 1 and b == 2:
        s += 'b'
    elif a == 2 and b == 1:
        s += 'c'
    elif a == 2 and b == 2:
        s += 'd'
    return s
            
id_var = '+'
satir_orta = [repl(x) for x in satir_birlestir(rows, cols, id_var)]
sutun_orta = ([satir_orta[x*9:x*9+9] for x in range(0,9)] +
                [satir_orta[x::9] for x in range(0,9)] +
                [satir_birlestir(rs, cs, id_var) for rs in ('ABC','DEF','GHI')
                 for cs in ('123','456','789')
                 if not (rs in 'ABCGHI' and cs in '123789')])
#bütün satırlar
tum_kareler = set(satir_a + satir_b + satir_c + satir_d + satir_orta)
values = dict((s, digits) for s in tum_kareler)
#bütün sütunlar
tum_sutunlar = sutun_a + sutun_b + sutun_c + sutun_d + sutun_orta

units = dict((s, [u for u in tum_sutunlar if s in u])
             for s in tum_kareler)

komsular = dict((s, set(sum(units[s],[]))-set([s]))
             for s in tum_kareler)

def sol_ustt(grid):
    print("sss")
    global values
   
    for s,d in dict(sol_ust).items():
        #time.sleep(0.001)
       # print("s: "+s+" ---- d: "+d)
        if d in digits and not deger_ata(values, s, d):
            # (Fail if we can't deger_ata d to square s.)
            #time.sleep(0.001)
            return False
        
    return values
def sag_ustt(grid):
    print("sss")
    global values
    for s,d in dict(sag_ust).items():
       # print("s: "+s+" ---- d: "+d)
        if d in digits and not deger_ata(values, s, d):
            # (Fail if we can't deger_ata d to square s.)
          
            return False
        
    return values
def sol_altt(grid):
    print("sss")
    global values
    for s,d in dict(sol_alt).items():
       # print("s: "+s+" ---- d: "+d)
        if d in digits and not deger_ata(values, s, d):
            # (Fail if we can't deger_ata d to square s.)
          
            return False
    return values
def sag_altt(grid):
    print("sss")
    global values
    for s,d in dict(sag_alt).items():
       # print("s: "+s+" ---- d: "+d)
        if d in digits and not deger_ata(values, s, d):
            # (Fail if we can't deger_ata d to square s.)
          
            return False
    return values
def ortaa(grid):
    print("sss")
    global values
    for s,d in dict(orta).items():
       # print("s: "+s+" ---- d: "+d)
        #time.sleep(0.001)
        if d in digits and not deger_ata(values, s, d):
            # (Fail if we can't deger_ata d to square s.)

           # time.sleep(0.001)
          
            return False
    return values
# 2 . threadlerin fonksiyonları
def sol_ustt1(grid):
    print("sss")
    global values
    
    for s,d in dict(ters_sol_ust).items():
        #time.sleep(0.001)
       # print("s: "+s+" ---- d: "+d)
        if d in digits and not deger_ata(values, s, d):
            # (Fail if we can't deger_ata d to square s.)
            #time.sleep(0.001)
            return False
        #print(" ------------------- ")
    """print("ters spl ust")
    print(ters_sol_ust)  
    print(" -----------  ")
    print("spl ust")
    print(sol_ust) """
    #for i in  range(len(dict(sol_ust))):
       #print(i)
    return values
def sag_ustt1(grid):
    print("sss")
    global values
    for s,d in dict(ters_sag_ust).items():
       # print("s: "+s+" ---- d: "+d)
        if d in digits and not deger_ata(values, s, d):
            # (Fail if we can't deger_ata d to square s.)
          
            return False
    return values
def sol_altt1(grid):
    print("sss")
    global values
    for s,d in dict(ters_sol_alt).items():
       # print("s: "+s+" ---- d: "+d)
        if d in digits and not deger_ata(values, s, d):
            # (Fail if we can't deger_ata d to square s.)
          
            return False
    return values
def sag_altt1(grid):
    print("sss")
    global values
    for s,d in dict(ters_sag_alt).items():
       # print("s: "+s+" ---- d: "+d)
        if d in digits and not deger_ata(values, s, d):
            # (Fail if we can't deger_ata d to square s.)
          
            return False
    return values
def ortaa1(grid):
    print("sss")
    global values
    for s,d in dict(ters_orta).items():
       # print("s: "+s+" ---- d: "+d)
        #time.sleep(0.001)
        if d in digits and not deger_ata(values, s, d):
            # (Fail if we can't deger_ata d to square s.)

           # time.sleep(0.001)
          
            return False
    return values

def samurai_solve(grid):
    global thread_kontrol
    dict1=grid_values(grid).items()
    
    #senkron()
    t1 = threading.Thread(target=sol_ustt(grid))
    #sol_ustt(grid,values)
    t2= threading.Thread(target=ortaa(grid))
    #sag_ustt(grid)
    t3=threading.Thread(target=sag_ustt(grid))
    #sol_altt(grid)
    t4=threading.Thread(target=sol_altt(grid))
    #sag_altt(grid)
    t5= threading.Thread(target=sag_altt(grid))
    #ortaa(grid,values)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    if( thread_kontrol==1):
        t6 = threading.Thread(target=sol_ustt1(grid))
        #sol_ustt(grid,values)
        t7= threading.Thread(target=ortaa1(grid))
        #sag_ustt(grid)
        t8=threading.Thread(target=sag_ustt1(grid))
        #sol_altt(grid)
        t9=threading.Thread(target=sol_altt1(grid))
        #sag_altt(grid)
        t10= threading.Thread(target=sag_altt1(grid))
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        t10.start()
    
    return values
tum =open('tum.txt','w')
def sudoku(arr):
    return [x for sub in arr for x in sub]

def reverse(list1,list2):
    dizi=list1[len(list1):0:-1]
    dizi.append(list1[0])
    dizi1=list2[len(list2):0:-1]
    dizi1.append(list2[0])
    return dict(zip(dizi, dizi1))
def grid_values(grid):
    global matris1
    global sol_ust
    global sag_ust
    global sol_alt
    global sag_alt
    global orta
    global ters_sol_ust
    global ters_sag_ust
    global ters_sag_alt
    global ters_sol_alt
    global ters_orta
    print("dfdsg")
    "Convert grid into a dict of {square: char} with '0' or '.' for empties."
    a = sudoku([x[:9] for x in grid[:9]])
    b = sudoku([x[9:18] for x in grid[:6]] + [x[12:21] for x in grid[6:9]])
    c = sudoku([x[:9] for x in grid[12:]])
    d = sudoku([x[12:21] for x in grid[12:15]] + [x[9:18] for x in grid[15:]])
    mid = sudoku([x[6:15] for x in grid[6:9]] + [x[0:9] for x in grid[9:12]] + [x[6:15] for x in grid[12:15]])
    chars = a + b + c + d + mid
    print("aaaa")
    r=0
    """for i in range(9):
        for j in range(9):
            matris1[i][j]=a[r]
            r+=1"""
   # print(a)
   # print(dizi)
    #print(type(satir_a))
    ters_sol_ust=reverse(satir_a,a)
    ters_sag_ust=reverse(satir_b,b)
    ters_sol_alt=reverse(satir_c,c)
    ters_sag_alt=reverse(satir_d,d)
    ters_orta=reverse(satir_orta,mid)
   #chars txt içindeki samuray sudokusunun sayıları var
   # print(chars)
   # sqrs içinde bütün kutucuklar var
    sqrs = satir_a + satir_b + satir_c + satir_d + satir_orta
    #print(sqrs)
    sol_ust=dict(zip(satir_a, a))
    sag_ust=dict(zip(satir_b, b))
    sol_alt=dict(zip(satir_c, c))
    sag_alt=dict(zip(satir_d, d))
    orta=dict(zip(satir_orta, mid))
    assert len(chars) == 405
    return dict(zip(sqrs, chars))
yazilanlar=[]
yildiz_sayi=52
def txt_yaz(s,d):
    global yazilanlar
    if((len(yazilanlar)!=0 and yazi_kontrol(s)) or len(yazilanlar)==0 ):
            yazilanlar.append(s)
            tum.write(str(s)+ " -- ")
            tum.write(str(d))
            tum.write("\n")
def yazi_kontrol(s):
    global yazilanlar
    for i in yazilanlar:
        if(str(i)==str(s)):
            
            return False
            
    return True

def atama(values,s,d):
    global yazilanlar
    global yildiz_sayi
    if(s[2]=='a' and len(values[s])==1 ):
       # print(s[1])
        for i in range(len(matris1)):
            matris1[rows.index(s[0])][digits.index(s[1])]=d
            
        txt_yaz(s,d)
        
        #print("---------------------------") 
    elif(s[2]=='+' and len(values[s])==1 ):
       # print(s[1])
        #matris5[rows.index(s[0])][digits.index(s[1])]=d
        for i in range(len(matris5)):
            matris5[rows.index(s[0])][digits.index(s[1])]=d
            
        txt_yaz(s,d)
    elif(s[2]=='b' and len(values[s])==1 ):
       # print(s[1])
        #matris2[rows.index(s[0])][digits.index(s[1])]=d
        for i in range(len(matris2)):
            matris2[rows.index(s[0])][digits.index(s[1])]=d
            
        txt_yaz(s,d)
    elif(s[2]=='c' and len(values[s])==1 ):
       # print(s[1])
        #matris4[rows.index(s[0])][digits.index(s[1])]=d  
        for i in range(len(matris4)):
            matris4[rows.index(s[0])][digits.index(s[1])]=d
            
        txt_yaz(s,d)
    elif(s[2]=='d' and len(values[s])==1 ):
       # print(s[1])
        matris3[rows.index(s[0])][digits.index(s[1])]=d
        for i in range(len(matris3)):
            matris3[rows.index(s[0])][digits.index(s[1])]=d
             
        
        txt_yaz(s,d)
ass=0
def deger_ata(values, s, d):
    global ass
    global thread_kontrol   
    atama(values,s,d)
    #print(s,d,values[s])
    if( len(values[s])==1 and d in digits):
        ass+=1
        if(thread_kontrol==1):
            
            axis_x.append(ass)
            end =time.time()-start
            axis_y.append(end)
            
            
        else:
            axis_x1.append(ass)
            end =time.time()-start
            axis_y1.append(end)
    

    other_values = values[s].replace(d, '')
    
    if all(eleme(values, s, d2) for d2 in other_values):
       # print(values)
        
        return values
    else:
        
        return False

def eleme(values, s, d):
    # Eleme İşlemleri
    
    if d not in values[s]:
        # Already elemed
      #  print(d+" ***** "+values[s])
        return values
    values[s] = values[s].replace(d,'')
    # (1) If a square s is reduced to one value d2,
    # then eleme d2 from the komsular.
    if len(values[s]) == 0:
        # Contradiction: removed last value
        return False
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eleme(values, s2, d2) for s2 in komsular[s]):
            return False
    # (2) If a unit u is reduced to only one place for a value d,
    # then put it there.
    for u in units[s]:       
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            # Contradiction: no place for this value
            return False
        elif len(dplaces) == 1:
            # d can only be in one place in unit; deger_ata it there
            if not deger_ata(values, dplaces[0], d):
                return False
    return values

def ara(values):
    if values is False:
        return False ## Failed earlier
  #  print("----*----")    
    if all(len(values[s]) == 1 for s in tum_kareler ):
        
        return values ## Solved!
    ## Chose the unfilled square s with the fewest possibilities
    n,s = min((len(values[s]), s) for s in tum_kareler if len(values[s]) > 1)
    return some(ara(deger_ata(values.copy(), s, d))
                for d in values[s])
def some(seq):
    
    for e in seq:
        if e: return e
    return False
 
if __name__ == '__main__':
    prompt = 1
    while prompt:
        txt = "aaa.txt"
        try:
            f = open(txt, 'r')
            prompt = 0
        except FileNotFoundError:
            print("File not found. (Example test cases can be found under "
                  "~/tests)\n")
    samurai_grid = f.read().split('\n')
    thread_kontrol=1
    ans = ara(samurai_solve(samurai_grid))
    ass=0
    thread_kontrol=2
    ans = ara(samurai_solve(samurai_grid))
    app = ara_yuz(sudoku_gui)
    sudoku_gui.mainloop()
    kat=369/axis_x[len(axis_x)-1]
    for i in range(len(axis_x)):
        axis_x[i]=axis_x[i]*kat
    plt.plot(axis_y, axis_x, label = "10 thread")
    for i in range(len(axis_y1)):
        axis_y1[i]=axis_y1[i]-axis_y[len(axis_y)-1]
    kat1=369/axis_x1[len(axis_x1)-1]
    for i in range(len(axis_x1)):
        axis_x1[i]=axis_x1[i]*kat1
    plt.plot(axis_y1, axis_x1, label = "5 thread")
    # naming the x axis
    plt.xlabel('Süre')
    # naming the y axis
    plt.ylabel('Kare Sayısı')
    # giving a title to my graph
    plt.title('Grafik')
    # show a legend on the plot
    plt.legend()
    plt.show()
