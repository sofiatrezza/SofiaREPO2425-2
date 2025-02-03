"""
 Deseas crear un programa que te ayude a organizar tus eventos y tareas. Para esto, tu
 programa debe:------
Solicitar por teclado el nombre del evento a agendar
 Mostrar ordenadamente los meses del año para que el usuario seleccione el mes del
 evento
 Mostrar ordenadamente los días del mes para que el usuario seleccione el día del
 evento
 Mostrar ordenadamente las 24 horas del día para que el usuario seleccione la hora del
 evento (en este programa, cada evento tendrá una duración de una hora)
 Verificar si ese horario ya fue ocupado anteriormente por otro evento
 Notificar que el evento fue creado con éxito o que el horario seleccionado no está
 disponible. En caso de que se de lo último, deberá solicitarse una nueva fecha
 Debeexistir la opción de mostrar todos los eventos agendado
"""
#creamos una lista donde estaran los eventos
agenda=[]
#pedimos al usuario que agregue el evento
evento= input('ingrese el evento que desea agendar>>> ')
eventos_agendados=input('desea ver los eventos agendados>>>\n si o no: ').lower()
if eventos_agendados=='si':
    print(agenda)
else:
    print('no hay eventos agendados :)')

#meses del anio
meses=['enero', 'febrero','marzo','abril','mayo','junio','julio',\
       'agosto','septiembre','octubre','noviembre','diciembre']
print(meses)
mes_evento=input('ingrese el mes en el que sera el evento>>> ').lower()

for mes in meses:
    if mes==mes_evento:
        if mes=='febrero':
            for i in range(1,29):
                print(i) 
        elif mes in ['enero', 'marzo','mayo','julio','agosto','octubre','diciembre']:
            for i in range(1,32):
                print(i)
        else:
            for i in range(1,31):
                print(i)
#pedimos al usuario la fecha
fecha=int(input('seleccione el dia del mes>>> '))

#pedimos la hora del evento
for hora in range(25):
    print(f'{hora}:00')
hora_evento=int(input('seleccione la hora del evento>>> '))

#creamos el evento
nuevo_evento= f'{evento}, {fecha} de {mes} a las {hora_evento}:00 horas'

if hora_evento in agenda:
    print('no esta disponible esa hora del dia')
    hora_evento=input('seleccione la hora del evento>>> ')
else:
    agenda.append(nuevo_evento)
    print('el evento fue registrado con exito :)')

print(agenda)
    