//Ex03: Crie um programa que imprime a tabuada de um número que o usuário digitar.

//Entrada de dados
const numero = parseInt(prompt("Digite um número que deseje saber sua taboada: "))


//Processamento
let contador = 0

//while (contador <= 10) {
//    document.writeln(numero * contador)
//    contador++
//}

while (contador <= 10) {
    const resultado = contador * numero

    document.writeln(`${numero} x ${contador} = ${resultado} <br>`)

    contador++
}

//Saída de dados