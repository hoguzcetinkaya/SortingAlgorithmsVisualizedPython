import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.ttk import Combobox # Combobox için gerekli
from tkinter import messagebox # Messagebox için gerekli

rastgeleDizi = []
copyRastgeleDizi = []
isStopped = False

# Oluştura basıldığında yeni grafik gelmesi arkada çalışan kaldırıldı
def olustur():
    global rastgeleDizi
    global copyRastgeleDizi
    if Combo.get() == "" or Combo2.get() == "":
        messagebox.showinfo("UYARI", "Grafik türünü ve sıralama algoritmasını seçmeniz gerekmektedir.")
        draw_button.config(state=tk.DISABLED)
    else:
        gtipi= Combo2.get()
        fig = plt.Figure(figsize=(5, 3), dpi=100)
        graph_ax = fig.add_subplot(111)
        graph_ax.clear()
        adet=grafikBoyut.get()
        rastgeleDizi=[np.random.randint(1,100) for _ in range(adet)]
        n=len(rastgeleDizi)
        graph_canvas = FigureCanvasTkAgg(fig, master=root)
        graph_canvas.get_tk_widget().place(x=100,y=175) # Grafik canvas konumlandırma
        if gtipi=='Bar':
            graph_ax.bar(list(range(adet)), rastgeleDizi,color='b')
        elif gtipi == 'Scatter':
            graph_ax.scatter(list(range(adet)), rastgeleDizi,color='b')
        elif gtipi == 'Stem':
            graph_ax.stem(list(range(adet)),rastgeleDizi)
        graph_canvas.draw()
        copyRastgeleDizi= list(rastgeleDizi)
        draw_button.config(state=tk.ACTIVE)
        clear_button.config(state=tk.ACTIVE)
        
def sifirla():
    etiket51.config(text='')
    etiket61.config(text='')
    generate_button.config(state=tk.ACTIVE)
    grafikBoyut.config(state=tk.ACTIVE)
    hizBoyut.config(state=tk.ACTIVE)
    Combo.config(state=tk.ACTIVE)
    Combo2.config(state=tk.ACTIVE)
    global rastgeleDizi, isStopped
    isStopped=False
    rastgeleDizi.clear()
    fig = plt.Figure(figsize=(5, 3), dpi=100)
    graph_ax = fig.add_subplot(111)
    graph_ax.clear()
    graph_canvas = FigureCanvasTkAgg(fig, master=root)
    graph_canvas.get_tk_widget().place(x=100,y=175) # Grafik canvas konumlandırma
    graph_canvas.draw()

def durdur():
    global isStopped
    isStopped = True
    stop_button.config(state=tk.DISABLED)

def BubbleSort():
    global rastgeleDizi, isStopped
    rastgeleDizi = list(copyRastgeleDizi)
    # Grafik tipini okumak için değişken
    gtipi= Combo2.get()
     # Algoritmanın çıkacağı alanı tanımladık boyutu 6ya 4 figure üzerine algoritma animasyonu çalışıyor
    fig = plt.Figure(figsize=(5, 3), dpi=100)
    graph_ax = fig.add_subplot(111)
    graph_ax.clear()

    # Grafik boyutunu okumak için adet sayısını alıyoruz
    adet=grafikBoyut.get()

    n=len(rastgeleDizi)
    # Figure alanının konumlandırması
    graph_canvas = FigureCanvasTkAgg(fig, master=root)
    graph_canvas.get_tk_widget().place(x=100,y=175) # Grafik canvas konumlandırma

    def bubble_sort(dizi):
        global sayac
        sayac=0
        for i in range(n):
            for j in range (0,n-i-1):
                sayac=sayac+1
                etiket61.config(text=sayac) # Label'a sayacı ata
                if isStopped:
                    return  # Döngüyü durdur
                if dizi[j]>dizi[j+1]:
                    dizi[j+1],dizi[j]=dizi[j], dizi[j+1]
                colors = ['blue' if x not in [j, j+1] else 'red' for x in range(adet)]
                if gtipi=='Bar':
                    graph_ax.bar(list(range(adet)), dizi,color=colors)
                elif gtipi == 'Scatter':
                    graph_ax.scatter(list(range(adet)), dizi,color=colors)
                elif gtipi == 'Stem':
                    graph_ax.stem(list(range(adet)), dizi)
                graph_canvas.draw()
                root.update()
                plt.pause((101-hizBoyut.get())/1000)
                graph_ax.clear()

    bubble_sort(rastgeleDizi)
    etiket51.config(text='O(n²)')
    plt.show
    stop_button.config(state=tk.DISABLED)

