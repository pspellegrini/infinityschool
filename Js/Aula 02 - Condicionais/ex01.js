//Calcule a área de um retangulo a partir da insersão de dois números e imprima o resultado dentro de uma frase.

//Entrada de dados
const base = parseFloat(prompt("Digite um número para a base do retângulo: "))
const altura = parseFloat(prompt("Digite um número para a altura do retângulo? "))

//Processamento
const resultado = base * altura

//Saída de dados
console.log(`Um retângulo com base de ${base}cm e altura de ${altura}cm tem uma área de ${resultado}cm².`)