//01. While

let contador = 0

while (contador < 10) {
    document.writeln(contador)
    
    if (contador === 5) {
        break
    }

    contador++
}

console.log(contador)