def SelectionSort():
    global rastgeleDizi
    rastgeleDizi = list(copyRastgeleDizi)
    # Grafik tipini okumak için değişken
    gtipi= Combo2.get()

    fig = plt.Figure(figsize=(5, 3), dpi=100)
    graph_ax = fig.add_subplot(111)

    # Grafik boyutunu okumak için adet sayısını alıyoruz
    adet=grafikBoyut.get()
    n=len(rastgeleDizi)

    # Figure alanının konumlandırması
    graph_canvas = FigureCanvasTkAgg(fig, master=root)
    graph_canvas.get_tk_widget().place(x=100,y=175) # Grafik canvas konumlandırma

    def selection_sort(dizi):
        global sayac
        sayac=0
        for i in range (0,n-1):
            min_index=i
            for j in range(i+1,n):
                if isStopped:
                    return  # Döngüyü durdur
                if dizi[j]<dizi[min_index]:
                    min_index=j
                sayac=sayac+1
                etiket61.config(text=sayac) #Label'a sayacı ata
            dizi[i], dizi[min_index]=dizi[min_index],dizi[i]
            colors = ['blue' if x not in [min_index,i] else 'red' for x in range(adet)]
            if gtipi=='Bar':
                graph_ax.bar(list(range(adet)), dizi,color=colors)
            elif gtipi == 'Scatter':
                graph_ax.scatter(list(range(adet)), dizi,color=colors)
            elif gtipi == 'Stem':
                graph_ax.stem(list(range(adet)), dizi)
            graph_canvas.draw()
            root.update()
            plt.pause((1000-hizBoyut.get())/1000)
            graph_ax.clear()

    selection_sort(rastgeleDizi)
    etiket51.config(text='O(n²)')
    plt.show
    stop_button.config(state=tk.DISABLED)

def InsertionSort():
    global rastgeleDizi
    rastgeleDizi = list(copyRastgeleDizi)
    # Grafik tipini okumak için değişken
    gtipi= Combo2.get()

    fig = plt.Figure(figsize=(5, 3), dpi=100)
    graph_ax = fig.add_subplot(111)

    # Grafik boyutunu okumak için adet sayısını alıyoruz
    adet=grafikBoyut.get()

    n=len(rastgeleDizi)

    # Figure alanının konumlandırması
    graph_canvas = FigureCanvasTkAgg(fig, master=root)
    graph_canvas.get_tk_widget().place(x=100,y=175) # Grafik canvas konumlandırma

    def insertion_sort(dizi):
        global sayac
        sayac=0
        for i in range(1,n):
            j=i
            while dizi[j-1]>dizi[j] and j>0:
                sayac=sayac+1
                etiket61.config(text=sayac) # Label'a sayacı ata
                if isStopped:
                    return  # Döngüyü durdur
                dizi[j-1], dizi[j]=dizi[j],dizi[j-1]
                colors = ['blue' if x not in [j, j-1] else 'red' for x in range(adet)]
                if gtipi=='Bar':
                    graph_ax.bar(list(range(adet)), dizi,color=colors)
                elif gtipi == 'Scatter':
                    graph_ax.scatter(list(range(adet)), dizi,color=colors)
                elif gtipi == 'Stem':
                    graph_ax.stem(list(range(adet)), dizi)
                graph_canvas.draw()
                root.update()
                plt.pause((101-hizBoyut.get())/1000)
                graph_ax.clear()
                j-=1
    insertion_sort(rastgeleDizi)
    etiket51.config(text='O(n²)')
    plt.show
    stop_button.config(state=tk.DISABLED)

