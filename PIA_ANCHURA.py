import csv

#Definimos las listas 
rows = [] #Contiene todas las filas sacadas del archivo
sub1 = [] #aqui se guardaran las actividades del tema 1
sub2 = [] #aqui se guardaran las actividades del tema 2
sub3 = [] #aqui se guardaran las actividades del tema 3
sub4 = [] #aqui se guardaran las actividades del tema 4
obligatorias =[] #aqui se guardan las actividades obligatorias
c = [] #aqui se guarda la suma de los valores de cada tema

#Abre los documentos y extrae los datos en la lista rows
with open(r"C:\Users\emili\OneDrive - Universidad Autonoma de Nuevo León\FCFM\Inteligencia Artificial\instancias\i_1_0.csv", "r") as file:
#with open(r"C:\Users\DELL\Downloads\instancias\instancias\i_1_0.csv", "r") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        rows.append(row)

#Recibe la actividad que se esta revisando y regresa el valor de dicho tema
def cerrarsub(row):
    j = row[1]
    c = 0
    if j == '1':
        for i in sub1:
            c = c + int(i[5])
    elif j == '2':
        for i in sub2:
            c = c + int(i[5])
    elif j == '3':
        for i in sub3:
            c = c + int(i[5])
    elif j == '4':
        for i in sub4:
            c = c + int(i[5])
    return c

#Revisa las actividades requeridas de la actividad seleccionada
def requerimentos(row):
    if int(row[7]) != 0: #checa si se requiere una actividad extra para agregar la actividad seleccionada
        for i in rows:
            if i[3] == row[7]: #se busca en rows
                rows.remove(i) #se borra
                if int(i[1]) == 1:
                    sub1.append(i) #se agrega a la lista
                elif int(i[1]) == 2: 
                    sub2.append(i) #se agrega a la lista
                elif int(i[1]) == 3: 
                    sub3.append(i) #se agrega a la lista
                elif int(i[1]) == 4: 
                    sub4.append(i) #se agrega a la lista
                requerimentos(i) #se revisa si esta nueva actividad requiere alguna actividad mas 
    if int(row[8]) != 0: #checa si se requiere una actividad extra para agregar la actividad seleccionada
        for i in rows: 
            if i[3] == row[8]: #se busca en rows
                rows.remove(i) #se borra
                if int(i[1]) == 1:
                    sub1.append(i) #se agrega a la lista
                elif int(i[1]) == 2: 
                    sub2.append(i) #se agrega a la lista
                elif int(i[1]) == 3: 
                    sub3.append(i) #se agrega a la lista
                elif int(i[1]) == 4: 
                    sub4.append(i) #se agrega a la lista
                requerimentos(i) #se revisa si esta nueva actividad requiere alguna actividad mas 

#revisa si la lista de cada tema necesita actividades para llegar al valor minimo 
def inornot(row):
    c = cerrarsub(row)
    if int(row[1]) == 1 and c<70: #si el tema 1 necesita actividades (aun no se llega al valor minimo)
        sub1.append(row) #se agrega a la lista
    elif int(row[1]) == 2 and c<70: #si el tema 2 necesita actividades (aun no se llega al valor minimo)
        sub2.append(row) #se agrega a la lista
    elif int(row[1]) == 3 and c<70: #si el tema 3 necesita actividades (aun no se llega al valor minimo)
        sub3.append(row) #se agrega a la lista
    elif int(row[1]) == 4 and c<70: #si el tema 4 necesita actividades (aun no se llega al valor minimo)
        sub4.append(row) #se agrega a la lista

#Revisa si se cumple todo para terminar el programa 
def terminar(sub1,sub2,sub3,sub4):
    c = [0,0,0,0] #aqui se guardan los valores de cada tema
    d = [0,0,0,0] #aqui se guarda la duracion de cada tema
# se suma los valores y las duraciones de cada tema
    for i in sub1:
        c[0] = c[0] + int(i[5])
        d[0] = d[0] + int(i[4])
    for i in sub2:
        c[1] = c[1] + int(i[5])
        d[1] = d[1] + int(i[4])
    for i in sub3:
        c[2] = c[2] + int(i[5])
        d[2] = d[2] + int(i[4])
    for i in sub4:
        c[3] = c[3] + int(i[5])
        d[3] = d[3] + int(i[4])
#se revisa si todos los valores ya son mayores a 70
    if c[0] >= 70 and c[1] >= 70 and c[2] >= 70 and c[3] >= 70:
#se imprime todo 
        for i in sub1:
            print(i)
        print("///////////////////////////////////////////////////////////////////////////////")
        for i in sub2:
            print(i)
        print("///////////////////////////////////////////////////////////////////////////////")
        for i in sub3:
            print(i)
        print("///////////////////////////////////////////////////////////////////////////////")
        for i in sub4:
            print(i)
        print("Valores =",c)
        print("Duracion =",d)
        return False
    return True

for i in rows: #se buscan todas las actividades obligatorias
    if int(i[9]) == 1: #en caso de ser obligatoria
        obligatorias.append(i) #se agrega a la lista obligatorias
#se le aplican los requerimentos a todas las act obligatorias y se agregan a sus respectivas listas
for i in obligatorias:
    requerimentos(i)
    if int(i[1]) == 1:
        sub1.append(i) #se agrega a la lista
    elif int(i[1]) == 2: 
        sub2.append(i) #se agrega a la lista
    elif int(i[1]) == 3: 
        sub3.append(i) #se agrega a la lista
    elif int(i[1]) == 4: 
        sub4.append(i) #se agrega a la lista

#se agregan a los temas
#se borran todas las actividades obligatorias de la lista principal 
while obligatorias:  
    for i in rows:
        if int(obligatorias[0][3]) == int(i[3]):
            rows.remove(obligatorias[0])
            break
    obligatorias.remove(obligatorias[0])
#se revisa si las actividades obligatorias son suficientes para cumplir con los parametros
terminar(sub1,sub2,sub3,sub4)

 #mientras no se cumplan los parametros    
while terminar(sub1,sub2,sub3,sub4): 
    lastrow = rows[-1]
    requerimentos(lastrow) #se revisan los requerimentos de la mejor
    inornot(lastrow) #Se revisa si se puede agregar al tema correspondiente 
    rows.remove(lastrow) #se borra de la lista principal




