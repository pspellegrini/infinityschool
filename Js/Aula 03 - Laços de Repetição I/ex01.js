//Ex01: Crie um programa que verifique se um número é negativo ou positivo. Utilize o operador ternário para fazer as tomadas de decisão.

//Entrada de dados
const numero = parseInt(prompt("Digite um número: "))

//Processamento


//Saída de dados
if (numero >= 0 ) {
    document.write("O número escolhido é positivo.")
} else {
   document.write("O número escolhido é negativo.")
}


numero >= 0 ? document.write("O número escolhido é positivo.") : document.write("O número escolhido é negativo.")

const resposta = numero >= 0 ? "O número escolhido é positivo." : "O número escolhido é negativo."
console.log(resposta)