def QuickSort():
    global rastgeleDizi
    rastgeleDizi = list(copyRastgeleDizi)
    global sayac
    sayac=0
    # Grafik tipini okumak için değişken
    gtipi= Combo2.get()

    fig = plt.Figure(figsize=(5, 3), dpi=100)
    graph_ax = fig.add_subplot(111)

    # Grafik boyutunu okumak için adet sayısını alıyoruz
    adet=grafikBoyut.get()

    n=len(rastgeleDizi)

    # Figure alanının konumlandırması
    graph_canvas = FigureCanvasTkAgg(fig, master=root)
    graph_canvas.get_tk_widget().place(x=100,y=175) # Grafik canvas konumlandırma

    def quick_sort(dizi,sol,sag):
        global sayac
        if sol<sag:
            colors = ['blue' if x not in [sol, sag] else 'red' for x in range(adet)]
            if gtipi=='Bar':
                graph_ax.bar(list(range(adet)), dizi,color=colors)
            elif gtipi == 'Scatter':
                graph_ax.scatter(list(range(adet)), dizi,color=colors)
            elif gtipi == 'Stem':
                graph_ax.stem(list(range(adet)), dizi,color=colors)
            graph_canvas.draw()
            root.update()
            plt.pause((101-hizBoyut.get())/1000)
            graph_ax.clear()
            sayac=sayac+1
            etiket61.config(text=sayac) # Label'a sayacı ata
            partition_pos=partition(dizi,sol,sag)
            quick_sort(dizi,sol,partition_pos-1)
            quick_sort(dizi,partition_pos+1,sag)
            colors = ['blue' if x not in [sol, sag] else 'red' for x in range(adet)]
            if gtipi=='Bar':
                graph_ax.bar(list(range(adet)), dizi,color=colors)
            elif gtipi == 'Scatter':
                graph_ax.scatter(list(range(adet)), dizi,color=colors)
            elif gtipi == 'Stem':
                graph_ax.stem(list(range(adet)), dizi)
            graph_canvas.draw()
            root.update()
            plt.pause((101-hizBoyut.get())/1000)
            graph_ax.clear()
            
    def partition(dizi,sol,sag):
        global sayac
        i=sol
        j=sag
        pivot=dizi[sag]
        while i<j:
            sayac=sayac+1
            etiket61.config(text=sayac) # Label'a sayacı ata
            if isStopped:
                return  # Döngüyü durdur
            while i<sag and dizi[i]<pivot:
                i+=1
            while j>sol and dizi[j]>=pivot:
                j-=1
            if i<j:
                dizi[i], dizi[j]=dizi[j],dizi[i]
        if dizi[i]>pivot:
            if isStopped:
                return  # Döngüyü durdur
            dizi[i],dizi[sag]=dizi[sag],dizi[i]
            sayac=sayac+1
            etiket61.config(text=sayac) # Label'a sayacı ata
        
        return i

    quick_sort(rastgeleDizi,0,n-1)
    etiket51.config(text='O(n log(n))')
    plt.show
    stop_button.config(state=tk.DISABLED)

def MergeSort():
    global rastgeleDizi
    global sayac
    sayac=0
    rastgeleDizi = list(copyRastgeleDizi)
    # Grafik tipini okumak için değişken
    gtipi= Combo2.get()

    fig = plt.Figure(figsize=(5, 3), dpi=100)
    graph_ax = fig.add_subplot(111)
    

    # Grafik boyutunu okumak için adet sayısını alıyoruz
    adet=grafikBoyut.get()

    n=len(rastgeleDizi)

     # Figure alanının konumlandırması
    graph_canvas = FigureCanvasTkAgg(fig, master=root)
    graph_canvas.get_tk_widget().place(x=100,y=175) # Grafik canvas konumlandırma

    def merge_sort(dizi, sol, sag):
        if isStopped:
            return  # Döngüyü durdur
        
        if sol>=sag:
            return
        
        orta=(sol+sag)//2
        colors = ['blue' if x not in [sol, sag] else 'red' for x in range(adet)]
        if gtipi=='Bar':
            graph_ax.bar(list(range(adet)), dizi,color=colors)
        elif gtipi == 'Scatter':
            graph_ax.scatter(list(range(adet)), dizi,color=colors)
        elif gtipi == 'Stem':
            graph_ax.stem(list(range(adet)), dizi)
        graph_canvas.draw()
        root.update()
        plt.pause((101-hizBoyut.get())/1000)
        graph_ax.clear()

        if isStopped:
            return  # Döngüyü durdur
        
        merge_sort(dizi, sol,orta)
        
        if isStopped:
            return  # Döngüyü durdur
        merge_sort(dizi, orta+1,sag)
        
        if isStopped:
            return  # Döngüyü durdur
        
        merge(dizi,sol,sag,orta)
        colors = ['blue' if x not in [sol, sag, orta] else 'red' for x in range(adet)]
        if gtipi=='Bar':
            graph_ax.bar(list(range(adet)), dizi,color=colors)
        elif gtipi == 'Scatter':
            graph_ax.scatter(list(range(adet)), dizi,color=colors)
        elif gtipi == 'Stem':
            graph_ax.stem(list(range(adet)), dizi)
        graph_canvas.draw()
        root.update()
        plt.pause((101-hizBoyut.get())/1000)
        graph_ax.clear()

    def merge(dizi,sol,sag,orta):
        global sayac
        sol_kopya=dizi[sol:orta+1]
        sag_kopya=dizi[orta+1:sag+1]

        sol_sayac, sag_sayac=0, 0
        sirali_sayac=sol

        while sol_sayac<len(sol_kopya) and sag_sayac <len(sag_kopya):
            sayac=sayac+1
            etiket61.config(text=sayac) # Label'a sayacı ata
            if sol_kopya[sol_sayac]<=sag_kopya[sag_sayac]:
                dizi[sirali_sayac]=sol_kopya[sol_sayac]
                sol_sayac+=1
            else:
                dizi[sirali_sayac]=sag_kopya[sag_sayac]
                sag_sayac+=1
            sirali_sayac+=1

        while sol_sayac<len(sol_kopya):
            dizi[sirali_sayac]=sol_kopya[sol_sayac]
            sol_sayac+=1
            sirali_sayac+=1

        while sag_sayac<len(sag_kopya):
            dizi[sirali_sayac]=sag_kopya[sag_sayac]
            sag_sayac+=1
            sirali_sayac+=1
    merge_sort(rastgeleDizi,0,n-1)
    etiket51.config(text='O(n log(n))')
    plt.show
    stop_button.config(state=tk.DISABLED)

