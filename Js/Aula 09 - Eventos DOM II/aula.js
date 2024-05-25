// function teste() {
//     console.log('Teste');
// }

// function teste2(callBack){
//     console.log('Teste 2');
//     callBack
// }

// teste2(teste)

let btn = document.querySelector('#btn')
let texto = document.querySelector('#texto')
let inputText = document.querySelector('#textInput')
let minhaDiv = document.querySelector('#minhaDiv')

let novaDiv = document.createElement('div')

novaDiv.style.backgroundColor = 'blue';
novaDiv.style.padding = '10px';
novaDiv.innerText = 'Minha div dois'

minhaDiv.appendChild(novaDiv)


// minhaDiv.addEventListener('mouseover', () => {
//     minhaDiv.innerHTML = 'Passou o mouse por cima'
//     texto.innerHTML = 'Novo texto'
// })

// minhaDiv.addEventListener('mouseout', () => {
//     texto.innerHTML = 'Retirou o mouse'
// })

// inputText.addEventListener('input', (event) => {
//     console.log(`Esse é o valor do meu input: ${event.target.value}`);
// })


// btn.addEventListener('click', () => {
//     texto.innerHTML = 'Cliclado'
//     console.log('O ouvinte está aqui');
// })

// function btnClick() {
//     console.log('A função não é mais o listener');
// }
