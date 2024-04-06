// Crie um programa que peça ao usuário sua data de nascimento e a partir dessa informação identifique sua idade e utilizando o {document.write()} imprima a seguintes mensagens abaixo:
// Caso menor de 18 anos: "Você ainda não tem a idade necessária para dirigir. Volte assim que completar a idade mínima exigida de 18 anos."
// Caso maior ou igual a 19 anos: "Você já tem a idade necessária para dirigir."

//Entrada de dados
const anoNascimento = parseInt(prompt("Digite o ano de nascimento: "))

//Processamento
const idade = 2024 - anoNascimento

//Saída de dados
if (idade < 18) {
    document.write("Você ainda não tem a idade necessária para dirigir. Volte assim que completar a idade mínima exigida de 18 anos.")
} else {
    document.write("Você já tem a idade necessária para dirigir.")
}