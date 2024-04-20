//Crie um algoritmo que verifique se uma palavra é um palíndromo.

function verificarPalindromo(palavra) {
    const palavraNormalizada = palavra.toLowerCase().replace(/[^a-z0-9]/gi, '');
    const palavraInvertida = palavraNormalizada.split('').reverse().join('');
    
    return palavraNormalizada === palavraInvertida;
  }
  
  // Exemplo de uso:
  const palavra = "Ana";
  const ehPalindromo = verificarPalindromo(palavra);
  console.log(`A palavra "${palavra}" é um palíndromo? ${ehPalindromo}`);

//**  Este código define uma função verificarPalindromo que recebe uma string palavra como argumento. Primeiro, normaliza a palavra removendo caracteres não alfanuméricos e convertendo para minúsculas. Depois, inverte a palavra e compara com a original normalizada. Se forem iguais, a palavra é um palíndromo e a função retorna true; caso contrário, retorna false. Você pode testar esse código para verificar diferentes palavras. Se tiver mais alguma dúvida ou precisar de ajuda com outra coisa, estou aqui para ajudar! */

//** Para otimizar a verificação de palíndromos em palavras longas, você pode implementar algumas melhorias no algoritmo. Aqui estão algumas sugestões: Evitar a normalização e reversão de toda a string: Em vez de criar uma nova string invertida e compará-la com a original, você pode simplesmente comparar os caracteres correspondentes nas posições iniciais e finais da string. Interrupção antecipada: Se em algum momento os caracteres não corresponderem, você pode interromper a verificação imediatamente, pois isso indica que a palavra não é um palíndromo. Comparação de metades: Como um palíndromo é simétrico, você só precisa comparar a primeira metade da palavra com a segunda metade invertida. Aqui está um exemplo de código otimizado com essas melhorias:*/

function verificarPalindromoOtimizado(palavra) {
    const palavraNormalizada = palavra.toLowerCase().replace(/[^a-z0-9]/gi, '');
    const meio = Math.floor(palavraNormalizada.length / 2);
  
    for (let i = 0; i < meio; i++) {
      if (palavraNormalizada[i] !== palavraNormalizada[palavraNormalizada.length - 1 - i]) {
        return false;
      }
    }
  
    return true;
  }
  
  // Exemplo de uso:
  const palavra = "Anotaram a data da maratona";
  const ehPalindromo = verificarPalindromoOtimizado(palavra);
  console.log(`A palavra "${palavra}" é um palíndromo? ${ehPalindromo}`);

//**Este código otimizado verifica apenas até a metade da palavra, economizando tempo e recursos, especialmente em palavras mais longas. Se a palavra for um palíndromo, todos os caracteres até a metade corresponderão aos seus pares na outra metade da palavra. Espero que essas dicas ajudem a otimizar seu algoritmo! Se tiver mais perguntas ou precisar de ajuda com algo mais, estou à disposição. */