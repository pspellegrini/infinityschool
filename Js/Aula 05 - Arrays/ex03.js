// Crie um array de usuários que comece vazio. Utilize o laço de repetição {for} para pedir e adicionar 5 valores ao array. Ao final, imprima o array.

// Criando um array vazio para armazenar os usuários
const usuarios = [];

// Pedindo e adicionando 5 valores ao array
for (let i = 0; i < 5; i++) {
    const novoUsuario = prompt('Digite o nome do novo usuário: ')
    usuarios.push(novoUsuario);
}

// Imprimindo o array no console
console.log(usuarios);