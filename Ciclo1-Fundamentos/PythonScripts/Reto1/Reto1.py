
# Reto 1: calcular promedio por las ventas de la semana de un vendedor
# Creador: Mario Cabarique
# Fecha: 08-may-2021


def promedioVentas(nombre:str, v1:int, v2:int, v3:int, v4:int, v5:int) -> str:
    
    '''
    Función para calcular comisión de ventas de la semana de un vendedor
    input: nombre, v1, v2, v3, v4, v5
    output: mensaje con la comisión y el promedio de venta del vendedor
    '''

    porcentaje = 0.35
    comm     = ((v1 + v2 + v3 + v4 + v5) * porcentaje)
    promedio = round((v1 + v2 + v3 + v4 + v5) / 5, 1)
    # mensaje = f"La comisión obtenida por las ventas es de {comm} y el promedio de las ventas para {nombre} es: {promedio}"
    mensaje = "La comisión obtenida por las ventas es de {} y el promedio de las ventas para {} es: {}".format(comm,nombre,promedio)
    return mensaje

respuesta = promedioVentas('Juan Carlos', 200, 100, 150, 180, 500)
print(respuesta)
