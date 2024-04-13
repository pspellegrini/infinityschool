//Ex02
//Menor de 18 - Você não pode entrar nessa festa
//Maior que 60 - Não sei o que ta fazendo aqui.

//Entrada de dados
const diaNascimento = parseInt(prompt("Digite o dia de nascimento: "))
const mesNascimento = parseInt(prompt("Digite o mês de nascimento: "))
const anoNascimento = parseInt(prompt("Digite o ano de nascimento: "))


//Processamento
const dataAtual = new Date(Date.now())
const diaAtual = dataAtual.getDay()
const mesAtual = dataAtual.getMonth()
const anoAtual = dataAtual.getFullYear()

const diferencaAno = anoAtual - anoNascimento
const menorDezoito = diferencaAno == 18 && mesAtual < mesNascimento && diaAtual < diaNascimento
const maiorSessenta = diferencaAno == 60 && mesAtual > mesNascimento && diaAtual > diaNascimento

//Saída de dados
if (diferencaAno < 18 || menorDezoito) {
    document.write("Você não pode entrar nessa festa.")
} else if (diferencaAno >= 60 || maiorSessenta) {
    document.write("Não sei o que ta fazendo aqui.")
} else {
    document.write("Seja bem vindo! Aproveite a festa.")
}