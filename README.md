# Flag_Hunter
Flag_hunter es un pequeño script diseñado con Python y bash, que nos permite automatizar la búsqueda de archivos en  el sistema, un caso útil para usar este script es cuando en un CTF estamos buscando las flags, al lanzar el script con el nombre del archivo y la extensión, lo buscará por todo el sistema

Explicación
Script diseñado para CTF'S, para búsqueda de flag's 
Soporta cualquier extensión de archivo, podremos editarlo dentro del script
Por ahora solo hay versión de Windows

Abajo tendremos una guía de uso de flag_hunter.py y flag_hunter.sh

# USO flag_hunter.py y flag_hunter.sh

## Flag_Hunter en Windows

Tendremos que tener instalado python 3 en nuestro dispositivo, si no lo tenemos haremos lo siguiente desde PowerShell

winget install --id Python.Python.3 --source winget

una vez hecho eso ejecutaremos el script de la siguiente manera

python3 flag_hunter.py

## Flag_Hunter en Linux

Tendremos que tener instalado python 3 en nuestro dispositivo, si no lo tenemos haremos lo siguiente desde la terminal

sudo apt install python3

Una vez hecho eso, ejecutaremos el script de la siguiente manera

python3 flag_hunter.py

# USO flag_hunter.sh

## flag_hunter.sh en Linux

En el directorio donde se encuentre el script, le otorgaremos permisos con el siguiente comando

chmod +x flag_hunter.sh

ejecutaremos el script de la siguiente manera

./flag_hunter.sh



