def pedirLibros():
    libros=[]
    while True:
        titulo=input("Libro: ")
        if titulo=='/':
            total_digitos=contarDigitos(libros)
            print(f'Línea completa. Aparecen {total_digitos} dígitos numéricos.')
            libros.clear()
        elif titulo == '*':
            break
        else:
            libros.append(titulo)
    return libros

def contarDigitos(linea):
    return sum(caracter.isdigit() for libro in linea)

def leerLineas():
    lineas = []
    conteo_barras = 0
    while True:
        libros = pedirLibros()
        if libros:
            lineas.extend(libros)
            total_digitos = contarDigitos(libros)
            print(f'Línea completa. Aparecen {total_digitos} dígitos numéricos.')
            conteo_barras += 1
        else:
            break
    return conteo_barras

def main():
    conteo_barras = leerLineas()
    print(f'Fin. Se leyeron {conteo_barras} líneas completas.')

if __name__ == "__main__":
    main()