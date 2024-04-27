// Modifique o exercício anterior para que ele consiga pedir uma quantidade de usuários ilimitada

// Criando um array vazio para armazenar os usuários
const usuarios = []

// Pedindo e adicionando valores ao array até que o usuário deseje parar
do {
    const novoUsuario = prompt('Digite o nome do usuário: ')
    
    usuarios.push(novoUsuario)
} while (confirm('Quer continuar?'))

// Imprimindo a lista de usuários no console
console.log(usuarios)
