# Especificación del TAD Carrito

## Ambigüedades Decididas
1. **Sacar producto inexistente:** Lanza ValueError.
2. **Cantidad menor o igual a cero:** Lanza ValueError.
3. **Modo de extracción:** Resta unidades; si llega a 0 se elimina el producto.
4. **Carrito vacío:** obtener_total_items retorna 0.
