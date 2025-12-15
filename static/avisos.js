document.addEventListener("DOMContentLoaded", () => {
    const params = new URLSearchParams(window.location.search)
    if (params.get("reset") === "true") {
        alert("Sistema reiniciado!✅ Clique em OK para iniciar uma nova compra.🛍️🛒")}

    const botoes = document.querySelectorAll("[data-preco]")
    const confirmar = document.getElementById("confirmar")

    botoes.forEach(botao => {
        botao.addEventListener("click", () => {
            document.getElementById("combo_nome").value = botao.dataset.nome
            document.getElementById("combo_preco").value = botao.dataset.preco

            document.querySelectorAll(".combo").forEach(c =>
                c.classList.remove("selecionado")
            )

            botao.closest(".combo").classList.add("selecionado")
            confirmar.disabled = false})
    })
})

document.addEventListener("DOMContentLoaded", () => {
    const total = Number(document.getElementById("total").value)
    const cartao = document.getElementById("cartao")
    const dinheiro = document.getElementById("dinheiro")
    const confirmar = document.getElementById("confirmar")
    const campoDinheiro = document.getElementById("campoDinheiro")
    const pago = document.getElementById("p")

    cartao.onclick = () => {
        confirmar.style.display = "inline-block"
        campoDinheiro.style.display = "none"
        confirmar.click()}

    dinheiro.onclick = () => {
        campoDinheiro.style.display = "block"
        confirmar.style.display = "inline-block"}

    confirmar.onclick = e => {
        if (campoDinheiro.style.display === "block") {
            if (Number(pago.value) < total) {
                e.preventDefault()
               alert("💸 Valor insuficiente!\n\nO valor informado é menor que o total da compra.\nPor favor, informe um valor igual ou maior para continuar 💰")}
        }
    }
})