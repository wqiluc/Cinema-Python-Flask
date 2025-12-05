acumuladores = {
    "valor_usuario": 0,
    "ingressos_usuario": 0,
    "valor_dia": 0,
    "ingressos_dia": 0,
    "vendas_dia": 0,
    "inteira": 0,
    "meia": 0,
    "promocional": 0,
    "gratuita": 0}

def calcular_valor(tipo, idade):
    precos = {1: 30, 2: 15, 3: 21, 4: 0}
    if idade < 5:
        return 0
    return precos.get(tipo, 0)


def registrar_ingresso(tipo, idade):
    valor = calcular_valor(tipo, idade)
    
    acumuladores["ingressos_dia"] += 1
    acumuladores["vendas_dia"] += valor
    
    acumuladores["valor_usuario"] += valor
    acumuladores["ingressos_usuario"] += 1

    if (tipo == 1):
        acumuladores["inteira"] += 1
    elif (tipo == 2):
        acumuladores["meia"] += 1
    elif (tipo == 3):
        acumuladores["promocional"] += 1
    elif (tipo == 4) or (idade < 5):
        acumuladores["gratuita"] += 1

    return valor

def resumo_compra_atual():
    return {"total_usuario": acumuladores["valor_usuario"],
    "ingressos_usuario": acumuladores["ingressos_usuario"]}

def resumo_dia():
    return {
        "total": acumuladores["vendas_dia"],
        "total_dia": acumuladores["valor_dia"],
        "ingressos_dia": acumuladores["ingressos_dia"],
        "inteira": acumuladores["inteira"],
        "meia": acumuladores["meia"],
        "promocional": acumuladores["promocional"],
        "gratuita": acumuladores["gratuita"],}

def zerar_compra():
    acumuladores["valor_usuario"] = 0
    acumuladores["ingressos_usuario"] = 0

def menu_filmes():
    return [
        "O Poderoso Chefão","Interestelar","A Origem","Vingadores: Ultimato",
        "O Lobo de Wall Street","Matrix","Avatar","John Wick","Clube da Luta",
        "O Senhor dos Anéis: A Sociedade do Anel","O Senhor dos Anéis: O Retorno do Rei",
        "Homem-Aranha: Sem Volta Para Casa","Batman: O Cavaleiro das Trevas",
        "Gladiador","Forrest Gump","O Resgate do Soldado Ryan","Jurassic Park",
        "Velozes e Furiosos","Mad Max: Estrada da Fúria","Top Gun: Maverick",
        "Procurando Nemo","Toy Story","Shrek","Piratas do Caribe: A Maldição do Pérola Negra",
        "Harry Potter e a Pedra Filosofal"]

def menu_sessoes():
    return ["10:00","11:00","12:00","13:00","15:00","16:00","17:00","18:00",
            "19:00","20:00","21:00","22:00","23:00"]

def menu_forma_de_pagamento():
    return ["Dinheiro","Cartão"]