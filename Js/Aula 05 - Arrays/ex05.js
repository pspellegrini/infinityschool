// Modifique o exercício anterior para que ele permita que após adicionar todos os nomes, o usuário consiga remover um dos nomes.

// Criando um array vazio para armazenar os usuários
const usuarios = []

// Pedindo e adicionando valores ao array até que o usuário deseje parar
do {
    const novoUsuario = prompt('Digite o nome do usuário: ')
    
    usuarios.push(novoUsuario)
} while (confirm('Quer continuar?'))

// Imprimindo a lista de usuários no console
console.log(usuarios)

// Pedindo para o usuário excluir um usuário
const usuarioASerRemovido = prompt('Digite o nome do usuário a ser removido: ')
const posicaoUsuarioASerRemovido = usuarios.indexOf(usuarioASerRemovido)
if (posicaoUsuarioASerRemovido >= 0) {
    usuarios.splice(posicaoUsuarioASerRemovido, 1)

    console.log(usuarios)
} else {
    console.log('O usuário não existe!')
}
console.log(usuarios)
