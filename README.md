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

### Si usa Windows
Para ejecutar el proyecto, dentro de la carpeta principal del repositorio (dónde solo se puedan observar las carpetas Proyecto y Pruebas, en terminal ejecute el siguiente código:
</br>
<code>py Proyecto/main.py </code>
</br>
Con todo esto poco a poco van a ir apareciendo las gráficas comparando distintos tiempos de ejecución de distintos algoritmos de encriptación, los cuales tendrá que cerrar para poder avanzar a la siguiente parte del proyecto. Una vez terminado de ejecutar todos los algoritmos y visto todas las gráficas, toda la información recolectada se guardarán en <i>Texto.txt</i> para que usted a detalle pueda analizarlo después.

### Si usa Linux
Debido a que algunas cosas no se podrán hacer de manera automática, se tendrán que hacer de manera manual, por lo que primero se tenrá que instalar las librerias manualmente ejecutando desde dentro de la carpeta principal del repositorio (dónde solo se puedan observar las carpetas Proyecto y Pruebas, en terminal ejecute el siguiente código:
</br>
<code>pip install -r Proyecto/requirements.txt</code>
</br>
Una vez terminado de instalar las liberrias necesarias, desde la misma localización, ejecutar el siguiente código para iniciar el programa:
</br>
<code>python3 Proyecto/EjecutarProyecto.py</code>
