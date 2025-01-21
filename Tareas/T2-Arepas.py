"""
Sofia Trezza
Seccion 2
Tarea 2
"""

print("Hola! Queremos ayudarte a calcular el volumen de la arepa que haras")
conv_taza_cda= 16
conv_cdta_cda= 3
conv_cda_ml= 15
evap= round(0.1,1)
taza_agua= float(input("Cual fue el numero de tazas de agua que usaste (Ej. media taza = 0.5): "))
taza_harina= float(input("Cual fue el numero de tazas de harina PAN que usaste (Ej. media taza = 0.5): "))
cdta_sal= float(input("Cual fue el numero de cucharaditas de sal que usaste (Ej. media cdta = 0.5): "))
cda_aceite= float(input("Cual fue el numero de cucharadas de aceite que usaste (Ej. media cda = 0.5): "))

agua=taza_agua*conv_taza_cda*conv_cda_ml
ml_agua=agua-(agua*evap)
ml_harina=taza_harina*conv_taza_cda*conv_cda_ml
ml_sal=(cdta_sal/conv_cdta_cda)*conv_cda_ml
ml_aceite=cda_aceite*conv_cda_ml

vol_arepa=ml_aceite+ml_agua+ml_harina+ml_sal
print("El volumen total de la arepa que hiciste es "+str(vol_arepa)+" ml!")