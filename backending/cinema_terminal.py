from cores import (
    RESET,
    VERMELHO,
    VERDE,
    AZUL,
    BRANCO,
    VERDE_CLARO,
    AMARELO_CLARO,
    AZUL_CLARO,
    MAGENTA_CLARO,
    BRANCO_CLARO)

def main():
    acumuladorvalor = 0
    acumuladoringresso = 0
    acumuladorvalor_dia = 0
    acumuladoringresso_dia = 0
    acumuladorpipoca = 0

    while True:
        def menu_principal():
            print(f"{MAGENTA_CLARO}--- CINEMA PYTHON 🎞️ ---{RESET}")
            print("\nInsira a Idade do cliente e qual ingresso deseja")
        menu_principal()

        def tipos_de_ingressos():
            print(f"{AZUL_CLARO}\n Tipos de ingressos:{RESET}")
            print("1 - Inteira - R$ 30,00 🎫")
            print("2 - Meia-entrada - R$ 15,00 🎫")
            print("3 - Promocional - R$ 21,00 🎫")
            print("4 - Entrada Gratuita - R$ 0,00 🎫")
        tipos_de_ingressos()

        idade = input("\n Digite a idade do cliente:")
        while idade.isdigit() == False:
            print(f"{VERMELHO}Entrada inválida. Por favor, insira um valor valido❌{RESET}")
            idade = input("Digite a idade do cliente: ")
        idade = int(idade)
        if idade <= 0 or idade >= 120:
            print(f"{VERMELHO}Idade inválida. ❌{RESET}")
            continue

        if idade < 5:
            print("Entrada gratuita 🎟️")

        ingresos = input("Digite o tipo de ingresso que quer comprar: ")
        while ingresos.isdigit() == False:
            print(f"{VERMELHO}Entrada inválida. Por favor, insira um valor valido ❌{RESET}")
            ingresos = input("Digite o tipo de ingresso que quer comprar: ")
        ingresos = int(ingresos)
        if ingresos == 1:
            acumuladorvalor += 30
            acumuladoringresso += 1
            print(f"{AMARELO_CLARO}Valor do ingresso Inteiro: R$ 30,00 🎫{RESET}")
            if ingresos == 1 and idade < 5:
                acumuladorvalor -= 30
        elif ingresos == 2:
            acumuladorvalor += 15
            acumuladoringresso += 1
            print(f"{AMARELO_CLARO}Valor do ingresso Meia-entrada: R$ 15,00 🎫{RESET}")
            if ingresos == 2 and idade < 5:
                acumuladorvalor -= 15
        elif ingresos == 3:
            acumuladorvalor += 21
            acumuladoringresso += 1
            print(f"{AMARELO_CLARO}Valor do ingresso Promocional: R$ 21,00 🎫{RESET}")
            if ingresos == 3 and idade < 5:
                acumuladorvalor -= 21
        elif ingresos == 4:
            acumuladorvalor += 0
            print(f"{AMARELO_CLARO}Valor do ingresso Gratuito: R$ 0,00 🎫{RESET}")
            acumuladoringresso += 1
        else:
            print(f"{VERMELHO}Tipo de ingresso inválido. ❌{RESET}")
            acumuladoringresso = 0

        def menu_pipoca():
            nonlocal acumuladorvalor
            nonlocal acumuladorpipoca
            print(f"\n{AZUL_CLARO}--- COMBOS DE PIPOCA 🍿 ---{RESET}")
            print("1 - Pequeno - R$ 15,00 🍿")
            print("2 - Médio   - R$ 30,00 🍿")
            print("3 - Grande  - R$ 50,00 🍿")
            print("4 - Não quero pipoca ❌")
            opcao = input("Escolha seu combo de pipoca: ")
            while opcao.isdigit() == False:
                print(f"{VERMELHO}Entrada inválida. Por favor, insira um valor válido❌{RESET}")
                opcao = input("Escolha seu combo de pipoca: ")
            opcao = int(opcao)
            if opcao == 1:
                acumuladorvalor += 15
                acumuladorpipoca += 15
                print(f"{AMARELO_CLARO}Combo Pequeno adicionado: R$ 15,00{RESET}")
            elif opcao == 2:
                acumuladorvalor += 30
                acumuladorpipoca += 30
                print(f"{AMARELO_CLARO}Combo Médio adicionado: R$ 30,00{RESET}")
            elif opcao == 3:
                acumuladorvalor += 50
                acumuladorpipoca += 50
                print(f"{AMARELO_CLARO}Combo Grande adicionado: R$ 50,00{RESET}")
            elif opcao == 4:
                print(f"{AZUL}Nenhuma pipoca adicionada.{RESET}")
            elif opcao != 1 or opcao!=2 or opcao !=3 or opcao!=4:
                print(f"{VERMELHO}Opção inválida. Nenhuma pipoca adicionada.{RESET}")
                return menu_pipoca()
        menu_pipoca()

        continuar = input(f"{AZUL}Deseja comprar mais ingressos? (s/n): {RESET}").lower()
        if continuar in "Ss":
            continue
        else:
            print(f"{VERDE}\nTotal a pagar: R$ {acumuladorvalor:.2f}{RESET} 💸")
            print(f"{BRANCO}Quantidade de ingressos comprados: {acumuladoringresso}{RESET} 🎫")
            print(f"{AMARELO_CLARO}Total gasto com pipoca: R$ {acumuladorpipoca:.2f}{RESET} 🍿")

        if acumuladorvalor == 0 and acumuladoringresso == 0:
            print(f"{VERMELHO}Nenhum ingresso comprado. Encerrando o programa. ❌{RESET}")
            exit()
        if idade >= 5 and ingresos not in [1,2,3]:
            print(f"{VERMELHO}Entrada gratuita SOMENTE para crianças menores de 5 anos. Incongruência na sua compra. Encerrando o sistema ❌...{RESET}")
            exit()

        def menu_forma_de_pagamento():
            print(f"\n {BRANCO_CLARO}Formas de pagamento:{RESET}")
            print(f"{VERDE_CLARO}1 - Dinheiro 💰{RESET}")
            print(f"{VERDE_CLARO}2 - Cartão 💳{RESET}")
            formapagamento = int(input("Escolha a forma de pagamento (dinheiro 💰 / cartão 💳): "))
            if formapagamento == 1:
                print("Pagamento em dinheiro selecionado. 💸")
                dinheiro = input("Digite o valor em dinheiro: R$ ")
                while dinheiro.isdigit() == False:
                    print(f"{VERMELHO}Entrada inválida. Por favor, insira um valor valido ❌{RESET}")
                    dinheiro = input("Digite o valor em dinheiro: R$ ")
                dinheiro = float(dinheiro)
                while dinheiro < acumuladorvalor:
                    print(f"{VERMELHO}Valor insuficiente.{RESET} ❌")
                    dinheiro = input("Digite o valor em dinheiro: R$ ")
                    while dinheiro.isdigit() == False:
                        print(f"{VERMELHO}Entrada inválida. Por favor, insira um valor valido ❌{RESET}")
                        dinheiro = input("Digite o valor em dinheiro: R$ ")
                    dinheiro = float(dinheiro)
                troco = dinheiro - acumuladorvalor
                print(f"{VERDE_CLARO}Pagamento em dinheiro realizado com sucesso. Troco: R$ {troco:.2f}{RESET} 💸")
            elif formapagamento == 2:
                print(f"{VERDE_CLARO}Pagamento com cartão selecionado e realizado com sucesso. 💳{RESET}")
            while formapagamento not in [1,2]:
                print(f"{VERMELHO}Forma de pagamento inválida. ❌{RESET}")
                formapagamento = int(input("Escolha a forma de pagamento (dinheiro/cartão): "))
                if formapagamento == 1:
                    print("Pagamento em dinheiro selecionado. 💸")
                    dinheiro = input("Digite o valor em dinheiro: R$")
                    while dinheiro.isdigit() == False:
                        print(f"{VERMELHO}Entrada inválida. Por favor, insira um valor valido ❌{RESET}")
                        dinheiro = input("Digite o valor em dinheiro: R$")
                    dinheiro = float(dinheiro)
                    while dinheiro < acumuladorvalor:
                        print(f"{VERMELHO}Valor insuficiente.{RESET} ❌")
                        dinheiro = input("Digite o valor em dinheiro: R$ ")
                        while dinheiro.isdigit() == False:
                            print(f"{VERMELHO}Entrada inválida. Por favor, insira um valor valido ❌{RESET}")
                            dinheiro = input("Digite o valor em dinheiro: R$ ")
                        dinheiro = float(dinheiro)
                    troco = dinheiro - acumuladorvalor
                    print(f"{VERDE}Pagamento em dinheiro realizado com sucesso. Troco: R$ {troco:.2f}{RESET} 💸")
                elif formapagamento == 2:
                    print(f"{VERDE}Pagamento com cartão selecionado e realizado com sucesso. 💳{RESET}")
        menu_forma_de_pagamento()

        while True:
            def menu_resumo_cliente():
                print(f"\n{MAGENTA_CLARO}--- RESUMO DA SUA COMPRA 📃 ---{RESET}")
                print(f"{VERDE_CLARO}Total pago: R$ {acumuladorvalor:.2f}{RESET}💰")
                print(f"{AMARELO_CLARO}Quantidade de ingressos comprados: {acumuladoringresso}{RESET} 🎟️")
                print(f"{AMARELO_CLARO}Total gasto com pipoca: R$ {acumuladorpipoca:.2f}{RESET} 🍿")
                print(f"{AZUL_CLARO}Ótima sessão! Volte sempre ao CINEMA PYTHON.{RESET} 🎞️")
            menu_resumo_cliente()
            break

        while True:
            voltar = input(f"{BRANCO_CLARO}Deseja voltar ao realizar uma nova compra? 🛍️ (s/n):{RESET} ").lower()
            if voltar == "s":
                acumuladorvalor_dia += acumuladorvalor
                acumuladoringresso_dia += acumuladoringresso
                acumuladorvalor = 0
                acumuladoringresso = 0
                acumuladorpipoca = 0
                print(f"\n{MAGENTA_CLARO}--- NOVA COMPRA 🛍️ ---{RESET}")
                break 
            elif voltar == "n":
                acumuladorvalor_dia += acumuladorvalor
                acumuladoringresso_dia += acumuladoringresso
                opcao = input("Deseja ver o resumo do dia? 📃 (s/n): ").lower()
                if opcao in "Ss":
                    print(f"\n{MAGENTA_CLARO} --- RESUMO DO DIA 📃 ---{RESET}")
                    print(f"{VERDE_CLARO}Total arrecadado: R${acumuladorvalor_dia:.2f}{RESET} 💰")
                    print(f"{AMARELO_CLARO}Total de ingressos vendidos: {acumuladoringresso_dia}{RESET} 🎟️")
                    print(f"{AMARELO_CLARO}Total arrecadado com pipoca: R$ {acumuladorvalor:.2f}{RESET} 🍿")
                print(f"{AZUL}Obrigado por utilizar o CINEMA PYTHON. Até a próxima! 🎞️{RESET}")
                exit()
            else:
                print(f"{VERMELHO}Opção inválida. Digite apenas 's' ou 'n'.{RESET} ❌")

if __name__ == "__main__":
    main()
    debug = True
...