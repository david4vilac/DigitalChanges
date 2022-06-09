Prueba Digital Changes
-------------
Repositorio creado con el fin de dar solución a la prueba técnica de DIGITAL CHANGES.

NIVEL 1
-------------
En este nivel se presentan diferentes funciones para verificar que los datos de ADN sean correctos. Estas funciones se encuentran **app/mutant.py**.
Las funciones son las siguientes:
 + is_adn
 + array_size   
 + horizontal_validation
 + vertical_validation
 + oblique_validation
 + is_mutant
 
Se hizo uso de nombres semánticos a la hora de nombrar las funciones y variables, esto con el fin de facilitar la lectura del código.

Al llamar la función **is_mutant** se validan las anteriores funciones. En caso que un ADN tenga un tamaño de NxN y los valores correspondan a los que representa a la base nitrogenada del ADN, se valida la condición que tenga **más de una secuencia de cuatro letras iguales**. Al no cumplirse envía un valor **False**. Estos valores se consumen en el siguiente nivel.


NIVEL 2 - API REST
-------------
Se utilizó el framework de FastAPI, para cumplir los objetivos de la prueba. Para hacer uso de las librerías utilizadas, sugiero crear un entorno virtual e instalar las librerías, de la siguiente manera:

 + Consola git bash o SO Linux
 
`$ python3 -m venv venv`

`$ source venv/bin/activate`

 + cmd windows (se necesita tener el paquete de software virtualenv).

 + Instalar librerías
 
`C:\> pip install virtualenv` - [Opcional]

`C:\> virtualenv venv` - Crea el virtual environment.

`C:\> venv\Scripts\activate.bat` - Inicializa el virtual environment.

 + Por ultimo se instalan los paquetes utilizados en el proyecto.

`(env) $ pip install -r requirements.txt`

 + Ya con esto se puede inicializar nuestro servicio. Con el comando:

`$ uvicorn app.main:main`

Al ingresar a localhost:8000/ se visualizará lo siguiente: 
![](https://github.com/AlvariroA/DigitalChanges/blob/main/img/Home.png)

Ahora al ingresar a localhost:8000/docs, se podrán ver las API con los métodos solicitados en el documento, estas se documentaron desde el archivo main.py

localhost:8000/docs
-------------

![](https://github.com/AlvariroA/DigitalChanges/blob/main/img/FastAPI.png)



Nivel 3
-------------

Utilice PostgreSQL para solucionar este ítem, la base de datos está adjuntada en el git, la cual cuenta con algunos registros. La conexión se encuentra en el archivo **database.py**, el nombre de la base de datos es **xmen**.

```
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:<password>@localhost:<puerto>/xmen"
```
Utilice PostgreSQL para solucionar este ítem, la base de datos está adjuntada en el git, la cual cuenta con algunos registros.
En este archivo se puede cambiar la dirección para consumo de la base de datos.

Para guardar datos en la base de datos se utiliza un HTTP POST -> /mutantDB/

Las estadísticas se pueden visualizar desde un HTTP GET -> /stats.

Pruebas
-------------

Para la realización de pruebas se puede hacer uso de los siguientes datos:
ADN - Mutante
```
dna =["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
``` 
ADN - Humano
```
humano = ["ATGCGA","CCGTGC","TTATAT","ATAAGG","CCTCTA","TCACTC"]
```
ADN - con fallas
```
["ATGCGA","CGTGC","TPATAT","ATAAGG","CCTCTA","TCACTC"]
```  





