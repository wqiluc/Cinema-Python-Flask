document.addEventListener("DOMContentLoaded", () => {const params = 
    new URLSearchParams(window.location.search);
    if (params.get("reset") === "true") {
        alert("Sistema reiniciado!✅ Clique em OK para iniciar uma nova compra.🛍️🛒");
    }});


