let listaCompras = ["arroz", "feijão", "macarrão", "banana", "ovo", "pão", "carne", "peixe"]

const valor = listaCompras[2]
console.log(valor)
console.log(listaCompras[3])

listaCompras[4] = "whey"
console.log(listaCompras)

// .pop() - Adiciona um valor ao array
let listaNomes = []

listaNomes.push('Not')
console.log(listaNomes)

listaNomes.push('Arthur')
console.log(listaNomes)

listaNomes.push('Davi')
console.log(listaNomes)

// .pop() - Remove o último valor do array
listaNomes.pop()
console.log(listaNomes)

const valorRemovido = listaNomes.pop()
console.log(valorRemovido)
console.log(listaNomes)

// .unshift(valor) - Adiciona um valor ao inicio do array
listaNomes.unshift('Diego')
console.log(listaNomes)

// .shift(valor) - Remove um valor do inicio do array
listaNomes.shift()
console.log(listaNomes)

// .indexOf(valor) - 
console.log(listaCompras)
posicao = listaCompras.indexOf('macarão')
console.log(posicao)

// .slice(valor, valor)
const pedacoCompras = listaCompras.slice(posicao, 7)
console.log(pedacoCompras)
console.log(listaCompras)

// .splice(valor, valor)
const pedacoRemovidoCompras = listaCompras.splice(3, 2)
console.log(pedacoRemovidoCompras)
console.log(listaCompras)

for (let compra of listaCompras) {
    console.log(compra)
}