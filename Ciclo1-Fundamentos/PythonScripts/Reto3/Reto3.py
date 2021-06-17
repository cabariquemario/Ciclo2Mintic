# Reto 3 -> ingresos por tipo de tv
# 1. Amazon Prime y 2. Netflix.
facturas = [
{
"abonado": "amazon_prime",
"valor_a_pagar": 30000
},
{
"abonado": "amazon_prime",
"valor_a_pagar": 35000
},
{
"abonado": "amazon_prime",
"valor_a_pagar": 22000
},
{
"abonado": "amazon_prime",
"valor_a_pagar": 28000
},
{
"abonado": "amazon_prime",
"valor_a_pagar": 35000
},
{
"abonado": "amazon_prime",
"valor_a_pagar": 23000
},
{
"abonado": "amazon_prime",
"valor_a_pagar": 18000
}
]

#print(facturas[0]['abonado'])

from functools import reduce # no fue usado

def calcular_ingresos(datos: list) -> dict:
    """
    Función para calcular (redondeado a 1 dígito)
    a. Total ingresos
    b. Promedio ingresos

    Según tipo de televisión streaming:
    1. Amazon Prime
    2. Netflix.

    Input: lista de diccionarios:
    abonado: “amazon_prime” o “netflix”
    valor_a_pagar: int

    Output: dicionario
    {total: int, 
    promedio_amazonprime: float, 
    promedio_netflix: float}
    """

    # Total ingresos
    def total_ingresos(datos:list) -> int:
        total:int = 0
        for i in datos:
            # print(i) # recorre cada suscripción en formato {}
            total = total + i['valor_a_pagar']
        return total
    
    # Promedios amazon_prime y netflix
    def promedio_ingresos(datos:list) -> int:
        
        promedio_amazonprime:int = 0
        promedio_netflix:int = 0

        total_amazonprime:int = 0
        total_netflix:int = 0

        for i in datos:
            # print(i) # recorre cada suscripción en formato {}
            if i['abonado'] == 'amazon_prime':
                total_amazonprime = total_amazonprime + 1
                promedio_amazonprime = promedio_amazonprime + i['valor_a_pagar']
            elif i['abonado'] == 'netflix':
                total_netflix = total_netflix + 1
                promedio_netflix = promedio_netflix + i['valor_a_pagar']
            else:
                continue
        if total_amazonprime == 0:
            promedio_amazonprime = 0
        else:
            promedio_amazonprime = round(promedio_amazonprime/total_amazonprime,1)
        if total_netflix == 0:
            promedio_netflix = 0
        else:
            promedio_netflix = round(promedio_netflix/total_netflix,1)

        return promedio_amazonprime, promedio_netflix
    
    r = {'total': int(total_ingresos(datos)),
         'promedio_amazonprime': promedio_ingresos(datos)[0],
         'promedio_netflix': promedio_ingresos(datos)[1]}

    return r

print(calcular_ingresos(facturas))

# print(facturas[0].values())

