//Crie um algoritmo que conte a quantidade de vogais que um texto tem.

const texto = prompt("Digite um texto qualquer:")
let qntVogais = 0

for (let caractere of texto) {
    if ('aeiouAEIOU'.includes(caractere)){
        qntVogais++
    }
}

console.log(qntVogais)