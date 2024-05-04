//Crie um função chamada "soma". Essa função deve receber dois números como parâmetro e deve retornar a soma desses dois números.

function soma(num1, num2 = 0) {
    return num1 + num2
}
console.log(soma(84,18))
console.log(soma(53,35))
console.log(soma(15,43))


function soma(num1, num2) {
    const total = num1 + num2
    return total
}
const resultado = soma(20,3)
console.log(resultado)