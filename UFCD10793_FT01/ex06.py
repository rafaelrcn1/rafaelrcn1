#Faz um programa que receba três parâmetros inteiros (horas, minutos e segundos) e converta o resultado para segundos, 
# devolvendo o output para o ecrã

horasv = int(input("Horas:\n-> "))
minutosv = int(input("Minutos:\n-> "))
segundos = int(input("Segundos:\n-> "))
               
horas_seg = horasv * 60 * 60
minutos_seg = minutosv *60

print(horas_seg+minutos_seg+segundos)