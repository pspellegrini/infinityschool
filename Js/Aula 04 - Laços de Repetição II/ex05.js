//Crie um algoritmo que verifique se uma palavra é um palíndromo.

const palavra = prompt("Digite uma palavra:")
const finalPalavra = palavra.length - 1

const palavraInversa = ''

for (let i = finalPalavra; 1 >= 0; i--) {
    palavraInversa += palavra[i]
}

if (palavra === palavraInversa) {
    document.write("É um palíndromo!")
} else {
    document.write("Não é um palíndromo!")
}