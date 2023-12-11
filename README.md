# Segundo proyecto de criptografia

Este proyecto está diseñado para poner a prueba distintos algoritmos de criptografía post-cuánticos, para los cuáles, no se medirá ni el tiempo ni la eficiencia de ejecución de estos, es más para probar la facilidad de su implementación y las librerías necesarias. Para este proyecto se probrarán los siguientes algoritmos:
<ul>
  <li><b>ML-KEM Scheme</b></li>
  <li><b>ML-DSA Signature Scheme</b></li>
  <li><b>SLH-DSA</b></li>
</ul>

Este proyecto tomará un archivo .txt pequeño para probar los algoritmos, la razón de esto es para simpleza y velocidad, ya que lo que importa es que pueda encriptar la información, no lo rápido que haga.

## Partes de la ejecución
<ul>
  <li>
    Este programa es mucho más sencillo que el proyecto pasado, ya que para este únicamente ejecutará una vez todos los algoritmos de encriptación para verificar de que los algoritmos mencionados funcionen, con lo que solo en la terminal se imprimiran las ejecuciones y si fueron exitosas; Se espera que la ejecución sea tan corta que parezca instantaneo.
   </li>
</ul>

## Requerimientos
<ul>
  <li>Python 3.9 o superior</li>
  <li>CMake</li>
  <li>liboqs</li>
  <li>Algún compilador de C como GCC</li>
  <li>Visual Studio 2019 o 2022</li>
</ul>

## Uso
Para hacer uso del programa, primero se tiene que saber que se divide entre dos carpetas, la de <b>Proyecto</b> y la de <b>Pruebas</b>. Mientras que en la primera carpeta se encuentra el proyecto final que se entrega, en la segunda se encuentran todos los archivos que usamos para experimentos de algoritmos o funciones antes de ingresarlos al proyecto principal.
En la carpeta de <b>Proyecto</b> se encuentran los archivos más importantes:
<ul>
  <li>main.py: Es el archivo dónde se instalan las librerías necesarias para la ejecución del proyecto antes de arrancar el mismo proyecto.</li>
  <li>
    EjecutarProyecto.py: En este archivo se hacen llamadas a todos los algoritmos para su ejecución y análisis.
  </li>
  <li>
    Claves.json: Este es el archivo más importantes para el usuario, ya que dentro de este sencillo archivo podrá modificar alguno valores como la clave que se usarán en distintos algorítmos o el número de ciclos que desee ejecutar en todos los algorítmos, todo esto sin necesidad de modificar directamente el código fuente y que todo esto sea uniforme para todo el proyecto.
  </li>
</ul>

## Instalación
<ol>
  <li>

### Instalar CMake
Como primer paso de esto, para el proyecto necestiará de una herramienta multiplataforma de generación o automatización de código, en este caso vamos a hacer uso de <b>CMake</b>, para lo cual entrará en su página oficial <a>https://cmake.org/</a> y descargará la versión que va de acuerdo a su sistema operativo, ya sea el instalable o el .zip.

#### Si usa Windows
Despues de instalar o extraer sus carpetas de CMake en su computadora, queda pendiente el generar un PATH para que su sistema operativo pueda hacer uso de este, por lo que deberá ingresar a la carpeta de CMake hasta la carpeta "bin" y copiará la ruta de esta. <b>En la mayoría de las ocasiones, la ruta será:<i>C:\Program Files\CMake\bin</i></b>
Una vez copiada esta ruta, deberá ingresar a <b>Editar las variables de entorno del sistema</b> o <b>Edit the system enviroment variables</b>, dependiendo del idioma de su sistema operativo.
Una vez dentro, irá a la pestaña "Opciones avanzadas" y dará click en el botón <b>Variables de entorno...</b> para editar las variables.
Dentro de la nueva ventana abierta, en la mitad inferior llamada "Variables del sistema", donde seleccionará la variable llamada "Path" y dará click en <b>Editar...</b> para abrir un nuevo menú.
Ya dentro del menú, agregará la ruta a la carpeta bin que había copiado anteriormente hasta abajo, <b>Sin modificar alguna de las rutas que ya se encontraban antes</b>. Una vez colocado de en "Aceptar" en todo para guardar cambios.

#### Verificación
Para verificar que tenga correctamente instalado CMake, en una terminal escriba el siguiente comando.
```shell
cmake
```
  </li>
  <li>
    
## Instalar liboqs
Para instalar la librería liboqs, deberá abrir una terminal en su sistema operativo en cualquier parte que le sea comodo guardar archivos, como el escritorio o una carpeta destinada. <b>En caso de hacer uso de Windows, deberá abrir la terminal como administrador, de caso contrario no podrá instalar al 100% la librería</b>. Dentro de la terminal, deberá ingresar las siguientes líneas de comandos.
```shell
git clone --depth=1 https://github.com/open-quantum-safe/liboqs
cmake -S liboqs -B liboqs/build -DBUILD_SHARED_LIBS=ON
cmake --build liboqs/build --parallel 8
cmake --build liboqs/build --target install
```
#### Nota
En el tercer comando <i>--parallel 8</i>, el numero deberá ser de acuerdo al número de núcleos que su procesador tenga.

Despues de instalar liboqs en su computadora, queda pendiente el generar un PATH para que su sistema operativo pueda hacer uso de este, por lo que deberá ingresar a la carpeta de liboqs hasta la carpeta "bin" y copiará la ruta de esta. <b>En la mayoría de las ocasiones, la ruta será:<i>C:\Program Files (x86)\liboqs\bin</i></b>
Una vez copiada esta ruta, deberá ingresar a <b>Editar las variables de entorno del sistema</b> o <b>Edit the system enviroment variables</b>, dependiendo del idioma de su sistema operativo.
Una vez dentro, irá a la pestaña "Opciones avanzadas" y dará click en el botón <b>Variables de entorno...</b> para editar las variables.
Dentro de la nueva ventana abierta, en la mitad inferior llamada "Variables del sistema", donde seleccionará la variable llamada "Path" y dará click en <b>Editar...</b> para abrir un nuevo menú.
Ya dentro del menú, agregará la ruta a la carpeta bin que había copiado anteriormente hasta abajo, <b>Sin modificar alguna de las rutas que ya se encontraban antes</b>. Una vez colocado de en "Aceptar" en todo para guardar cambios.
  </li>
  <li>
    
### Ingresar ops al proyecto
Una vez terminado todo, ya solo quedará ingresar a la carpeta principal del proyecto e ingresar en terminal el siguiente comando:
```shell
pip install .
```
  </li>
</ol>

 ## Ejecución
  <ul>
    <li>
      
### Si usa Windows
Para ejecutar el proyecto, dentro de la carpeta principal del repositorio (dónde solo se puedan observar las carpetas Proyecto y Pruebas, en terminal ejecute el siguiente código:
```shell
py Proyecto/main.py
```
Con todo esto el programa comenzará a ejecutar cada uno de los algoritmos, imprimiendo sus resultados y confirmando su exitosa ejecución.
    </li>
    <li>
### Si usa Linux
Debido a que algunas cosas no se podrán hacer de manera automática, se tendrán que hacer de manera manual, por lo que primero se tenrá que instalar las librerias manualmente ejecutando desde dentro de la carpeta principal del repositorio (dónde solo se puedan observar las carpetas Proyecto y Pruebas, en terminal ejecute el siguiente código:
```shell
pip install -r Proyecto/requirements.txt
```
Una vez terminado de instalar las liberrias necesarias, desde la misma localización, ejecutar el siguiente código para iniciar el programa:
```shell
python3 Proyecto/EjecutarProyecto.py
```
  </li>
  </ul>
