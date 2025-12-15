from flask import Flask, render_template, request, redirect, url_for
from backending.cinema import registrar_ingresso
from backending.cinema import resumo_dia
from backending.cinema import resumo_compra_atual
from backending.cinema import zerar_compra
from backending.cinema import menu_filmes
from backending.cinema import menu_sessoes
from backending.cinema import menu_forma_de_pagamento
from backending.cinema import registrar_pipoca_e_refri
from backending.cinema import acumuladores
from backending.cores import MAGENTA, RESET
from backending.gerenciador_dados import carregar_dados, salvar_dados

app = Flask(__name__)

ARQUIVO_CINEMA = "dados_gerais.json"
carregar_dados(ARQUIVO_CINEMA)


def rota_logada(nome_rota, extra=""):
    print(f"\n {MAGENTA}[Rota] {nome_rota} carregada com sucesso! {extra} {RESET}\033[0m \n")


@app.route("/")
@app.route("/index")
def index():
    filmes = menu_filmes()
    sessoes = menu_sessoes()
    rota_logada("Index✅")
    return render_template("index.html", filmes=filmes, sessoes=sessoes)


@app.route("/ingresso")
def ingresso():
    idade = request.args.get("idade", default=0, type=int)
    formas_pagamento = menu_forma_de_pagamento()

    rota_logada("Ingressos🎟️", f"(idade={idade})")

    return render_template(
        "ingresso.html",
        idade=idade,
        formas_pagamento=formas_pagamento)

@app.route("/pipoca")
def pipoca():
    combos = registrar_pipoca_e_refri()
    rota_logada("Pipocas🍿")
    return render_template("pipoca.html", combos=combos)

@app.route("/adicionar_pipoca")
def adicionar_pipoca():
    rota_logada("Pipoca adicionada🍿✅")
    preco = request.args.get("preco", default=0, type=int)
    nome = request.args.get("nome", type=str)

    if preco is None or nome is None:
        return redirect(url_for("pipoca"))

    acumuladores["valor_usuario"] += preco
    acumuladores["vendas_dia"] += preco
    acumuladores["combos_gerais"] += preco

    acumuladores["combo_nome"] = nome
    acumuladores["combo_preco"] = preco

    return redirect(url_for("pagamento"))


@app.route("/confirmar")
def confirmar():
    idade = request.args.get("idade", default=0, type=int)
    extra = request.args.get("extra", default=1, type=int)
    voltar = request.args.get("voltar", default=0, type=int)

    if idade <= 0:
        return redirect(url_for("ingresso"))

    registrar_ingresso(extra, idade)

    if voltar == 1:
        return redirect(url_for("ingresso", idade=idade))

    ingressos_usuario = acumuladores.get("ingressos_usuario", 0)
    valor = acumuladores.get("valor_usuario", 0)

    rota_logada("Confirmar Ingressos👍")

    return render_template(
        "confirmar.html",
        idade=idade,
        tipo=extra,
        valor=valor,
        ingressos_usuario=ingressos_usuario,
        acumuladores=acumuladores)

@app.route("/pagamento")
def pagamento():
    totalRS = acumuladores.get("valor_usuario", 0)
    ingressos_usuario = acumuladores.get("ingressos_usuario", 0)
    
    rota_logada("Pagamento💸")

    return render_template(
        "pagamento.html",
        totalRS=totalRS,
        ingressos_usuario=ingressos_usuario,
        acumuladores=acumuladores)


@app.route("/resumo")
def resumo():
    totalRS = acumuladores.get("valor_usuario", 0)
    ingressos_usuario = acumuladores.get("ingressos_usuario", 0)


    resumo = {
        "totalRS": acumuladores.get("vendas_dia", 0),
        "ingressos": acumuladores.get("ingressos_dia", 0),
        "inteira": acumuladores.get("inteira", 0),
        "meia": acumuladores.get("meia", 0),
        "promocional": acumuladores.get("promocional", 0),
        "gratuita": acumuladores.get("gratuita", 0),
        "pipocaserefisR$": acumuladores.get("combos_gerais", 0)}

    salvar_dados(ARQUIVO_CINEMA, resumo)

    zerar_compra()
    acumuladores["valor_usuario"] = 0
    acumuladores["ingressos_usuario"] = 0

    rota_logada("Resumo📃")

    return render_template(
        "resumo.html",
        totalRS=totalRS,
        ingressos_usuario=ingressos_usuario,
        resumo=resumo)

