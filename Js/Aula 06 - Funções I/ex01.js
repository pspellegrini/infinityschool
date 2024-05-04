// Crie uma função chamada saudacao. Essa função deve pedir o nome do usuário e imprimir uma mensagem personalizada com o nome dele. Por fim, execute essa função.

function saudacao() {
    const nome = prompt("Digite seu nome: ")
    const mensagem = `Seja muito bem-vindo, ${nome}!`
    console.log(mensagem)
}
saudacao()


function saudacao2() {
    const nome = prompt("Digite seu nome: ")
    console.log(`Olá seja bem vindo ${nome}!`)
}
saudacao2()
