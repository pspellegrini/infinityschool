//02. Condicionais
//if
const numero01 = parseFloat(prompt("Digite um número: "))
if (numero01 > 5) {
    document.write("O número é maior que 5.")
} else {
    document.write("O número não é maior que 5.")
}

// else if
const numero02 = parseFloat(prompt("Digite outro número: "))
if (numero02 > 5) {
    document.write("O número é maior que 5.")
} else if (numero02 > 2) {
    document.write("O número não é maior que 5,mas é maior que 2.")
} else {
    document.write("O número não é maior que 5 e nem maior que 2.")
}