from cores import (RESET, VERMELHO)

def valida_idade():
    idade = input("\n Digite a idade do usuário: ")
    while not idade.isdigit():
        print(f"{VERMELHO}\n Entrada inválida. Por favor, insira um valor valido❌{RESET}")
        idade = input("\n Digite a idade do cliente: ")
    idade = int(idade)
    if idade <= 0 or idade >= 120:
        print(f"{VERMELHO}\n Idade inválida. Reiniciando sistema...❌ \n {RESET}")
        return None
    return idade

def valida_ingresso():
    ingresos = input("\n Digite o tipo de ingresso que quer comprar: ")
    while not ingresos.isdigit():
        print(f"{VERMELHO}\n Entrada inválida. Por favor, insira um valor valido ❌{RESET}")
        ingresos = input("\n Digite o tipo de ingresso que quer comprar: ")
    return int(ingresos)

def valida_opcao_sn(mensagem):
    opcao = input(mensagem).strip().lower()
    while opcao not in ("s", "n"):
        print(f"{VERMELHO}\n Opção inválida. Digite apenas s ou n.{RESET}")
        opcao = input(mensagem).strip().lower()
    return str(opcao)

def valida_menu_numerico(mensagem, opcoes):
    valor = input(mensagem)
    while not valor.isdigit() or int(valor) not in opcoes:
        print(f"{VERMELHO}\n Opção inválida. ❌{RESET}")
        valor = input(mensagem)
    return int(valor)

def valida_float():
    valor = input().replace(",", ".").strip()
    while not valor.replace(".", "", 1).isdigit():
        print(f"{VERMELHO}\n Entrada inválida. Por favor, insira um valor valido ❌{RESET}")
        valor = input().replace(",", ".").strip()
    return float(valor)

def valida_dinheiro(valor_minimo):
    dinheiro = input("\n Digite o valor em dinheiro: R$ ").replace(",", ".", 1).strip()
    while not dinheiro.replace(".", "", 1).isdigit():
        print(f"{VERMELHO}\n Entrada inválida. Por favor, insira um valor valido ❌{RESET}")
        dinheiro = input("\n Digite o valor em dinheiro: R$ ").replace(",", ".").strip()
    dinheiro = float(dinheiro)
    while dinheiro < valor_minimo:
        print(f"{VERMELHO}Valor insuficiente.{RESET} ❌")
        dinheiro = input("Digite o valor em dinheiro: R$ ").replace(",", ".", 1).strip()
        while not dinheiro.replace(".", "", 1).isdigit():
            print(f"{VERMELHO}Entrada inválida. Por favor, insira um valor valido ❌{RESET}")
            dinheiro = input("Digite o valor em dinheiro: R$ ").replace(",", ".").strip()
        dinheiro = float(dinheiro)
    return dinheiro




...