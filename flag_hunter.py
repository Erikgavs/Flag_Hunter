# SCRIPT PARA BUSCAR ARCHIVOS POR TODO EL SISTEMA  
# PROTOTIPO PARA USARLO EN CTF'S PARA ENCONTRAR FLAG'S

# PARA CAMBIAR LA EXTENSIÓN DEL ARCHIVO, SUSTITUIR EL ".txt" POR OTRA EXTENSIÓN ".zip"


import os

def buscar_archivo(nombre_objetivo, carpeta_inicial="/"):
    encontrados = []
    for carpeta_raiz, carpetas, archivos in os.walk(carpeta_inicial):
        for archivo in archivos:
            if nombre_objetivo.lower() in archivo.lower() and archivo.endswith(".txt"): # MODIFICAR SEGÚN LA EXTENSIÓN DE ARCHIVO QUE NOS INTERESE 
                ruta_completa = os.path.join(carpeta_raiz, archivo)
                encontrados.append(ruta_completa)
    return encontrados


# EJEMPLOS DE USO
# ¿Qué archivo estás buscando? flag.txt
# ¿Qué archivo estás buscando? archivo.zip


nombre_a_buscar = input("¿Qué archivo estás buscando?: ")
carpeta_inicio = "/" if os.name != "nt" else "C:\\"

if not carpeta_inicio.strip():
    carpeta_inicio = "/" if os.name != "nt" else "C:\\"
resultados = buscar_archivo(nombre_a_buscar, carpeta_inicio)

print("\n🔍 Resultados:")
if resultados:
    for ruta in resultados:
        print(ruta)
else:
    print("No se ha ecncontrado el archivo específicado")