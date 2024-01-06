import pandas as pd
import numpy as np
import math

    #Excel dosyasını oku ve DataFrame'e dönustur
df = pd.read_excel("C:/Users/gokha/OneDrive/Masaüstü/İstatistik/Tez/6.1-Entropy.xlsx")
satir_sayisi = df.shape[0] 
sutun_sayisi = df.shape[1]

h = 1 / math.log(sutun_sayisi)

    #Toplamlar
toplamlar =[]
for j in range(0,sutun_sayisi):
    toplam = 0
    for i in range(0,satir_sayisi):
        toplam = toplam + (df.iloc[i,j])
    toplamlar.append(toplam)

    #Normalize
normalize_df = df.copy()
for j in range(0,sutun_sayisi):
    for i in range(0,satir_sayisi):
        normalize_df.iloc[i,j] = df.iloc[i,j] / toplamlar[j]
    
    #RIJ * ln(rij),
yeni_df = normalize_df.copy()
for j in range(0,sutun_sayisi):
    for i in range(0,satir_sayisi):
        yeni_df.iloc[i,j] = normalize_df.iloc[i,j] * math.log(normalize_df.iloc[i,j])

    #Yeni_df toplamlar
yeni_toplamlar =[]
for j in range(0,sutun_sayisi):
    yeni_toplam = 0
    for i in range(0,satir_sayisi):
        yeni_toplam = yeni_toplam + (yeni_df.iloc[i,j])
    yeni_toplamlar.append(yeni_toplam)

    #Eij
eij = []
for i in range(len(yeni_toplamlar)):
    eij.append(h *  yeni_toplamlar[i] * (-1))
    
eij_minusone = []
for i in range(len(yeni_toplamlar)):
    eij_minusone.append(1 - eij[i])
    
eij_minusone_toplam = sum(eij_minusone)

    #Wij
wij = []
for i in range(len(yeni_toplamlar)):
    wij.append(eij_minusone[i] /eij_minusone_toplam)
    
print(f"Entropy Wi: \n {wij}")
