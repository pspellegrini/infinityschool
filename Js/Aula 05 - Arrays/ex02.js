// Crie uma lista de usuários que vai começar vazia. Adicione 3 valores a essa lista. Remova o valor do índice 1. Imprima essa lista no console.

// Criando uma lista de usuários vazia
const listaUsuarios = []

// Adicionando 3 valores à lista
listaUsuarios.push("Alice");
listaUsuarios.push("Bob");
listaUsuarios.push("Carol");
console.log(listaUsuarios)

// Removendo o valor do índice 1
const usuarioRemovido = listaUsuarios.shift(1)
console.log(usuarioRemovido)

// Imprimindo a lista
console.log(listaUsuarios)