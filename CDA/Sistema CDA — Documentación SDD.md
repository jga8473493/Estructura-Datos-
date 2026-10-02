CDA

# Sistema de atención CDA

Documentación SDD (Desarrollo Dirigido por Especificación): Requisitos → Diseño → Tareas → Implementación

## Resumen

Sistema de consola en Python que gestiona la atención de vehículos en un Centro de Diagnóstico Automotor. Permite registrar vehículos (tipo, placa colombiana validada, marca y color), consultar cuál sigue, atenderlo, retirarlo de la cola por placa y ver cuántos faltan.

Los **vehículos especiales** (ambulancia, bomberos, policía) tienen atención prioritaria.

### Problema y objetivo

### Problema

Atender solo por orden de llegada no contempla vehículos especiales, que requieren prioridad.

### Objetivo

Atender primero a los especiales y mantener el orden de llegada entre los demás.

### Usuarios

## Historias de usuario y criterios de aceptación

## Requisitos funcionales

| ID | Requisito | Origen |
| --- | --- | --- |

## Requisitos no funcionales

| ID | Requisito |
| --- | --- |

## Dos colas, una prioridad

Siempre se atiende primero la fila de especiales. Cuando está vacía, se pasa a la normal.

Registro: el tipo de vehículo decide a qué fila entra

### Cola de especiales se atiende primero

Sale ▶ABC123DEF456

### Cola normales solo si no hay especiales

Sale ▶GHI78JKLM789NOP12Q

Dentro de cada fila el orden es de llegada (FIFO).

## Reglas de priorización

1. Los especiales se atienden antes que los normales.
2. Entre especiales, por orden de llegada.
3. Entre normales, por orden de llegada.
4. Un normal solo se atiende cuando no hay especiales pendientes.

## Modelo del vehículo

### Campos (en orden)

1\. Tipo (lista fija)\
2\. Placa (validada)\
3\. Marca\
4\. Color (solo letras)

### Placas colombianas

Carro y especiales: `^[A-Z]{3}\d{3}$` → ABC123\
Moto: `^[A-Z]{3}\d{2}[A-Z]$` → ABC12D

## Operaciones

| Operación | Lógica | RF |
| --- | --- | --- |
| `registrar` | Rechaza placa repetida. Especial a su cola, normal a la suya. | RF-01 a 03 |
| `siguiente` | Primero de especiales; si no hay, de normales. No retira. | RF-04 a 06 |
| `atender` | Como siguiente, pero lo retira. | RF-07 |
| `pendientes` | Suma el tamaño de ambas colas. | RF-08 |
| `retirar(placa)` | Busca la placa en ambas colas y la saca. | RF-11 |

**Decisión de diseño:** dos colas en lugar de una ordenada. Registrar y atender no recorren toda la cola y el orden se mantiene solo (RNF-02).

**Archivos:** `vehiculo.py` (modelo y validación) · `cola_cda.py` (operaciones) · `main.py` (menú) · `pruebas.py` (una prueba por CA)

## Tareas

| ID | Tarea | Archivo | RF | Estado |
| --- | --- | --- | --- | --- |

Orden seguido: T-01 → T-02 a T-06 → T-08 → T-07 → T-09 → T-10.
