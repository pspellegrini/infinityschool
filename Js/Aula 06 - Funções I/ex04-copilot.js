//Crie um programa de calculadora que apresenta as seguintes funções: 01. Função que imprima menu; 02. Função para cada operação aritmética a seguir: Soma, Subtração e Multiplicação.

// Função para imprimir o menu
function exibirMenu() {
    console.log("Opções disponíveis:");
    console.log("1. Soma");
    console.log("2. Subtração");
    console.log("3. Multiplicação");
}

// Função para realizar a soma
function somar(a, b) {
    return a + b;
}

// Função para realizar a subtração
function subtrair(a, b) {
    return a - b;
}

// Função para realizar a multiplicação
function multiplicar(a, b) {
    return a * b;
}

// Exemplo de uso
exibirMenu();
const resultadoSoma = somar(5, 3);
console.log("Resultado da soma:", resultadoSoma);
