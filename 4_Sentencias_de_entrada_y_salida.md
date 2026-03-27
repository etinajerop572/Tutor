# Sentencias de entrada y salida

### Objetivo de la lección

El participante explicará cómo utilizar sentencias de entrada y salida en un programa escrito en el lenguaje C que se compila y ejecuta correctamente

### Al finalizar esta lección el estudiante será capaz de:

* Conoce el término de sentencia de entrada
* Conoce el término de sentencia de salida
* Conoce las aplicaciones de las sentencias de entrada
* Conoce las aplicaciones de las sentencias de salida
* Puede explicar cómo utilizar sentencias de entrada y salida en un programa

### printf()

Cuando se programa en el lenguaje C muchas veces es necesario visualizar en pantalla la salida de la ejecución del programa. La forma más sencilla de realizar esta visualización es con el uso de la función printf() la cual se describe a continuación.

Para desplegar una cadena de texto en pantalla, debemos escribir entre comillas dobles dicho texto y pasarlo a la función printf() como se muestra a continuación. En este ejemplo se despliega en pantalla la cadena ¡Hola mundo!

printf(“¡Hola mundo!”);

El formato de la salida se puede ver afectado por una secuencia de escape las cuales se enuncian a continuación.

|Secuencuencia|Significado|
| --- | --- |
|\a|Campana|
|\b|Retroceso|
|\n|Nueva línea|
|\t|Tabulador horizontal|
|\\|Diagonal inversa|
|\?|Signo de interrogación|
|\'|Comilla simple|
|\"|Comillas dobles|

Además de texto, muchas veces es necesario desplegar en pantalla el valor almacenado en una variable junto al texto lo cual se realiza utilizando especificadores de conversión las cuales se describen a continuación.

|Especificador|Significado|
| --- | --- |
|%c|Un carácter|
|%d|Número entero|
|%f|Número decimal|
|%s|Cadena de caracteres|
|%u|Entero sin signo|

El número de especificadores de conversión debe corresponder con el número de variables a las que hacen referencia. En caso de que no se cumpla lo anterior,  si hay más variables que especificadores de conversión en ese caso las variables que no hacen par no se imprimen; en caso de que existan más especificadores que variables entonces se pueden generar salidas en la pantalla que no representen valores válidos.