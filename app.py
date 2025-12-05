from flask import Flask, render_template, request, redirect, url_for
from backending.Cinema import registrar_ingresso, resumo_dia, resumo_compra_atual, zerar_compra
from backending.Cinema import menu_filmes, menu_sessoes, menu_forma_de_pagamento, acumuladores
from backending.gerenciador_dados import carregar_dados, salvar_dados

app = Flask(__name__)

ARQUIVO_CINEMA = "Dados_ingressos_cinema.json"

carregar_dados(ARQUIVO_CINEMA)

def rota_logada(nome_rota, extra=""):
    print(f"\033[92m[Rota] {nome_rota} carregada com sucesso!{extra}\033[0m")

@app.route("/")
@app.route("/index")
def index():
    filmes = menu_filmes()
    sessoes = menu_sessoes()
    rota_logada("Index")
    return render_template("index.html", filmes=filmes, sessoes=sessoes)

@app.route("/")
@app.route("/ingresso")
def ingresso():
    idade = request.args.get("idade", default=0, type=int)
    formas_pagamento = menu_forma_de_pagamento()
    rota_logada("Ingresso", f"(idade={idade})")
    return render_template("ingresso.html", idade=idade, formas_pagamento=formas_pagamento)

@app.route("/")
@app.route("/confirmar")
def confirmar():
    idade = request.args.get("idade", default=0, type=int)
    extra = request.args.get("extra", default=1, type=int)
    if idade <= 0:
        return redirect(url_for("ingresso"))
    valor = registrar_ingresso(extra, idade)
    rota_logada("Confirmar", f"(idade={idade}, tipo={extra}, valor={valor})")
    return render_template("confirmar.html", idade=idade, tipo=extra, valor=valor, acumuladores=acumuladores)

@app.route("/")
@app.route("/pagamento")
def pagamento():
    totalRS = acumuladores["valor_usuario"]
    return render_template("pagamento.html", totalRS=totalRS, acumuladores=acumuladores)

@app.route("/")
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
        "gratuita": acumuladores.get("gratuita", 0)}
    
    salvar_dados(ARQUIVO_CINEMA, resumo)

    zerar_compra()

    acumuladores["valor_usuario"] = 0
    acumuladores["ingressos_usuario"] = 0

    return render_template(
        "resumo.html",
        totalRS=totalRS,
        ingressos_usuario=ingressos_usuario,
        resumo=resumo)
