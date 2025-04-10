#!/bin/bash
# SCRIPT PARA BUSCAR ARCHIVOS POR TODO EL SISTEMA  
# PROTOTIPO PARA USARLO EN CTF'S PARA ENCONTRAR FLAG'S

# PARA CAMBIAR LA EXTENSIÓN DEL ARCHIVO, SUSTITUIR EL ".txt" POR OTRA EXTENSIÓN ".zip"

read -p "Nombre del archivo que estás buscando: " nombre 
extension=".txt"

sistema=$(uname -s)

if [[ "$sistema" == "Linux" ]]; then
    carpeta_inicio="/"
elif  [[ "$sistema" == MINGW* || "$sistema" == CYGWIN* || "$sistema" == MSYS* ]]; then
    carpeta_inicio="C:/"
else 
    echo "Sistema operativo no compatible"
    exit 1
fi

echo -e "\n Resultados de la búsqueda:"
resultados=$(find "$carpeta_inicio" -type f -iname "*$nombre*$extension" 2>/dev/null)

if [[ -n "$resultados" ]] then
    echo "$resultados"
else   
    echo "No hemos encontrado el archivo"
fi
