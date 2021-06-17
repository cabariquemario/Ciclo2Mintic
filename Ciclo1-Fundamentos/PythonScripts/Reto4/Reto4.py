
def max_transacciones_anuales (d: dict) -> tuple:
    '''
    Función que recibe un diccionario de tiendas y transacciones por mes
        Debe calcular promedios ponderados por tienda.
        Debe retornar la mejor tienda con el mejor promedio anual

    input: diccioario con tiendas y ventas con transacciones por mes
    output: tupla con la siguiente estructura (cod_nit, empresa, promedio)

    '''
    
    def concatenarValores(l:list) -> str:
        '''
        Función para concatenar los elementos de una lista como string
        input: lista con elementos
        output: string concatenado de los elementos de la lista
        '''
        r = ''
        for i in l:
            r = r + (str(i))
        return r

    meses = ['enero','febrero','marzo','abril','mayo','junio', 
            'julio', 'agosto','septiembre','octubre','noviembre','diciembre']
    sedes = ['sede1', 'sede2', 'sede3', 'sede4']
    comparador = []
    promedios = []

    for i in list(datos.keys()):
        # print(i)
        tresLetras = datos[i]['empresa'][:3]
        nit = datos[i]['nit']
        pares   = [int(i) for i in list(nit) if int(i) % 2 == 0]
        impares = [int(i) for i in list(nit) if int(i) % 2 != 0]
        sumaImpares = sum(impares)
        listaValores = [i*sumaImpares for i in pares]
        valorConcatenado = concatenarValores(listaValores)
        resParte1 = tresLetras+valorConcatenado
        resParte2 = datos[i]['empresa']
        
        
        acumulado = 0
        for j,k in enumerate(meses):
            # print(j,k)
            acumulado = acumulado + sum(datos[i]['transacciones'][j][k].values())

        resParte3 = round(acumulado/(len(meses)*len(sedes)),2)

        resultado = (resParte1,resParte2,resParte3)
        comparador.append(resultado)
        promedios.append(resParte3)

    indiceElemento = promedios.index(max(promedios))
    respuesta = comparador[indiceElemento]

    return respuesta

# ('Ali120906030', 'AliExpress', 213.81)
datos = {
"01": {
"empresa": "MercadoLibre",
"nit": "12345678",
"url": "www.mercadolibre.com.co",
"transacciones": [
{
"enero": {
"sede1": 258,
"sede2": 100,
"sede3": 200,
"sede4": 250
}
},
{
"febrero": {
"sede1": 100,
"sede2": 50,
"sede3": 20,
"sede4": 250
}
},
{
"marzo": {
"sede1": 10,
"sede2": 50,
"sede3": 200,
"sede4": 25
}
},
{
"abril": {
"sede1": 100,
"sede2": 500,
"sede3": 200,
"sede4": 250
}
},
{
"mayo": {
"sede1": 40,
"sede2": 50,
"sede3": 20,
"sede4": 250
}
},
{
"junio": {
"sede1": 200,
"sede2": 50,
"sede3": 200,
"sede4": 250
}
},
{
"julio": {
"sede1": 300,
"sede2": 50,
"sede3": 200,
"sede4": 150
}
},
{
"agosto": {
"sede1": 100,
"sede2": 150,
"sede3": 200,
"sede4": 250
}
},
{
"septiembre": {
"sede1": 100,
"sede2": 510,
"sede3": 100,
"sede4": 250
}
},
{
"octubre": {
"sede1": 100,
"sede2": 50,
"sede3": 100,
"sede4": 250
}
},
{
"noviembre": {
"sede1": 100,
"sede2": 50,
"sede3": 100,
"sede4": 250
}
},
{
"diciembre": {
"sede1": 100,
"sede2": 50,
"sede3": 100,
"sede4": 150
}
}
]
},
"02": {
"empresa": "AliExpress",
"nit": "7865432",
"url": "www.aliexpress.com",
"transacciones": [
{
"enero": {
"sede1": 258,
"sede2": 100,
"sede3": 200,
"sede4": 2500
}
},
{
"febrero": {
"sede1": 1000,
"sede2": 550,
"sede3": 200,
"sede4": 250
}
},
{
"marzo": {
"sede1": 100,
"sede2": 50,
"sede3": 400,
"sede4": 250
}
},
{
"abril": {
"sede1": 200,
"sede2": 50,
"sede3": 200,
"sede4": 50
}
},
{
"mayo": {
"sede1": 100,
"sede2": 50,
"sede3": 100,
"sede4": 250
}
},
{
"junio": {
"sede1": 300,
"sede2": 50,
"sede3": 200,
"sede4": 250
}
},
{
"julio": {
"sede1": 50,
"sede2": 50,
"sede3": 100,
"sede4": 150
}
},
{
"agosto": {
"sede1": 100,
"sede2": 50,
"sede3": 100,
"sede4": 250
}
},
{
"septiembre": {
"sede1": 100,
"sede2": 350,
"sede3": 100,
"sede4": 50
}
},
{
"octubre": {
"sede1": 100,
"sede2": 50,
"sede3": 20,
"sede4": 25
}
},
{
"noviembre": {
"sede1": 100,
"sede2": 50,
"sede3": 200,
"sede4": 250
}
},
{
"diciembre": {
"sede1": 10,
"sede2": 50,
"sede3": 50,
"sede4": 250
}
}
]
}
}

