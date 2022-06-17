import os
import re

z=[]

def recursive(x):
    if os.path.isdir(x):
        a=os.listdir(x)
        b=0
        t='n'
        while b<len(a):
            c=re.search(r'(.[a-z]*)$',a[b])#extraer la extension del archivo
            if os.path.isdir(os.path.join(x,a[b])): #consulta si es directorio
                if os.path.join(x,a[b]) not in z:
                    recursive(os.path.join(x,a[b]))
            elif c[1] in ['.txt','.csv']: #consulta si la carpeta actual contiene .txt o .csv
                t='s'
            b+=1
        if t=='s':
            z.append(x)
        return
    else:
        print('la direccion ingresada no es un directorio')
        return
        
if __name__=='__main__':
    dire=input('Direccion: ')
    recursive(dire)
    for a in z:
        print(a)
