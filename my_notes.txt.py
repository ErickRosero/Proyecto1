# Creamos un nuevo archivo llamado "notas.txt" en modo escritura ("w")
with open("notas.txt", "w") as Archivo_escritura:
    # Escribimos tres líneas de notas personales en el archivo
    Archivo_escritura.write("Linea 1: Soy Erick Rosero\n")
    Archivo_escritura.write("Linea 2: Me gusta el futbol\n")
    Archivo_escritura.write("Linea 3: Soy Militar de la Fuerza Aerea Ecuatoriana \n")
    # Cerramos el archivo
    Archivo_escritura.close()
    print("Archivo 'notas.txt' creado y escrito con éxito.")
    # Abrimos el archivo "notas.txt" en modo lectura ("r")
    with open("notas.txt", "r") as Archivo_escritura:
        # Leemos el contenido del archivo línea por línea
        Linea_1 = Archivo_escritura.readline()
        Linea_2 = Archivo_escritura.readline()
        Linea_3 = Archivo_escritura.readline()
        # Cerramos el archivo
        Archivo_escritura.close()
        # Mostramos en la consola cada línea leída
        print("Contenido del Archivo")
        print(
            "1: ", Linea_1,
            "2: ", Linea_2,
            "3: ", Linea_3
        )