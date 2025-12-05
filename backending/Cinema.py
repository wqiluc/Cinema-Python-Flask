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
        "O Poderoso Chefão",
        "O Poderoso Chefão II",
        "O Poderoso Chefão III",

        "Scarface",

        "Capitão América: O Primeiro Vingador",
        "Capitão Marvel",
        "Homem de Ferro",
        "Homem de Ferro 2",
        "O Incrível Hulk",
        "Thor",
        "Os Vingadores",
        "Homem de Ferro 3",
        "Thor: O Mundo Sombrio",
        "Capitão América: O Soldado Invernal",
        "Guardiões da Galáxia",
        "Guardiões da Galáxia Vol. 2",
        "Vingadores: Era de Ultron",
        "Homem-Formiga",
        "Capitão América: Guerra Civil",
        "Pantera Negra",
        "Viúva Negra",
        "Homem-Aranha: De Volta ao Lar",
        "Doutor Estranho",
        "Thor: Ragnarok",
        "Homem-Formiga e a Vespa",
        "Vingadores: Guerra Infinita",
        "Vingadores: Ultimato",
        "Homem-Aranha: Longe de Casa",
        "Shang-Chi e a Lenda dos Dez Anéis",
        "Eternos",
        "Homem-Aranha: Sem Volta Para Casa",

        "A Origem",
        "Interestelar",
        "O Lobo de Wall Street",

        "Matrix",
        "Matrix Reloaded",
        "Matrix Revolutions",
        "Matrix Resurrections",

        "Avatar",
        "Avatar 2: O Caminho da Água",

        "John Wick",
        "John Wick 2",
        "John Wick 3: Parabellum",
        "John Wick 4",

        "Clube da Luta",

        "O Senhor dos Anéis: A Sociedade do Anel",
        "O Senhor dos Anéis: As Duas Torres",
        "O Senhor dos Anéis: O Retorno do Rei",
        "O Hobbit: Uma Jornada Inesperada",
        "O Hobbit: A Desolação de Smaug",
        "O Hobbit: A Batalha dos Cinco Exércitos",

        "Homem-Aranha (2002)",
        "Homem-Aranha 2(2004)",
        "Homem-Aranha 3(2007)",

        "O Espetacular Homem-Aranha",
        "O Espetacular Homem-Aranha 2",

        "Homem-Aranha: De Volta ao Lar",
        "Homem-Aranha: Longe de Casa",
        "Homem-Aranha: Sem Volta Para Casa",
        "Homem-Aranha no Aranhaverso",
        "Homem-Aranha Através do Aranhaverso",
        "Homem-Aranha Além do Aranhaverso  ",
        "Homem-Aranha: Um novo dia",

        "Batman Begins",
        "Batman: O Cavaleiro das Trevas",
        "Batman: O Cavaleiro das Trevas Ressurge",
        "The Batman",

        "Gladiador",
        "Gladiador 2",

        "Forrest Gump",

        "O Resgate do Soldado Ryan",

        "Jurassic Park",
        "Jurassic Park 2: O Mundo Perdido",
        "Jurassic Park 3",
        "Jurassic World",
        "Jurassic World: Reino Ameaçado",
        "Jurassic World: Domínio",

        "Velozes e Furiosos",
        "Mais Velozes e Mais Furiosos",
        "Velozes e Furiosos: Desafio em Tóquio",
        "Velozes e Furiosos 4",
        "Velozes e Furiosos 5: Operação Rio",
        "Velozes e Furiosos 6",
        "Velozes e Furiosos 7",
        "Velozes e Furiosos 8",
        "Velozes e Furiosos 9",
        "Velozes e Furiosos 10",

        "Mad Max",
        "Mad Max 2: A Caçada Continua",
        "Mad Max 3: Além da Cúpula do Trovão",
        "Mad Max: Estrada da Fúria",
        "Furiosa: Uma Saga Mad Max",

        "Top Gun",
        "Top Gun: Maverick",

        "Procurando Nemo",
        "Procurando Dory",
        "Toy Story",
        "Toy Story 2",
        "Toy Story 3",
        "Toy Story 4",
        "Toy Story 5",
        "Shrek",
        "Shrek 2",
        "Shrek Terceiro",
        "Shrek Para Sempre",

        "Piratas do Caribe: A Maldição do Pérola Negra",
        "Piratas do Caribe: O Baú da Morte",
        "Piratas do Caribe: No Fim do Mundo",
        "Piratas do Caribe: Navegando em Águas Misteriosas",
        "Piratas do Caribe: A Vingança de Salazar",

        "Harry Potter e a Pedra Filosofal",
        "Harry Potter e a Câmara Secreta",
        "Harry Potter e o Prisioneiro de Azkaban",
        "Harry Potter e o Cálice de Fogo",
        "Harry Potter e a Ordem da Fênix",
        "Harry Potter e o Enigma do Príncipe",
        "Harry Potter e as Relíquias da Morte – Parte 1",
        "Harry Potter e as Relíquias da Morte – Parte 2",

        "Animais Fantásticos e Onde Habitam",
        "Animais Fantásticos: Os Crimes de Grindelwald",
        "Animais Fantásticos: Os Segredos de Dumbledore"]


def menu_sessoes():
    return ["10:00","11:00","12:00","13:00","15:00","16:00","17:00","18:00",
            "19:00","20:00","21:00","22:00","23:00"]

def menu_forma_de_pagamento():
    return ["Dinheiro","Cartão"]
