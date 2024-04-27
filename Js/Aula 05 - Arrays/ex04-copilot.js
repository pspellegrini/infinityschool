// Modifique o exercício anterior para que ele consiga pedir uma quantidade de usuários ilimitada

// Criando um array vazio para armazenar os usuários
const usuarios = [];

// Pedindo e adicionando valores ao array até que o usuário deseje parar
while (true) {
    const usuario = prompt("Digite o nome do usuário (ou digite 'parar' para encerrar):");
    if (usuario.toLowerCase() === "parar") {
        break; // Encerra o loop se o usuário digitar "parar"
    }
    usuarios.push(usuario);
}

// Imprimindo a lista de usuários no console
console.log("Lista de usuários:");
usuarios.forEach((nome, indice) => {
    console.log(`${indice + 1}. ${nome}`);
});
