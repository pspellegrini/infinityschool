//Ex04: modifique o exercício anterior para que ele imprima a tabuada do 1 até o 10.


//Exercício anterior: Crie um programa que imprime a tabuada de um número que o usuário digitar.

//Entrada de dados
const numero = parseInt(prompt("Digite um número que deseje saber sua taboada: "))

//Processamento
let x = 0

//while (contador <= 10) {
//    document.writeln(numero * contador)
//    contador++
//}

//while (x <= numero) {
//    let y = 0
//    while (y <= 10) {
//        document.write(`${x} x ${y} = ${x*y} <br>`)
//        y++
//    }
//    x++
//}


while (x <= numero) {
    let y = 0

    while (y <= 10) {
        document.write(`${x} x ${y} = ${x*y} <br>`)

        y++
    }

    x++
}

//Saída de dados