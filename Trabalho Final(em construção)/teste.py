while True:

    print('''
    _______________________________________
    |           _______________           |
    |           | Bem Vindo à |           |
    |           |  ClickMed   |           |
    |           |_____________|           |
    |                                     |
    |              1. Login               |
    |              2. Cadastro            |
    |              0. Sair                |
    |_____________________________________|
    
    ''')

    op = input("Escolha o menu que deseja acessar:")

    match op:
        case "1":
            menuLogin()
        case "2":
            menuCadastro()
        case "0":
            print("Saindo da programa...")
            break
        case _:
            print("Escolha uma opção válida.")
    

            while True:

                print('''
                Bem vindo ao Campeonato
                1. Menu de Times
                2. Menu das Partidas
                3. Menu da Tabela
                0. Sair
                ''')

                op = input("Escolha o menu que deseja acessar:")

                match op:
                    case "1":
                        verMenuTimes()
                    case "2":
                        verMenuPartidas()
                    case "3":
                        verMenuTabela()
                    case "0":
                        print("Saindo da programa...")
                        break
                    case _:
                        print("Escolha uma opção válida.")