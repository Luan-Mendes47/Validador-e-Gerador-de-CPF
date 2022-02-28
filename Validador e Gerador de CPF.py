from random import randint


def validacpf():
    cpf = input('Digite o cpf: ')
    novo_cpf = cpf[:-2]
    if len(cpf) == 11:
        reverso = 10
        total = 0
        for index in range(19):
            if index > 8:
                index -= 9

            total += int(novo_cpf[index]) * reverso

            reverso -= 1
            if reverso < 2:
                reverso = 11
                d = 11 - (total % 11)

                if d > 9:
                    d = 0
                total = 0
                novo_cpf += str(d)
        if cpf == novo_cpf:
            print(f'{cpf} é um cpf válido')
        else:
            print(f'{cpf} é Inválido')
    elif len(cpf) > 11:
        not_num = '.-'
        for caract in not_num:
            cpf = cpf.replace(caract, '')
        for caract in not_num:
            novo_cpf = novo_cpf.replace(caract, '')
        reverso = 10
        total = 0
        for index in range(19):
            if index > 8:
                index -= 9

            total += int(novo_cpf[index]) * reverso

            reverso -= 1
            if reverso < 2:
                reverso = 11
                d = 11 - (total % 11)

                if d > 9:
                    d = 0
                total = 0
                novo_cpf += str(d)
        if cpf == novo_cpf:
            print(f'{cpf} é um cpf válido')
        else:
            print(f'{cpf} é Inválido')
    else:
        print('ERRO, VERIFIQUE SE O CPF FOI CORRETAMENTE DIGITADO E TENTE NOVAMENTE.')


def geracpfvalido():
    num = str(randint(100000000, 999999999))

    novo_cpf = num
    reverso = 10
    total = 0
    for index in range(19):
        if index > 8:
            index -= 9

        total += int(novo_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)
    print(novo_cpf)


def menu():
    print('_________________________')
    print('Validar cpf           (1)')
    print('Gerar cpf válido      (2)')
    print('_________________________')


loop = True
while loop:
    menu()
    op = input('Input: ')
    if op == '1':
        validacpf()
    elif op == '2':
        geracpfvalido()
    else:
        print('Erro: Opção inválida!')
    s = input('Sair? s[sim] n[não] ')
    if s.lower() == 's':
        loop = False
