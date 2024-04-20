//Crie um algoritmo que reproduza o seguinte padrão no console:
//  *  
// **
// ***
// ****
//*****


for (let i = 1;i <= 5; i++) {
    const qntEspacos = (5 - i) / 2
    const espacos = ' '.repeat(qntEspacos)
    const asteriscos = '*'.repeat(i)
    console.log(espacos + asteriscos)
}