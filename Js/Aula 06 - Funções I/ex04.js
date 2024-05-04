//Crie um programa de calculadora que apresenta as seguintes funções: 01. Função que imprima menu; 02. Função para cada operação aritmética a seguir: Soma, Subtração, Multiplicação, Divisão e Exponenciação.


function somar(num1, num2 = 0) {
    return num1 + num2
}

function subtrair(num1, num2 = 0) {
    return num1 - num2
}

function multiplicar(num1, num2 = 0) {
    return num1 * num2
}

function dividir(num1, num2 = 0) {
    return num1 / num2
}

function potencia(num1, num2 = 0) {
    return num1 ** num2
}

function exibirMenu() {
    console.log("Escolha uma das opções abaixo: ")
    console.log("01. Somar")
    console.log("02. Subtratir")
    console.log("03. Mutiplicar")
    console.log("04. Divisão")
    console.log("05. Exponenciação")
    console.log("06. Encerrar")
}

function menu() {
    alert(`
    01. Somar
    02. Subtratir
    03. Mutiplicar
    04. Divisão
    05. Exponenciação
    06. Encerrar
    `)
}

while (true) {
    menu()
    const opcao = parseInt(prompt("Digite uma opção: "))

    if (opcao === 1) {
        const num1 = parseInt(prompt("Digite o primeiro valor: "))
        const num2 = parseInt(prompt("Digite o segundo valor: "))
        
        const resultado = soma(num1, num2)

        console.log(resultado)
    } else if (opcao === 2) {
        const num1 = parseInt(prompt("Digite o primeiro valor: "))
        const num2 = parseInt(prompt("Digite o segundo valor: "))
        
        const resultado = subtracao(num1, num2)

        console.log(resultado)
    } else if (opcao === 3) {
        const num1 = parseInt(prompt("Digite o primeiro valor: "))
        const num2 = parseInt(prompt("Digite o segundo valor: "))
        
        const resultado = multiplicacao(num1, num2)

        console.log(resultado)
    } else if (opcao === 4) {
        const num1 = parseInt(prompt("Digite o primeiro valor: "))
        const num2 = parseInt(prompt("Digite o segundo valor: "))
        
        const resultado = divisao(num1, num2)

        console.log(resultado)
    } else if (opcao === 5) {
        const num1 = parseInt(prompt("Digite o primeiro valor: "))
        const num2 = parseInt(prompt("Digite o segundo valor: "))
        
        const resultado = exponenciacao(num1, num2)

        console.log(resultado)
    } else if (opcao === 6) {
        console.log("Saindo...")
        break
    }
}