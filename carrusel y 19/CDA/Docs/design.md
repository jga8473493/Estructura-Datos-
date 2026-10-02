# Diseño — Sistema CDA

## 1. Estructura de datos
Dos colas FIFO (deque):
- cola_especiales
- cola_normales

Un conjunto (set) de placas pendientes para detectar duplicados rápidamente.

## 2. Modelo Vehículo
Atributos: tipo, placa, marca, color, es_especial (se calcula por el tipo).

- Tipos válidos: carro, moto, ambulancia, bomberos, policia.
- Tipos especiales: ambulancia, bomberos, policia.
- Validación de placa por RegEx según el tipo:
  - Carro (y especiales): `^[A-Z]{3}\d{3}$` (ejemplo: ABC123)
  - Moto: `^[A-Z]{3}\d{2}[A-Z]$` (ejemplo: ABC12D)

## 3. Reglas de priorización
1. Los vehículos especiales se atienden antes que los normales.
2. Entre especiales, se atiende por orden de llegada.
3. Entre normales, se atiende por orden de llegada.
4. Un vehículo normal solo se atiende cuando no hay especiales pendientes.

## 4. Operaciones
| Operación | Lógica | RF |
|-----------|--------|----|
| registrar(vehiculo) | Rechaza si la placa ya está pendiente. Si es especial va a cola_especiales, si no a cola_normales | RF-01 a RF-03 |
| siguiente() | Devuelve el primero de especiales; si no hay, el primero de normales; si ambas están vacías, devuelve None. No retira | RF-04 a RF-06 |
| atender() | Igual que siguiente(), pero lo retira de su cola | RF-07 |
| pendientes() | Suma el tamaño de ambas colas | RF-08 |
| retirar(placa) | Busca la placa en ambas colas y la retira; si no existe, devuelve None | RF-11 |
| ordenados() | Devuelve especiales + normales en orden de atención (lo usa la interfaz) | RF-04, RF-05 |

## 5. Formulario de registro (orden de campos)
1. Tipo de vehículo: opciones fijas, sin texto libre (RF-10). En consola es una lista numerada; en la interfaz gráfica, una lista desplegable.
2. Placa: texto validado con RegEx según el tipo (RF-09).
3. Marca: texto obligatorio.
4. Color: texto obligatorio, solo letras.

## 6. Decisión de diseño
Dos colas en vez de una cola ordenada: registrar y atender son O(1) y el orden
dentro de cada grupo se mantiene solo (RNF-02).

## 7. Estructura de archivos
- vehiculo.py: clase Vehiculo, tipos válidos y validar_placa().
- cola_cda.py: clase ColaCDA con las operaciones (la lógica del sistema).
- main.py: menú de consola.
- interfaz.py: interfaz gráfica (tkinter) que reutiliza ColaCDA.
- pruebas.py: una prueba por cada criterio de aceptación.
