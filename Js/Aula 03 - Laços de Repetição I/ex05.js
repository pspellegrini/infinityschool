//Ex05: Crie um programa que calculará o ano de nascimento do usuário. Caso o usuário digite um valor que nao seja um número, utilize um laço de repetição para força-lo a digitar um número.

//Entrada de dados
let idade

while (true) {
    idade = parseInt(prompt("Digite sua idade: "))
    
    if (!isNaN(idade)) {
        break
    }

    alert("Digite um valor válido!")
}

const anoNascimento = 2024 - idade

document.write(anoNascimento)