print(max_transacciones_anuales (datos))
# # print(datos)
# print('-'*80)
# print('Longitud de datos: {}'.format(len(datos)))
# print('-'*80)
# print()

# def concatenarValores(l:list) -> str:
#     '''
#     Función para concatenar los elementos de una lista como string
#     input: lista con elementos
#     output: string concatenado de los elementos de la lista
#     '''
#     r = ''
#     for i in l:
#         r = r + (str(i))
#     return r

# # print(concatenarValores([120, 90, 60, 30]))

# meses = ['enero','febrero','marzo','abril','mayo','junio', 
#          'julio', 'agosto','septiembre','octubre','noviembre','diciembre']
# sedes = ['sede1', 'sede2', 'sede3', 'sede4']
# comparador = []
# promedios = []

# for i in list(datos.keys()):
#     print(i)
#     tresLetras = datos[i]['empresa'][:3]
#     nit = datos[i]['nit']
#     pares   = [int(i) for i in list(nit) if int(i) % 2 == 0]
#     impares = [int(i) for i in list(nit) if int(i) % 2 != 0]
#     sumaImpares = sum(impares)
#     listaValores = [i*sumaImpares for i in pares]
#     valorConcatenado = concatenarValores(listaValores)
#     resParte1 = tresLetras+valorConcatenado
#     resParte2 = datos[i]['empresa']
    
    
#     acumulado = 0
#     for j,k in enumerate(meses):
#         # print(j,k)
#         acumulado = acumulado + sum(datos[i]['transacciones'][j][k].values())

#     resParte3 = round(acumulado/(len(meses)*len(sedes)),2)
    
#     print(f'tresLetras: {tresLetras}')
#     print(f'nit: {nit}')
#     print(f'pares: {pares}')
#     print(f'impares: {impares}')
#     print(f'sumaImpares: {sumaImpares}')
#     print(f'listaValores: {listaValores}')
#     print(f'valorConcatenado: {valorConcatenado}')
#     print(f'resParte1: {resParte1}')
#     print(f'resParte2: {resParte2}')
#     print(f'acumulado: {acumulado}')
#     print(f'resParte3: {resParte3}')
#     print('-'*80)
#     resultado = (resParte1,resParte2,resParte3)
#     print(resultado)
#     comparador.append(resultado)
#     promedios.append(resParte3)

# print(comparador)
# print(max(promedios))
# print('$'*80)
# print(promedios.index(max(promedios)))
# print([i for i in comparador if i[0][2]==max(promedios)])
# print(comparador[0][2])
    # print(list(datos[i]['transacciones'][0].keys()))

