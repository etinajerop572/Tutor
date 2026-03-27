# Constantes y variables

### Objetivo de la lección

El participante describirá las diferencias entre una constante y una variable ambas implementadas en un programa escrito en el lenguaje C que se compila y ejecuta correctamente

### Al finalizar esta lección el estudiante será capaz de:

* Conoce el término de variable  
* Conoce el término de constante  
* Conoce el procedimiento para declarar una variable  
* Conoce el procedimiento para declarar una constante  
* Puede describir la diferencia entre una constate y una variable  

### ¿Qué es una variable?
Antes de comenzar a programar en un lenguaje de programación debemos considerar la necesidad de las computadoras de almacenar datos en su memoria que muchas veces puede ser la memoria RAM o en el dispositivo de almacenamiento masivo de datos. 
Los programas almacenados en la memoria RAM en tiempo de ejecución trabajan con diferentes tipos de datos de entre los cuales podemos considerar a los datos numéricos o a las cadenas de texto. 
En el lenguajes de programación C se utilizan variables para almacenar diferentes tipos de datos, Aitken y Jones, (1994) definen una variable como sigue:
“Una variable es una posición de almacenamiento de datos de la memoria de la computadora que tiene un nombre. Al usar el nombre de variable en el programa de hecho se está haciendo referencia al dato que se encuentra guardado ahí”(p. 37). Es por lo anteriormente citado que debemos asignar un nombre a una variable. Este nombre no puede ser algo asignado al azar sino que debe cumplir con ciertas reglas para ser considerado como un nombre válido por el compilador. 
Las variables en el lenguaje C deben nombrarse según la siguiente regla:
* El primer elemento de una variable debe ser una letra mayúscula o minúscula, o los caracteres guion bajo _ y signo de dólar $  
* Las letras mayúsculas y minúsculas son importantes por lo que la declaración de variables es sensible a su uso  
* Los compiladores de C toman en cuenta los primeros treinta y dos caracteres de una variable  
* Las palabras reservadas no pueden ser utilizadas como nombres de variables  
* Por lo general las variables se escriben en minúsculas y las constantes en mayúsculas  
* Para el nombre de variables con varias palabras se pueden utilizar dos estilos. El primero utiliza un guion bajo para separar las palabras como por ejemplo tasa_interes. El segundo estilo es la notación de camello en la cual se pone en mayúscula la primera letra de cada palabra y se yuxtaponen en una sola, por ejemplo TasaInteres  

Lista de palabras reservadas en el lenguaje C: auto, break, case, char, const, continue, default, do, double, else, enum, extern, float, for, goto, if, int, long, register, return, short, signed, sizeof, static, struct, switch, typedef, union, unsigned, void, volatile y while.

Las variables numéricas en el lenguaje C se pueden clasificar en dos categorías: tipos de datos enteros y tipos de datos de punto flotante.  
Los tipos de datos enteros se dividen en dos categorías: con signo (signed) y sin signo (unsigned). El tamaño de los números enteros depende del tamaño del bus del procesador, desde 16, 32 o 64 bits. 
El lenguaje C tiene tipos de datos long para enteros grandes y también short para enteros pequeños.
Podemos especificar un tipo entero como long, short, signed o unsigned en las siguientes seis combinaciones: short int, unsigned short int, int, unsigned int, long int y unsigned long int. 
Los rangos típicos de los tipos de datos enteros en máquinas de 64 bits considerando datos en 16, 32 y 64 bits de longitud se describen a continuación.
Los tipos de datos flotantes representan números reales con parte decimal. En el lenguaje C se tienen tres tipos de datos flotantes: float los cuales son números de precisión simple, los números de tipo double los cuales son números de doble precisión y los números de tipo long double los cuales son números con precisión extendida.

|Tipo de dato|Número de bits|Valor mínimo|Valor máximo|
| --- | --- | --- | --- |
|short int|16|-(2^15) o bien -32,768|(2^15) o bien 32,768|
|int|32|-(2^31) o bien -2,147,483,648|(2^31-1) o bien 2,147,483,647|
|long int|64|-(2^63) o bien -9,223,372,036,854,775,808|(2^63-1) o bien 9, 223, 372,036,854,775,807|
|unsigned int|32|0|(2^32-1) o bien 4,294,967,295|
|unsigned long int|64|0|(2^32-1) o bien 18,446,744,073,709,551,615|
|float|64|1.17549x10^-38|3.40282x10^38|
|double|64|2.22507x10^-308|1.79769x10^308|

### ¿Cómo declarar una variable?
Conoce el procedimiento para declarar una variable

En el lenguaje C es necesario declara una variable antes de utilizarla. En caso de que se pretenda utilizar una variable sin ser declarada previamente se lanzará un error en el tiempo de compilación.
Para declara una variable debemos seguir la siguiente estructura básica:
nombre de tipo nombre de variable = valor inicial;

El nombre de tipo se refiere al tipo de variable el cual se definió en la sección anterior de entre los cuales puede ser un tipo de dato entero o un tipo de dato de punto flotante.
El nombre de variable se refiere al nombre de la variable siguiendo las reglas establecidas en la sección anterior.
Antes de usar una variable es una buena práctica asignarle un valor inicial el cual debe corresponder al tipo de dato. La razón de asignar un valor inicial es porque el compilador puede almacenar valores indeseados en tiempo de ejecución en caso contrario.

int contador = 0;
double incremento = 0,01;

Cuando escribamos código en el lenguaje C podemos declarar varias variables del mismo tipo en una misma línea separando los nombres de las variables por comas. Posteriormente se deben inicializar las variables por separado con un signo de igual y el valor asignado.

int contador, numero, cambio;
double hx, hy, incremento;

¿Qué es una constante?
Existen dos tipo de constantes, las constantes literales y las constantes simbólicas.
Las constantes literales son valores asignados a una variable que se mantiene según fue asignada.
Las constantes simbólicas están representadas por un nombre y su valor no puede cambiar. Cada vez que se requiere utilizar la constante se usa su nombre.

¿Cómo declarar una constante?
Una constante literal se declara en el lenguaje C tal y como se declaran las variables.

int contador = 0;
float impuesto = 0.16;

Las constantes literales de punto flotante se escriben utilizando un punto decimal para dividir la parte entera de la parte decimal pero también al escribir un punto al final indica al compilador que el valor es un valor de doble precisión. Asimismo, se puede utilizar la notación científica utilizando la letra E ó e después de un número decimal para indicar que es un número elevado a la potencia después de la letra e ó E.

float delta = 0.01;
float gamma = 1.23e3;
float eta = 2.82E-6;

Las constantes literales enteras se escriben como valores numéricos sin punto decimal y pueden ser de tres tipos: decimales, octales y hexadecimales.
Una constante literal octal se declara iniciando con el dígito 0 y utiliza los dígitos 0 a7. Por otro lado, una constate hexadecimal inicia con 0x ó 0X y los dígitos 0 a 9  y las letras A a F.
Puede describir la diferencia entre una constate y una variable
Aitken y Jones, (1994) define una constante en el lenguaje C como sigue: “De manera similar a las variables, una constante es una posición de almacenamiento de datos usada por el programa. A diferencia de la variable, el valor guardado en una constante no puede ser cambiado durante la ejecución del programa” (p. 44). Las constantes en el lenguaje C mantienen sus valores durante el tiempo de ejecución mientras que una variable puede cambiar su valor en tiempo de ejecución.

**REFERENCIAS**

Aitken, P. G., & Jones, B. (1994). Aprendiendo C en 21 días. Sams.