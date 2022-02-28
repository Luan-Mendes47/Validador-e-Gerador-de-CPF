# Validador-e-Gerador-de-CPF
Neste projeto você verá um menu com duas opções, nele você pode escolher validar o seu cpf ou escolher gerar um cpf válido.

O nome do projeto é auto-explicativo, porém darei algumas informações extras que pode ser que você não saiba:

Você sabe como é feito o processo de validação de um cpf?

Vamos pegar o CPF = 168.995.350-09 como exemplo:

1) Remover os 2 últimos dígitos do cpf e os caracteres: '.' e '-'. 
     novo cpf = 168995350

2) Após isso deve-se multiplicar o primeiro dígito por 10, o segundo por 9, e assim sucessivamente até chegar no último digito que será multiplicado por 2.

     1 * 10 = 10             
     6 * 9  = 54            
     8 * 8  = 64             
     9 * 7  = 63             
     9 * 6  = 54             
     5 * 5  = 25             
     3 * 4  = 12             
     5 * 3  = 15             
     0 * 2  = 0              
       
3) Somar todos os resultados e realizar a equação:
   11 - (Soma dos resultados % 11)
   
     11 - (297 % 11) = 11    
     11 > 9 = 0              
     Digito 1 = 0  

4) Com isso descobrimos o valor do primeiro dígito (neste exemplo: 0)

5) Agora multiplicamos como anteriormente, porém agora adicionamos ao cpf o dígito que acabamos de descobrir (novo cpf = 1689953500) e começando a partir do número 11:
 
     1 * 11 = 11;
     6 * 10 = 60; 
     8 * 9  = 72; 
     9 * 8  = 72; 
     9 * 7  = 63; 
     5 * 6  = 30; 
     3 * 5  = 15; 
     5 * 4  = 20; 
     0 * 3  = 0; 
     0 * 2  = 0;    
  
      11 - (343 % 11) = 9

     Digito 2 = 9

6) Fizemos a soma dos resultados como anteriormente e realizamos a mesma equação (11 - (Soma dos resultados % 11)). Com isso descobrimos o segundo dígito (neste exemplo: 9).

7) Agora adicionamos o dígito 2 ao nosso novo cpf (novo cpf = 16899535009).

8) Por último, comparamos o cpf antigo com o novo, se forem iguais então o CPF é válido, caso contrário, inválido.
