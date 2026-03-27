# Operadores aritméticos

### Objetivo de la lección

El participante explicará cómo utilizar operadores y funciones matemáticas en un programa escrito en el lenguaje C que se compila y ejecuta correctamente, así como por medio de la comprobación de los resultados correctos de las operaciones conocidas

### Al finalizar esta lección el estudiante será capaz de:

* Conoce las categorías de los operadores matemáticos
* Conoce los principios de uso de los operadores matemáticos
* Puede explicar la forma de declarar a los operadores matemáticos en un programa
* Puede explicar cómo utilizar los operadores matemáticos en un programa
* Puede explicar cómo utilizar funciones matemáticas en un programa

### Operadores matemáticos

En el lenguaje C existen dos operadores matemáticos unarios porque toman un solo operando. Los operadores unarios son el incremento y el decremento.

|Operador|Símbolo|Acción|Ejemplo|
| --- | --- | --- | --- |
|Incremento|++|Incrementa al operando en una unidad|x++, ++x|
|Decremento|--|Decrementa al operando en una unidad|x--, --x|

En el lenguaje C existen operadores binarios los cuales como su nombre lo indica utilizan dos operandos. Estos operadores son los operadores aritméticos de suma, resta, multiplicación, división y módulo. 

|Operador|Símbolo|Acción|Ejemplo|
| --- | --- | --- | --- |
|Suma|+|Realiza la suma aritmética de los dos operandos|x+y|
|Resta|-|Realiza la suma aritmética de los dos operandos|x-y|
|Multiplicación|*|Realiza la multiplicación aritmética de los dos operandos|x*y|
|División|/|Realiza la división aritmética de los dos operandos|x/y|
|Módulo|%|El resultado es el residuo cuando el primer operando es dividido entre el segundo|x%y|

La precedencia de las operaciones matemáticas en el lenguaje C determinan el orden en el que se realizarán dichas operaciones. Cada operador tiene una precedencia jerárquica la cual se debe respetar al realizar operaciones aritméticas.

|Operadores|Precedencia relativa|
| --- | --- |
|++, --|Primera|
|*, /, %|Segunda|
|+, -|Tercera|




