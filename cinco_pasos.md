## PASO 1 DEFINE EL PROBLEMA: 
Una tienda necesita un programa en C que calcule el precio final de un producto aplicando siempre el mismo IVA del 16 % (valor que nunca debe cambiar en todo el sistema). Sin embargo, el precio del producto sí varía según el artículo. Si alguien accidentalmente modifica el porcentaje de IVA dentro del código, el cálculo se vuelve incorrecto. ¿Cómo garantizamos que el IVA permanezca fijo y el precio pueda cambiar?

## PASO 2 PLANTEA UNA SOLUCIÓN: 
precio_final = precio_original + (precio_original*16/100)
Ejemplo: precio_original=100.0
precio_final=
100+(100*16/100)=116

## PASO 3 DISEÑA UN ALGORITMO: 
DEFINE IVA=16, precio_original, precio_final
ASIGNA precio=100
precio_final = precio_original + (precio_original*IVA/100.0)
ESCRIBE (“Precio original”, precio_original)
ESCRIBE (“IVA aplicado”,IVA)
ESCRIBE (“Precio final”, precio_final)

## PASO 4 CONVIERTE EL ALGORITMO EN UN PROGRAMA: 
#include <stdio.h>
#define IVA 16
int main() {
float precio = 100.0;
float precioFinal;
precioFinal = precio * (1 + IVA / 100.0);
printf("Precio original: %.2f\n", precio);
printf("IVA aplicado: %d%%\n", IVA);
printf("Precio final: %.2f\n", precioFinal);
return 0;
}

## PASO 5 VERIFICA LA OPERACIÓN DEL PROGRAMA: 