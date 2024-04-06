//Modifique o exercício anterior para verificar se o usuário já completou 18 anos com base no ano vigente da consulta e se já possui CNH emitida.

//Exercício anterior:
//Crie um programa que peça ao usuário sua data de nascimento e a partir dessa informação identifique sua idade e utilizando o {document.write()} imprima a seguintes mensagens abaixo:
//Caso menor de 18 anos: "Você ainda não tem a idade necessária para dirigir. Volte assim que completar a idade mínima exigida de 18 anos."
//Caso maior ou igual a 19 anos: "Você já tem a idade necessária para dirigir."

//Entrada de dados
const diaNascimento = parseInt(prompt("Digite o dia de nascimento: "))
const mesNascimento = parseInt(prompt("Digite o mês de nascimento: "))
const anoNascimento = parseInt(prompt("Digite o ano de nascimento: "))

const dataAtual = new Date(Date.now())
const diaAtual = dataAtual.getDay()
const mesAtual = dataAtual.getMonth()
const anoAtual = dataAtual.getFullYear()


//Processamento
const diferencaAno = anoAtual - anoNascimento
const naofezAniversario = diferencaAno == 18 && mesAtual < mesNascimento && diaAtual < diaNascimento

//Saída de dados
if (diferencaAno < 18 || naofezAniversario) {
    document.write("Você ainda não tem a idade necessária para dirigir. Volte assim que completar a idade mínima exigida de 18 anos.")
} else {

    const possuiCNH = prompt("Você já tem a idade necessária para dirigir. Já possui CNH? [S/N]").toUpperCase()

    if (possuiCNH === "S" ){
        document.write("Que bom que você já possui CHN. Diriga com responsabilidade!")
    } else if (possuiCNH === "N" ){
        document.write("Para poder dirigir faz-se necessário possuir uma CNH. Procure o DETRAN mais próximo e procure saber como emitir sua primeira CNH.")
    } else {
        document.write("Desculpe não foi possível entender sua resposta. Responda apenas usando S ou N.")
    }
}