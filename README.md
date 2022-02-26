# Codigos_Postales_Municipios_ESP

Este es un proyecto simple que saca los códigos postales de los municipios de España utilizando web scraping.

Hay algunos casos en los que existen más de un código postal para un municipio, ya que el código postal de esos municipios depende de la dirección de la calle.

Para ejecutar el código habrá que crear un entorno virtual, instalar las librerías del archivo requirements.txt y ejecutar el script extract_codes.py. Como resultado, se realizará el web scraping y se guardará un archivo como csv en la raíz del proyecto. Para ello, habría que ejecutar los siguientes comandos en la raíz del proyecto:

## Windows
    virtualenv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    python extract_codes.py

## Linux
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python extract_codes.py



**NOTA:** Se realizó una comprobación aleatoria de varios códigos postales para ver si los datos eran correctos. Todos los códigos postales comprobados correspondían al municipio del mismo registro. Aún así no se han comprobado todos.