import tkinter as tk #Librería Tkinter para interfaces gráficas
from tkinter import messagebox #Importar función para ventanas

# Lista de estudiantes
studentslist = [["Lista de alumnos"]] #Texto que se mostrará al inicio de la lista

# Función para clasificar la nota
def clasificar_nota(nota): #Función para establecer el nivel de calificación
    if nota < 5: #Uso del if para determinar el nivel de calificación
        return "Suspendido" #Suspendido es menor a 5, si no se aplicarán el resto de niveles
    elif 5 <= nota < 7:
        return "Mejorable"
    elif 7 <= nota < 9:
        return "Aprobado"
    else:
        return "Perfecto"

# Función para buscar un alumno por DNI
def buscar_alumno(dni): #Función para buscar un alumno si se va a modificar o eliminar
    for i, student in enumerate(studentslist):
        if i > 0 and student[2] == dni:  # Saltar el título
            return i, student
    return None, None

# Funciones del programa
def agregar_estudiante(): #Función para agregar estudiantes
    try:
        dni = int(entry_dni.get())#Verificar la entrada del DNI
        _, existing_student = buscar_alumno(dni)
        if existing_student: #Verificar si el DNI no se repite
            messagebox.showerror("Error", f"Ya existe un estudiante con el DNI {dni}: {existing_student}")
        else: #Entrada del resto de datos
            nombre = entry_nombre.get() #Nombre/s
            apellidos = entry_apellidos.get() #Apellido/s
            nota = float(entry_nota.get()) #Nota
            calificacion = clasificar_nota(nota) #Nivel de calificación

            newStudent = [nombre, apellidos, dni, nota, calificacion] #Agrupar los datos introducidos
            studentslist.append(newStudent) #Agregar a un estudiante con sus datos
            messagebox.showinfo("Éxito", f"Estudiante agregado: {newStudent}") #Mensaje si el estudiante fue agregado existosamente
            mostrar_estudiantes() #Actualizar la lista de estudiantes
    except ValueError: #Tirar error si falta ingresar un dato o si no se ingresaron valores númericos en nota y DNI
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

def mostrar_estudiantes(): #Función para mostrar estudiantes
    text_output.delete("1.0", tk.END) #Seleccionar el campo de abajo para la introducción de datos
    text_output.insert(tk.END, "--- Lista de estudiantes ---\n")
    for student in studentslist[1:]:  # Saltar el título inicial
        text_output.insert(tk.END, f"Nombre: {student[0]}, Apellidos: {student[1]}, DNI: {student[2]}, Nota: {student[3]}, Calificación: {student[4]}\n") #Ingresar los datos del estudiante

def modificar_estudiante(): #Función para modificar nota de un estudiante
    try: #Verificar que los datos introducidos sean correctos
        dni = int(entry_dni.get()) #Utilizar el DNI para buscar a un alumno
        index, student = buscar_alumno(dni)
        if student: #Verificar datos del estudiante
            nueva_nota = float(entry_nota.get())
            student[3] = nueva_nota
            student[4] = clasificar_nota(nueva_nota)
            messagebox.showinfo("Éxito", f"Estudiante modificado: {student}")
            mostrar_estudiantes()
        else: #Verificar si el estudiante existe por su DNI
            messagebox.showerror("Error", "Estudiante no encontrado.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

def eliminar_estudiante(): #Función para eliminar datos de un estudiante
    try: #Verificar que los datos introducidos sean correctos
        dni = int(entry_dni.get()) #Utilizar el DNI para buscar a un alumno
        index, student = buscar_alumno(dni)
        if student: #Verificar datos del estudiante
            studentslist.pop(index)
            messagebox.showinfo("Éxito", f"Estudiante con DNI {dni} eliminado.")
            mostrar_estudiantes()
        else: #Verificar si el estudiante existe por su DNI
            messagebox.showerror("Error", "Estudiante no encontrado.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

# Interfaz gráfica
root = tk.Tk() #Configurar la ventana gráfica
root.title("Gestión de estudiantes") #Título de la ventana
root.configure(bg='lightblue')

# Entradas y etiquetas
frame = tk.Frame(root, bg='lightblue') #Color de fondo de la ventana
frame.pack(pady=10)

tk.Label(frame, text="Nombre:", bg='lightblue').grid(row=0, column=0, padx=5, pady=5) #Campo nombre
entry_nombre = tk.Entry(frame) #Campo para introducir los nombres
entry_nombre.grid(row=0, column=1, padx=5, pady=5) #Tamaño del campo

tk.Label(frame, text="Apellidos:", bg='lightblue').grid(row=1, column=0, padx=5, pady=5) #Campo apellidos
entry_apellidos = tk.Entry(frame) #Campo para introducir los apellidos
entry_apellidos.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="DNI:", bg='lightblue').grid(row=2, column=0, padx=5, pady=5) #Campo DNI
entry_dni = tk.Entry(frame) #Campo para introducir el DNI
entry_dni.grid(row=2, column=1, padx=5, pady=5) 

tk.Label(frame, text="Nota:", bg='lightblue').grid(row=3, column=0, padx=5, pady=5) #Campo Nota
entry_nota = tk.Entry(frame) #Campo para introducir la nota
entry_nota.grid(row=3, column=1, padx=5, pady=5)

# Botones
tk.Button(root, text="Agregar Estudiante", bg='blue', fg='white', command=agregar_estudiante).pack(pady=5) #Agregar estudiante
tk.Button(root, text="Modificar Nota", bg='blue', fg='white', command=modificar_estudiante).pack(pady=5) #Modificar datos de un estudiante
tk.Button(root, text="Eliminar Estudiante", bg='red', fg='white', command=eliminar_estudiante).pack(pady=5) #Eliminar estudiante

# Área de texto para la salida
text_output = tk.Text(root, width=80, height=15) #Campo que se actualiza solo con las acciones que se realicen en el programa
text_output.pack(pady=10)
text_output.configure(bg='lightyellow')

root.mainloop() #Bucle principal del programa, permite su ejecución
