# Validador-e-Gerador-de-CPF
Neste projeto você verá um menu com duas opções, nele você pode escolher validar o seu cpf ou escolher gerar um cpf válido.

O nome do projeto é auto-explicativo, porém darei algumas informações extras que pode ser que você não saiba:

Você sabe como é feito o processo de validação de um cpf?

Vamos pegar o CPF = 168.995.350-09 como exemplo:

1) Remover os 2 últimos dígitos do cpf (e os caracteres como: . ou -):
    Output: 168995350

1 * 10 = 10             #   1 * 11 = 11
6 * 9  = 54             #   6 * 10 = 60
8 * 8  = 64             #   8 * 9  = 72
9 * 7  = 63             #   9 * 8  = 72
9 * 6  = 54             #   9 * 7  = 63
5 * 5  = 25             #   5 * 6  = 30
3 * 4  = 12             #   3 * 5  = 15
5 * 3  = 15             #   5 * 4  = 20
0 * 2  = 0              #   0 * 3  = 0
                        #   0 * 2  = 0
        297             #           343
11 - (297 % 11) = 11    #     11 - (343 % 11) = 9
11 > 9 = 0              #
Digito 1 = 0            #   Digito 2 = 9

