//Atividade 01
let btn = document.querySelector('#btn')

btn.addEventListener('click', () => {
    let inputText = document.querySelector('#inputText')
    let inputValue = inputText.value.trim();

    let itemList = document.createElement('li')

    itemList.textContent = inputValue

    let list= document.querySelector('#list')
    list.appendChild(itemList)
})


//Atividade 02
let btn2 = document.querySelector('#btn2')
btn2.addEventListener('click', () => {
    console.log('teste')
    let inputText = document.querySelector('#inputText2')
    let inputValue = inputText.value.trim();
    let minhaDiv = document.querySelector('#minhaDiv')
    console.log(inputValue)
    let paragrafo = document.createElement('p')
    paragrafo.innerText = inputValue

    minhaDiv.appendChild(paragrafo)    
})

//Atividade 03
function clickBtn3(){
    let bodyColor = document.body.style.backgroundColor = '#5E4C5A'
}

function clickBtn4(){
    let bodyColor = document.body.style.backgroundColor = '#6BAB90'
}

function clickBtn5(){
    let bodyColor = document.body.style.backgroundColor = '#FFE2D1'
}

//Atividade 04

let listaCitacoes = [
    'A educação é a arma mais poderosa que você pode usar para mudar o mundo. - Autor: Nelson Mandela (1918-2013), ex-presidente da África do Sul',
    'O maior erro que um homem pode cometer é sacrificar a sua saúde a qualquer outra vantagem. - Autor: Arthur Schopenhauer (1788-1860), filósofo alemão',
    'Não se curem além da conta. Gente curada demais é gente chata. Todo mundo tem um pouco de loucura. - Autor: NIse da Silveira (1905- 1999), médica psiquiatra brasileira',
    'A violência, seja qual for a maneira como ela se manifesta, é sempre uma derrota. - Autora: Jean-Paul Sartre (1905-1980), filósofo e escritor francês',
    'A violência, seja qual for a maneira como ela se manifesta, é sempre uma derrota. - Autor: Carlos Drummond de Andrade (1902-1087), escritor brasileiro'
]

console.log(listaCitacoes)

let btn6 = document.querySelector('#btn6')

btn6.addEventListener('click', () => {

    var numeroRamdom = Math.floor(Math.random() * 5);
    let paragrafo = document.createElement('p');
    paragrafo.innerText = listaCitacoes[numeroRamdom]

    let minhaDiv2 = document.querySelector('#minhaDiv2')
    console.log(numeroRamdom);
    minhaDiv2.appendChild(paragrafo)

})


//Atividade 06
let inputValueA = document.querySelector('#inputValueA')
let inputValueB = document.querySelector('#inputValueB')

let btn7 = document.querySelector('#btn7')

btn7.addEventListener('click', () => {
    let valueA = parseInt(inputValueA.value)
    let valueB = parseInt(inputValueB.value)
    let soma = valueA + valueB
    console.log(soma)
})
