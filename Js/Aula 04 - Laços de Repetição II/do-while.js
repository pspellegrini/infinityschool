let resposta = prompt("Quer continuar? [S/N]")

while (resposta !== "S" && resposta !== "N") {
    console.log("Resposta inválida! Tente novamente.")
    resposta = prompt("Quer continuar? [S/N]")
}

do {
    var resposta2 = prompt("Quer continuar 2? [S/N]")
} while (resposta2 !== "S" && resposta2 !== "N")