//00. Revisão: Condicionais

const numero = prompt("Digite um número: ")
const par = numero % 2 == 0
const impar = numero % 2 != 0

if (par) {
    document.write("O número escolhido é um número par.")
} else {
    document.write("O número escolhido é um número impar.")
}

par ? document.write("O número escolhido é um número par.") : document.write("O número escolhido é um número impar.")