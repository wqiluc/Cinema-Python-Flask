acumuladores = {
    "valor_usuario": 0,
    "ingressos_usuario": 0,
    "valor_dia": 0,
    "ingressos_dia": 0,
    "vendas_dia": 0,
    "inteira": 0,
    "meia": 0,
    "promocional": 0,
    "gratuita": 0,
    "combos_gerais" : 0}

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

def registrar_pipoca_e_refri():
    def pacote_pequeno():
        pipoca1 = 20
        refri1 = 10
        pacote1 = pipoca1 + refri1
        return pacote1

    def pacote_medio():
        pipoca2 = 30
        refri2 = 15
        pacote2 = pipoca2 + refri2
        return pacote2

    def pacote_grande():
        pipoca3 = 40
        refri3 = 20
        pacote3 = pipoca3 + refri3
        return pacote3
    
    combos = {
        "Pacote pequeno" : pacote_pequeno(),
        "Pacote médio" : pacote_medio(),
        "Pacote grande" : pacote_grande()
        }
    return combos
    

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
        "gratuita": acumuladores["gratuita"],
        "combos gerais": acumuladores["combos_gerais"]}

def zerar_compra():
    acumuladores["valor_usuario"] = 0
    acumuladores["ingressos_usuario"] = 0


def menu_filmes():
    return [
    # ===== MÁFIA / CRIME 🕴 ===== #
    "O Poderoso Chefão",
    "O Poderoso Chefão II",
    "O Poderoso Chefão III",
    "Scarface",
    "Os Bons Companheiros",
    "Cassino",
    "Donnie Brasco",
    "O Irlandês",
    "Carlito's Way",
    "Era Uma Vez na América",
    "Cidade de Deus",

    "Os Sopranos",

    # ===== HOMEM-ARANHA 🕷️ ===== #


    # ==== TOBEY MAGUIRE ==== #
    "Homem-Aranha (2002)",
    "Homem-Aranha 2 (2004)",
    "Homem-Aranha 3 (2007)",

    # ==== ANDREW GARFIELD ==== #
    "O Espetacular Homem-Aranha (2012)",
    "O Espetacular Homem-Aranha 2: A ameaça de Electro (2014)"
    "O Espetacular Homem-Aranha 3: Sexteto Sinistro (Estreia)",

    # ==== TOM HOLLAND ==== #
    "Homem-Aranha 1: De Volta ao Lar",
    "Homem-Aranha 2: Longe de Casa",
    "Homem-Aranha 3: Sem Volta Para Casa",
    "Homem-Aranha 4: Um Novo Dia(Estreia)",

    # ==== ARANHAVERSO ==== #
    "Homem-Aranha no Aranhaverso",
    "Homem-Aranha Através do Aranhaverso",
    "Homem-Aranha Além do Aranhaverso(Estreia)",

    # ===== DC 🦇 ===== #
    "Batman Begins",
    "Batman: O Cavaleiro das Trevas",
    "Batman: O Cavaleiro das Trevas Ressurge",
    "The Batman",
    "Coringa",
    "Coringa: Folie à Deux",

    # ===== FICÇÃO CIENTÍFICA 🧪 ===== #
    "A Origem",
    "Interestelar",
    "Matrix",
    "Matrix Reloaded",
    "Matrix Revolutions",
    "Matrix Resurrections",
    "Avatar",
    "Avatar 2: O Caminho da Água",

    # ===== AÇÃO 👊 ===== #
    "John Wick",
    "John Wick 2",
    "John Wick 3: Parabellum",
    "John Wick 4",
    "Mad Max",
    "Mad Max 2: A Caçada Continua",
    "Mad Max 3: Além da Cúpula do Trovão",
    "Mad Max: Estrada da Fúria",
    "Furiosa: Uma Saga Mad Max",
    "Top Gun",
    "Top Gun: Maverick",

    # ===== FANTASIA / AVENTURA 🧗 ===== #
    "O Senhor dos Anéis: A Sociedade do Anel",
    "O Senhor dos Anéis: As Duas Torres",
    "O Senhor dos Anéis: O Retorno do Rei",
    "O Hobbit: Uma Jornada Inesperada",
    "O Hobbit: A Desolação de Smaug",
    "O Hobbit: A B🧗atalha dos Cinco Exércitos",
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
    "Animais Fantásticos: Os Segredos de Dumbledore",
    "Piratas do Caribe: A Maldição do Pérola Negra",
    "Piratas do Caribe: O Baú da Morte",
    "Piratas do Caribe: No Fim do Mundo",
    "Piratas do Caribe: Navegando em Águas Misteriosas",
    "Piratas do Caribe: A Vingança de Salazar",

    # ===== DRAMA 🎭 ===== #
    "Forrest Gump",
    "Clube da Luta",
    "O Lobo de Wall Street",
    "Gladiador",
    "Gladiador 2",
    "O Resgate do Soldado Ryan",

    # ===== DINOSSAUROS 🦖 ===== #
    "Jurassic Park",
    "Jurassic Park 2: O Mundo Perdido",
    "Jurassic Park 3",
    "Jurassic World",
    "Jurassic World: Reino Ameaçado",
    "Jurassic World: Domínio",

    # ===== CORRIDA 🏎️ ===== #
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

    # ===== TERROR 🧟‍♀️ ===== #
    "Five Nights at Freddy's",
    "Five Nights at Freddy's 2",
    "Five Nights at Freddy's 3(Estreia)",
    "Invocação do Mal",
    "Invocação do Mal 2",
    "Invocação do Mal 3",
    "Annabelle",
    "Annabelle 2",
    "Annabelle 3",
    "A Freira",
    "A Freira 2",
    "It: A Coisa",
    "It: Capítulo Dois",
    "O Exorcista",
    "Hereditário",
    "O Babadook",
    "A Visita",
    "A Morte Te Dá Parabéns",
    "O Homem nas Trevas",

    # ===== DISNEY – ANIMAÇÕES COMPLETAS ===== #
    "Branca de Neve e os Sete Anões",
    "Pinóquio",
    "Fantasia",
    "Dumbo",
    "Bambi",
    "Saludos Amigos",
    "Os Três Caballeros",
    "Como É Bom se Divertir",
    "Tempo de Melodia",
    "As Aventuras de Ichabod e Sr. Sapo",
    "Cinderela",
    "Alice no País das Maravilhas",
    "Peter Pan",
    "A Dama e o Vagabundo",
    "A Bela Adormecida",
    "101 Dálmatas",
    "A Espada Era a Lei",
    "Mogli: O Menino Lobo",
    "Aristogatas",
    "Robin Hood",
    "As Aventuras de Winnie the Pooh",
    "Bernardo e Bianca",
    "O Cão e a Raposa",
    "O Caldeirão Mágico",
    "As Peripécias de um Ratinho Detetive",
    "Oliver e Sua Turma",
    "A Pequena Sereia",
    "Bernardo e Bianca na Terra dos Cangurus",
    "A Bela e a Fera",
    "Aladdin",
    "O Rei Leão",
    "Pocahontas",
    "O Corcunda de Notre Dame",
    "Hércules",
    "Mulan",
    "Tarzan",
    "Fantasia 2000",
    "Dinossauro",
    "A Nova Onda do Imperador",
    "Atlantis: O Reino Perdido",
    "Lilo & Stitch",
    "Planeta do Tesouro",
    "Irmão Urso",
    "Vacas Valentes",
    "Chicken Little",
    "A Família do Futuro",
    "Bolt",
    "A Princesa e o Sapo",
    "Enrolados",
    "Ursinho Pooh",
    "Detona Ralph",
    "Frozen",
    "Operação Big Hero",
    "Zootopia",
    "Moana",
    "WiFi Ralph",
    "Frozen II",
    "Raya e o Último Dragão",
    "Encanto",
    "Strange World",
    "Wish",
    "Moana 2",
    "Zootopia 2"

    # ===== PIXAR – CRONOLOGIA COMPLETA ===== #
    "Toy Story",
    "Vida de Inseto",
    "Toy Story 2",
    "Monstros S.A.",
    "Procurando Nemo",
    "Os Incríveis",
    "Carros",
    "Ratatouille",
    "Wall-E",
    "Up",
    "Toy Story 3",
    "Carros 2",
    "Valente",
    "Universidade Monstros",
    "Divertida Mente",
    "O Bom Dinossauro",
    "Procurando Dory",
    "Carros 3",
    "Viva – A Vida é uma Festa",
    "Os Incríveis 2",
    "Toy Story 4",
    "Dois Irmãos",
    "Soul",
    "Luca",
    "Red",
    "Lightyear",
    "Elementos",
    "Divertida Mente 2",
    "Elio",
    "Toy Story 5",

    # ==== MCU – SEM HOMEM-ARANHA ==== #
    # ===== FASE 1 ===== #
    "Homem de Ferro",
    "O Incrível Hulk",
    "Homem de Ferro 2",
    "Thor",
    "Capitão América: O Primeiro Vingador",
    "Os Vingadores",

    # ===== FASE 2 ===== #
    "Homem de Ferro 3",
    "Thor: O Mundo Sombrio",
    "Capitão América: O Soldado Invernal",
    "Guardiões da Galáxia",
    "Guardiões da Galáxia Vol. 2",
    "Vingadores: Era de Ultron",
    "Homem-Formiga",

    # ===== FASE 3 ===== #
    "Capitão América: Guerra Civil",
    "Doutor Estranho",
    "Pantera Negra",
    "Thor: Ragnarok",
    "Vingadores: Guerra Infinita",
    "Homem-Formiga e a Vespa",
    "Vingadores: Ultimato",
    "Viúva Negra",

    # ===== FASE 4 ===== #
    "Shang-Chi e a Lenda dos Dez Anéis",
    "Eternos",
    "Doutor Estranho no Multiverso da Loucura",
    "Thor: Amor e Trovão",
    "Pantera Negra: Wakanda Para Sempre",
    "Guardiões da Galáxia Vol. 3",

    # ===== FASE 5 ===== #
    "Homem-Formiga e a Vespa: Quantumania",
    "As Marvels",

    # ===== FUTUROS VINGADORES ===== #
    "Vingadores: Doomsday(Estreia)",
    "Vingadores: Guerras Secretas(Estreia)"]



def menu_sessoes():
    return ["10:00","11:00","12:00","13:00","15:00","16:00","17:00","18:00",
            "19:00","20:00","21:00","22:00","23:00"]

def menu_forma_de_pagamento():
    return ["Dinheiro","Cartão"]
