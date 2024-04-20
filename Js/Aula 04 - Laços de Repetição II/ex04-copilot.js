//Crie um algoritmo que conte a quantidade de vogais que um texto tem.

function contarVogais(texto) {
    const vogais = 'aeiouAEIOU';
    let contador = 0;
  
    for (let i = 0; i < texto.length; i++) {
      if (vogais.includes(texto[i])) {
        contador++;
      }
    }
  
    return contador;
  }
  
  // Exemplo de uso:
  const texto = "Este é um exemplo de texto para contagem de vogais.";
  const quantidadeDeVogais = contarVogais(texto);
  console.log(`O texto contém ${quantidadeDeVogais} vogais.`);
  
  //**  Esse código define uma função contarVogais que recebe uma string texto como argumento. Ele itera sobre cada caractere do texto e verifica se é uma vogal (tanto maiúscula quanto minúscula) usando o método includes. Cada vez que encontra uma vogal, incrementa o contador. No final, a função retorna o número total de vogais encontradas no texto. Você pode testar esse código em seu ambiente de desenvolvimento ou em qualquer editor de código online que suporte JavaScript. Se precisar de mais ajuda ou quiser adicionar mais funcionalidades, fique à vontade para perguntar! */