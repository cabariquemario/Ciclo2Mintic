
# Reto 2: Programa para recomentar eventos sociales a clientes según gustos y ciudad de ubicación
# Creador: Mario Cabarique
# Fecha: 23-may-2021

from pprint import pprint

def recomendaciones_evento(d: dict)-> dict:
    '''
    Programa de recomendación de eventos sociales según gustos
    input: diccionario con la siguiente estructura
        d = {'nombre_cliente': str,
             'apellido': str,
             'tarjeta_gold': bool,
             'bailar': bool,
             'salsa': bool,
             'mambo': bool,
             'edad': int}
    output: diccionario con la siguiente estructura
        respuesta = {'usuario':d['nombre_usuario'],
                     'recomendación': r,
                     'valor_pagar': v}
    '''
    
    # Buscar recomendación según intereses
    if d['edad'] >= 18:
        if d['bailar'] == 1:
            if d['salsa'] == 1:
                if d['mambo'] == 1:
                    if d['remix'] == 1:
                        r = 'Rumbódromo'
                    else:
                        r = 'Encuentro de melómanos'
                else:
                    r = 'Salsa para todos'
            else:
                r = 'Integración multicultural'
        else:
            if d['remix'] == 1:
                r = 'Encuentro ranchenato bailable'
            else:
                r = 'Integración multifamiliar'
    else:
        if d['bailar'] == 1:
            if d['salsa'] == 1:
                if d['mambo'] == 1:
                    if d['remix'] == 1:
                        r = 'Encuentro infantil de baile categoría remix'
                    else:
                        r = 'Competencia infantil de baile'
                else:
                    r = 'Historia de la salsa'
            else:
                r = 'Evento cultural para todos'
        else:
            r = 'Integración infantil, ¡cultura para todos!'
    
    # calcular  precio según elección
    precio_base = 4000
    if d['tarjeta_gold'] == 1:
        if r == 'Rumbódromo':
            v = precio_base*0.75 # 25% descuento
        elif r == 'Historia de la salsa':
            v = precio_base*0.60 # 40% descuento
        else:
            v = precio_base*1 # tarifa completa
    else:
        v = precio_base*1 # tarifa completa
    # v = float(v)
    
    # Armar estructura de salida del mensaje
    respuesta = {'usuario':d['nombre'] + ' ' + d['apellido'],
                 'recomendación': r,
                 'valor_pagar': v}
    return respuesta

datos_persona1 = {
    "nombre": "Fabian",
    "apellido": "Sanchéz",
    "tarjeta_gold": 1,
    "bailar": 1,
    "salsa": 1,
    "mambo": 1,
    "remix": 1,
    "edad": 18
}
datos_persona2 = {
    "nombre": "Juliana",
    "apellido": "Ortega",
    "tarjeta_gold": 1,
    "bailar": 1,
    "salsa": 1,
    "mambo": 0,
    "remix": 1,
    "edad": 22
}
datos_persona3 = {
    "nombre": "Juan",
    "apellido": "Perea",
    "tarjeta_gold": 0,
    "bailar": 1,
    "salsa": 1,
    "mambo": 0,
    "remix": 0,
    "edad": 12
}

d = {'nombre': 'Mario',
     'apellido': 'Cabarique',
     'tarjeta_gold': 'True',
     'bailar': False,
     'salsa': False,
     'mambo': False,
     'remix': False,
     'edad': 29}

print(recomendaciones_evento(d))
print(recomendaciones_evento(datos_persona1))
print(recomendaciones_evento(datos_persona2))
print(recomendaciones_evento(datos_persona3))
print('-%$'*80)
pprint(recomendaciones_evento(datos_persona1))
pprint(recomendaciones_evento(datos_persona2))
pprint(recomendaciones_evento(datos_persona3))
