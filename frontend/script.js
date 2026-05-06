const API = "http://127.0.0.1:8000"

async function loadBalance() {
    const res = await fetch(`${API}/balance`)
    const data = await res.json()

    document.getElementById("balance").innerText =
        `Receitas: ${data.Receitas} | Despesas: ${data.Despesas} | Saldo: ${data.Saldo}`
}

async function loadTransactions() {
    const res = await fetch(`${API}/transactions`)
    const data = await res.json()

    const list = document.getElementById("list")
    list.innerHTML = ""

    data.forEach(t => {
        const li = document.createElement("li")

        li.innerHTML = `
            <span>${t.description}</span>
            <span class="${t.type}">R$ ${t.amount}</span>
        `

        list.appendChild(li)
    })
}

async function addTransaction() {
    const description = document.getElementById("description").value
    const amount = parseFloat(document.getElementById("amount").value)
    const type = document.getElementById("type").value
    const category_id = parseInt(document.getElementById("category").value)

    await fetch(`${API}/transactions`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            description,
            amount,
            type,
            category_id
        })
    })

    // atualiza tela
    loadTransactions()
    loadBalance()
    loadCategoriesByType()

    // limpa inputs
    document.getElementById("description").value = ""
    document.getElementById("amount").value = ""

    // feedback
    alert("Transação adicionada!")
}
async function loadCategories() {
    const res = await fetch(`${API}/categories`)
    const data = await res.json()

    const select = document.getElementById("category")
    select.innerHTML = ""

    data.forEach(cat => {
        const option = document.createElement("option")
        option.value = cat.id
        option.textContent = `${cat.name} (${cat.type})`
        select.appendChild(option)
    })
}

async function loadCategoriesByType() {
    const type = document.getElementById("type").value
    const res = await fetch(`${API}/categories`)
    const data = await res.json()


    const select = document.getElementById("category")
    select.innerHTML = ""

    data
        .filter(cat => cat.type === (type === "receita" ? "income" : "expense"))
        .forEach(cat => {
            const option = document.createElement("option")
            option.value = cat.id
            option.textContent = cat.name
            select.appendChild(option)
        })
}

    loadTransactions()
    loadBalance()
    loadCategoriesByType()


loadTransactions()
loadBalance()