root = tk.Tk()
root.resizable(False, False)
root.title('Sıralama Algoritmaları Görselleştiricisi')
root.geometry("680x500")

etiket1 = tk.Label(root,text="Hız:",font="Helvetica 15 bold")
etiket1.place(x=10,y=15)

hizBoyut=Scale(root,from_=1,to=100,resolution=1,orient=HORIZONTAL,font=("Helvetica",10),width=8)
hizBoyut.place(x=60,y=10)

etiket2 = tk.Label(root,text="Boyut:",font="Helvetica 15 bold")
etiket2.place(x=10,y=55)

grafikBoyut=Scale(root,from_=10,to=100,resolution=1,orient=HORIZONTAL,font=("san-serif",10),width=8)
grafikBoyut.place(x=80,y=50)

grafikTipi=['Bar','Scatter','Stem']

etiket3 = tk.Label(root,text="Sıralama Algoritması:",font="Helvetica 15 bold")
etiket3.place(x=10,y=95)

Dizi=['Selection Sort','Insertion Sort','Quick Sort','Bubble Sort','Merge Sort']

Combo = Combobox(root,values=Dizi,height=5)
Combo.place(x=220,y=100)

etiket4 = tk.Label(root,text="Grafik Tipi:",font="Helvetica 15 bold")
etiket4.place(x=10,y=135)

etiket5 = tk.Label(root,text="Karmaşıklık Analizi: ", font="Helvetica 12 bold")
etiket5.place(x=400,y=10)

etiket51 = tk.Label(root,font="Helvetica 12 bold")
etiket51.place(x=560,y=10)

etiket6 = tk.Label(root,text="Karşılaştırma Sayısı: ", font="Helvetica 12 bold")
etiket6.place(x=400,y=30)

etiket61 = tk.Label(root,font="Helvetica 12 bold")
etiket61.place(x=570,y=30)

Combo2 = Combobox(root,values=grafikTipi,height=5)
Combo2.place(x=130,y=140)

def secilenSort():
    global rastgeleDizi
    plt.close()
    if grafikBoyut.get() != len(rastgeleDizi):
        messagebox.showinfo("UYARI", "Boyutu değiştirdiğiniz için önce oluştura basmalısınız.")
        draw_button.config(state=tk.DISABLED)
    else:
        draw_button.config(state=tk.DISABLED)
        generate_button.config(state=tk.DISABLED)
        grafikBoyut.config(state=tk.DISABLED)
        hizBoyut.config(state=tk.DISABLED)
        Combo.config(state=tk.DISABLED)
        Combo2.config(state=tk.DISABLED)
        stop_button.config(state=tk.ACTIVE)
        secilen_veri = Combo.get()
        if secilen_veri == 'Selection Sort':
            SelectionSort()
        elif secilen_veri == 'Insertion Sort':
            InsertionSort()
        elif secilen_veri == 'Quick Sort':
            QuickSort()
        elif secilen_veri == 'Bubble Sort':
            isStopped = False  # Döngü kontrolünü sıfırla
            BubbleSort()
        elif secilen_veri == 'Merge Sort':
            MergeSort()

# Çizim butonunu oluştur
draw_button =tk.Button(root, text='Başla',command=secilenSort,font="Helvetica 8 bold")
draw_button.place(x=10,y=215)
draw_button.config(state=tk.DISABLED)

generate_button =tk.Button(root, text='Oluştur',command=olustur,font="Helvetica 8 bold")
generate_button.place(x=10,y=175)

stop_button =tk.Button(root, text='Dur',command=durdur,font="Helvetica 8 bold")
stop_button.place(x=10,y=255)
stop_button.config(state=tk.DISABLED)

clear_button =tk.Button(root, text='Sıfırla',command=sifirla,font="Helvetica 8 bold")
clear_button.place(x=10,y=295)
clear_button.config(state=tk.DISABLED)

tk.mainloop()