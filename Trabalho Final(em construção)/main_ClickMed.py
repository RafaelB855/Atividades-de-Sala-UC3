from conexao import Conexao
import random

def criarTabela(con):
    listaSql=['''
    CREATE TABLE "Pacientes"(
    "ID" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" varchar(255) NOT NULL,
    "CPF" int NOT NULL,
    "Nascimento" varchar(255) NOT NULL default 'Não Informado',
    "Cep" int NOT NULL default 00000000,
    "Complemento" varchar(255) NOT NULL default 'Não Informado'
    )
    ''',
    
    '''
    CREATE TABLE "Login"(
    "ID" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Username" varchar(255) NOT NULL,
    "Password" varchar(255) NOT NULL,
    "Email" varchar(255) NOT NULL,
    "ID_Paciente" int NOT NULL,
    CONSTRAINT fk_ID_Paciente
        FOREIGN KEY("ID_Paciente")
        REFERENCES "Pacientes"("ID")
    )
    ''',

    '''
    CREATE TABLE "Sintomas"(
    "ID" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" varchar(255) NOT NULL
    )
    ''',

    '''
    CREATE TABLE "Doenças"(
    "ID" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" varchar(255) NOT NULL,
    "Sintomas1" int NOT NULL,
    "Sintomas2" int NOT NULL default 0,
    "Sintomas3" int NOT NULL default 0,
    "Sintomas4" int NOT NULL default 0,
    "Remédio" varchar(255) NOT NULL,
    "Tratamento" varchar(255) NOT NULL,
    CONSTRAINT fk_Sintomas1
        FOREIGN KEY("Sintomas1")
        REFERENCES "Sintomas"("ID"),
    CONSTRAINT fk_Sintomas2
        FOREIGN KEY("Sintomas2")
        REFERENCES "Sintomas"("ID"),
    CONSTRAINT fk_Sintomas3
        FOREIGN KEY("Sintomas3")
        REFERENCES "Sintomas"("ID"),
    CONSTRAINT fk_Sintomas4
        FOREIGN KEY("Sintomas4")
        REFERENCES "Sintomas"("ID")
    )
    ''',

    '''
    CREATE TABLE "Atendimento"(
    "ID" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "ID_Paciente" int NOT NULL,
    "Sintomas1" int NOT NULL,
    "Intensidade1" int NOT NULL default 1,
    "Sintomas2" int NOT NULL default 0,
    "Intensidade2" int NOT NULL default 0,
    "Sintomas3" int NOT NULL default 0,
    "Intensidade3" int NOT NULL default 0,
    "Sintomas4" int NOT NULL default 0,
    "Intensidade4" int NOT NULL default 0,
    "Doença" int NOT NULL,
    CONSTRAINT fk_ID_Paciente
        FOREIGN KEY("ID_Paciente")
        REFERENCES "Pacientes"("ID"),
    CONSTRAINT fk_Sintomas1
        FOREIGN KEY("Sintomas1")
        REFERENCES "Sintomas"("ID"),
    CONSTRAINT fk_Sintomas2
        FOREIGN KEY("Sintomas2")
        REFERENCES "Sintomas"("ID"),
    CONSTRAINT fk_Sintomas3
        FOREIGN KEY("Sintomas3")
        REFERENCES "Sintomas"("ID"),
    CONSTRAINT fk_Sintomas4
        FOREIGN KEY("Sintomas4")
        REFERENCES "Sintomas"("ID"),
    CONSTRAINT fk_Doença
        FOREIGN KEY("Doença")
        REFERENCES "Doenças"("ID")
    )
    ''']

    for sql in listaSql:
        if con.manipularBanco(sql):
            print("Tabela criada.")
        else:
            print("Falha ao criar.")

conexaoBanco = Conexao("ClickMed","localhost","5432","postgres","postgres")
# criarTabela(conexaoBanco) 

#----------------------------------------------------------------------------------------------------------------------#

def menuLogin():
    loginl=[]
    nome = []

    username = input("Digite o seu Username:")
    password = input("Digite a sua Password:")

    try: 
        loginl = conexaoBanco.consultarBanco(f'''SELECT * FROM "Login"
        WHERE "Username" = '{username}' and "Password" = '{password}'
        ''')

        nome = conexaoBanco.consultarBanco(f'''SELECT * FROM "Pacientes"
        WHERE "ID" = '{loginl[0][4]}'
        ''')

        if loginl != []:
            print(f"Olá {nome[0][1]}, como podemos lhe ajudar.")
        
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
                    verMenuSintomas()
                case "2":
                    verMenuPartidas()
                case "3":
                    verMenuTabela()
                case "0":
                    print("Saindo da programa...")
                    break
                case _:
                    print("Escolha uma opção válida.")

    except:
        return "Falha no login"

#----------------------------------------------------------------------------------------------------------------------# 

def menuCadastroPaciente():
    IDpa = []

    print("Bem vindo ao Cadastro da ClickMec.")

    nome = input("Digite o seu Nome:")
    if nome == "":
        print("Inserira um nome valido!")
    cfp = input("Digite o seu CFP:")
    if cfp == "":
        print("Inserira um cfp valido!")
    if cfp.isdigit():
        nascimento = input("Digite sua data de nascimento:")
        cep = input("Digite seu Cep:")    
        complemento = input("Digite o complemento do seu endereço:")

        if conexaoBanco.manipularBanco(f'''
        INSERT INTO "Pacientes"
        Values(default, '{nome}', '{cfp}', '{nascimento}', '{cep}', '{complemento}')
        '''):
            print(f"Está info bem {nome}.")
        
        else:
            print("Ocorreu um erro")


        Username = input("Digite o seu Username1:")
        Password = input("Digite a sua Password:")
        Email = input("Digite o seu Email:")
        IDpa = conexaoBanco.consultarBanco(f'''SELECT * FROM "Pacientes"
        WHERE "Nome" = '{nome}' and "CPF" = '{cfp}'
        ''')
        ID_Paciente = IDpa[0][0]
        
        if conexaoBanco.manipularBanco(f'''
        INSERT INTO "Login"
        Values(default, '{Username}', '{Password}', '{Email}', '{ID_Paciente}')
        '''):
            print(f"Tudo certo no seu cadastro {nome}.")
        
        else:
            print("Ocorreu um erro")

#----------------------------------------------------------------------------------------------------------------------#

def verMenuSintomas():

    while True:
        print('''
        Opções menu Sintomas:
        1. Ver Sintomas
        2. Criar Sintoma
        3. Atualizar Sintoma
        4. Remover Sintoma
        0. Voltar ao menu principal
        ''')
        op = input("Escolha uma das opções:")
        match op:
            case "1":
                verListaDeSintomas()
            case "2":
                cadastrarNovoSintoma()
            case "3":
                atualizarSintoma()
            case "4":
                removerSintoma()
            case "0":
                print("Voltando ao menu principal...")
                break
            case _:
                print("Escolha uma opção válida.")

        input("Digite Enter para continuar...")

def verListaDeSintomas():

    listaSintomas = conexaoBanco.consultarBanco('''
    SELECT * FROM "Sintomas"
    ORDER BY "ID" ASC
    ''')

    if listaSintomas:
        print("ID | NOME")
        for Sintoma in listaSintomas:
            print(f"{Sintoma[0]} | {Sintoma[1]}")

        confirmar = input("Deseja ver as doenças que apresenta esse Sintoma? (S/N)").upper()

        match confirmar:
            case "S":
                SintomaEscolhido = input("Digite o id do Sintoma escolhido:")
                verSintomaEspecifico(SintomaEscolhido)
            case "N":
                print("Ok voltando ao menu principal")
            case _:
                print("Você digitou um comando inválido. Voltando ao menu.")

    else:
        print("Ocorreu um erro na consulta, ou a lista é vazia.")

def cadastrarNovoSintoma():
    print("Cadastro de Sintoma - Insira as informações pedidas")

    nome = input("Digite o nome do Sintoma:")
    if nome == "":
        print("Inserira um nome valido!")
    
    else:
        sqlInserir = f'''
        INSERT INTO "Sintomas"
        Values(default, '{nome}')
        '''
        
        if conexaoBanco.manipularBanco(sqlInserir):

            print(f"O sintoma {nome} foi inserido com sucesso.")
        else:
            print("Falha ao inserir o time!")

def atualizarSintoma():
    print("Tela de atualização de Sintoma:")
    print("Lista de Sintomas")
    
    listaSintomas = conexaoBanco.consultarBanco('''
    SELECT * FROM "Sintomas"
    ORDER BY "ID" ASC
    ''')

    if listaSintomas:
        print("ID | NOME")
        for Sintoma in listaSintomas:
            print(f"{Sintoma[0]} | {Sintoma[1]}")

    SintomaEscolhido = input("Digite o id do Sintoma escolhido:")
    if SintomaEscolhido.isdigit():
        verSintomaEspecifico(SintomaEscolhido)
        novoNome = input("Digite o novo nome (vazio para não alterar):")
    
        if novoNome:
            conexaoBanco.manipularBanco(f'''
            UPDATE "Sintomas"
            SET "Nome" = '{novoNome}'
            WHERE "ID" = {SintomaEscolhido}
            ''')

            print(f"O nome foi alterado para '{novoNome}'.")
        
        if novoNome == "":
            print("O nome não foi alterado.")

def verSintomaEspecifico(idSintoma):
    Sintoma = conexaoBanco.consultarBanco(f'''SELECT * FROM "Sintomas"
    WHERE "ID" = {idSintoma}
    ''')

    if Sintoma:
        Sintoma = Sintoma[0]
        print("Sintoma Escolhido: ")
        print(f'''
        ID - {Sintoma[0]}
        Nome - {Sintoma[1]}
        ''')

        listaDoenças = conexaoBanco.consultarBanco(f'''
        SELECT * FROM "Doenças"
        WHERE "Sintomas1" = '{Sintoma[0]}' or "Sintomas2" = '{Sintoma[0]}' or "Sintomas3" = '{Sintoma[0]}' or "Sintomas4" = '{Sintoma[0]}'
        ''')

        if listaDoenças:
            print("{:^7} | {:^20} ".format("ID" ,"Nome"))
            for Doença in listaDoenças:
                print("{:^7} | {:^20} ".format((Doença[0]), (Doença[1])))

        else:
            print("O Sintoma não apresenta em nenhuma doença cadastrada.")

    else:
        print("O Sintoma não foi encontrado!")

def removerSintoma():
    print("Tela de remoção de Sintoma:")
    print("Lista de Sintomas")
    
    listaSintomas = conexaoBanco.consultarBanco('''
    SELECT * FROM "Sintomas"
    ORDER BY "ID" ASC
    ''')

    if listaSintomas:
        print("ID | NOME")
        for Sintoma in listaSintomas:
            print(f"{Sintoma[0]} | {Sintoma[1]}")

    SintomaEscolhido = input("Digite o id do Sintoma escolhido:")
    if SintomaEscolhido.isdigit():
        verSintomaEspecifico(SintomaEscolhido)
    confirmar = input("Deseja remover este Sintoma? (S/N)").upper()

    match confirmar:
        case "S":
           resultadoRemocao = conexaoBanco.manipularBanco(f'''
           DELETE FROM "Sintomas"
           WHERE "ID" = '{SintomaEscolhido}'
           ''')
           
           if resultadoRemocao:
               print("Sintoma removido com sucesso.")
           else:
               print("Sintoma não existe ou não foi removido.")
        case "N":
            print("Ok voltando ao menu principal")
        case _:
            print("Você digitou um comando inválido. Voltando ao menu.")

# #----------------------------------------------------------------------------------------------------------------------#

def verMenuPartidas():

    while True:
        print('''
        Opções menu Times:
        1. Ver Partidas
        2. Gerar Campeonato
        3. Criar Partida(Manualmente)
        4. Atualizar Partida
        5. Remover Partida
        6. zerar Partidas
        0. Voltar ao menu principal
        ''')
        op = input("Escolha uma das opções:")
        match op:
            case "1":
                verListaDePartidas()
            case "2":
                gerarCampeonato()
            case "3":
                criarPartida()
            case "4":
                atualizarPartida()
            case "5":
                removerPartida()
            case "6":
                zerarPartidas()
            case "0":
                print("Voltando ao menu principal...")
                break
            case _:
                print("Escolha uma opção válida.")

        input("Digite Enter para continuar...")

def verListaDePartidas():

    listaPartidas = conexaoBanco.consultarBanco('''
    SELECT * FROM "Partidas"
    ORDER BY "ID" ASC
    ''')

    if listaPartidas:
        print("{:^9} | {:^9} | {:^9} ".format("TIME" ,"PLACAR" ,"TIME"))
        for Partida in listaPartidas:
            
            Time1daPartida = conexaoBanco.consultarBanco(f'''
                SELECT * FROM "Times"
                WHERE "ID" = '{Partida[1]}'
                ''')[0]
            
            Time2daPartida = conexaoBanco.consultarBanco(f'''
                SELECT * FROM "Times"
                WHERE "ID" = '{Partida[4]}'
                ''')[0]

            print("{:^9} | {:^3}/{:^3} | {:^9} ".format((Time1daPartida[1]), (Partida[2]), (Partida[3]), (Time2daPartida[1])))

    else:
        print("Ocorreu um erro na consulta, ou a lista é vazia.")

def gerarCampeonato():

    listaTimes = conexaoBanco.consultarBanco('''
    SELECT * FROM "Times"
    ''')

    for Time1 in listaTimes:
        Time1 = Time1[0]
        for Time2 in listaTimes:
            Time2 = Time2[0]
            if Time1 != Time2:
                Gols1 = random.randrange(0,5)
                Gols2 = random.randrange(0,5)
                sqlInserir = f'''
                    INSERT INTO "Partidas"
                    Values(default,{Time1},{Gols1},{Gols2},{Time2})
                    '''
                    
                if conexaoBanco.manipularBanco(sqlInserir):
                    print("Campeonato gerado com sucesso.")
                else:
                    print("Falha ao gerar campeonato!")

def criarPartida():

    listaTimes = conexaoBanco.consultarBanco('''
    SELECT * FROM "Times"
    ORDER BY "ID" ASC
    ''')

    if listaTimes:
        print("ID | NOME")
        for Time in listaTimes:
            print(f"{Time[0]} | {Time[1]}")

    else:
        print("Ocorreu um erro na consulta, ou a lista é vazia.")


    Time1 = input("Digite o id do time desejado:")
    if Time1.isdigit():
        Time2 = input(f"Digite o id do time que iria enfrentar o time {Time1}:")
        if Time1 != Time2 and Time2.isdigit():
            Gols1 = input("Digite a quantidade de gols do time escolhido:")
            if Gols1.isdigit():
                Gols2 = input("Digite a quantidade de gols do time adversário:")
                if Gols2.isdigit():
                    sqlInserir = f'''
                        INSERT INTO "Partidas"
                        Values(default, {Time1},{Gols1},{Gols2},{Time2})
                        '''
                                
                if conexaoBanco.manipularBanco(sqlInserir):
                    print("Partida gerada com sucesso.")
                else:
                    print("Falha ao gerar Partida!")
    else:
        print("Escolha uma opção válida.")

def atualizarPartida():
    print("Tela de atualização de Partida:")
    print("Lista de Partidas")
    
    verListaDePartidas()
    PartidaEscolhido = input("Digite o id do partida escolhida:")
    if PartidaEscolhido.isdigit():
        verPartidaEspecifico(PartidaEscolhido)
        Time1 = input("Digite o id do time desejado:")
        if Time1.isdigit():
            Time2 = input(f"Digite o id do time que iria enfrentar o time {Time1}:")
            if Time1 != Time2 and Time2.isdigit():
                Gols1 = input("Digite a quantidade de gols do time escolhido:")
                if Gols1.isdigit():
                    Gols2 = input("Digite a quantidade de gols do time adversário:")
                    if Gols2.isdigit():
                        sqlInserir = f'''
                           UPDATE "Partidas"
                            SET "Time1" = {Time1}, "Gols1" = {Gols1}, "Gols2" = {Gols2}, "Time2" = {Time2}
                            WHERE "ID" = {PartidaEscolhido[0]}
                            '''
                                    
                    if conexaoBanco.manipularBanco(sqlInserir):
                        print("Partida alterada com sucesso.")
                    else:
                        print("Falha ao gerar Partida!")
    else:
        print("Escolha uma opção válida.")

def verPartidaEspecifico(idPartida):

    listaPartidas = conexaoBanco.consultarBanco(f'''
    SELECT * FROM "Partidas"
    WHERE "ID" = {idPartida[0]}
    ''')

    if listaPartidas:
        print("{:^9} | {:^9} | {:^9} ".format("TIME" ,"PLACAR" ,"TIME"))
        for Partida in listaPartidas:
            
            Time1daPartida = conexaoBanco.consultarBanco(f'''
                SELECT * FROM "Times"
                WHERE "ID" = '{Partida[1]}'
                ''')[0]
            
            Time2daPartida = conexaoBanco.consultarBanco(f'''
                SELECT * FROM "Times"
                WHERE "ID" = '{Partida[4]}'
                ''')[0]
            
            print("{:^9} | {:^3}/{:^3} | {:^9} ".format((Time1daPartida[1]), (Partida[2]), (Partida[3]), (Time2daPartida[1])))


    else:
        print("O Partidas não foi encontradas!")

def removerPartida():
    print("Tela de remoção de Partida:")
    print("Lista de Partidas")
    
    verListaDePartidas()
    partidaEscolhido = input("Digite o id do partida escolhida:")
    verPartidaEspecifico(partidaEscolhido)
    confirmar = input("Deseja remover esta partida? (S/N)").upper()

    match confirmar:
        case "S":
           resultadoRemocao = conexaoBanco.manipularBanco(f'''
           DELETE FROM "Partidas"
           WHERE "ID" = '{partidaEscolhido}'
           ''')
           
           if resultadoRemocao:
               print("Partida removida com sucesso.")
           else:
               print("Partida não existe ou não foi removido.")
        case "N":
            print("Ok voltando ao menu principal")
        case _:
            print("Você digitou um comando inválido. Voltando ao menu.")

def zerarPartidas():

    print("Tela de remoção de campeonato:")
    print("Lista de Partidas")
    
    verListaDePartidas()

    listaPartidas = conexaoBanco.consultarBanco('''
    SELECT * FROM "Partidas"
    ORDER BY "ID" ASC
    ''')

    confirmar = input("Deseja remover zerar tabela? (S/N)").upper()

    match confirmar:
        case "S":
           
           for idPartida in  listaPartidas:
            sqlRemocao = f'''
            DELETE FROM "Partidas"
            WHERE "ID" = '{idPartida[0]}'
            '''
            
            if conexaoBanco.manipularBanco(sqlRemocao):
                print("Campeonato zerada com sucesso.")
            else:
                print("Partida não existe ou não foi removido.")
        case "N":
            print("Ok voltando ao menu principal")
        case _:
            print("Você digitou um comando inválido. Voltando ao menu.")

# #----------------------------------------------------------------------------------------------------------------------#

def verMenuTabela():

    while True:
        print('''
        Opções menu Tabela:
        1. Ver Tabela
        2. Atualizar Tabela
        3. Zerar Tabela
        0. Voltar ao menu principal
        ''')
        op = input("Escolha uma das opções:")
        match op:
            case "1":
                verListaDeTabela()
            case "2":
                atualizarTabela()
            case "3":
                zerarTabela()
            case "0":
                print("Voltando ao menu principal...")
                break
            case _:
                print("Escolha uma opção válida.")

        input("Digite Enter para continuar...")

def verListaDeTabela():

    i = 0

    listaTabelas = conexaoBanco.consultarBanco('''
    SELECT * FROM "Tabela"
    ORDER BY "Pontos" DESC
    ''')

    if listaTabelas:
        print("{:^6} | {:^9} | {:^6} | {:^6} | {:^6} | {:^6} | {:^6} | {:^6} | {:^6}".format("Rank", "Time", "P", "V", "E" , "D" , "GP" , "GC" , "SG"))
        for Tabela in listaTabelas:

            i = i + 1
            
            TimedaTabela = conexaoBanco.consultarBanco(f'''
                SELECT * FROM "Times"
                WHERE "ID" = '{Tabela[1]}'
                ''')[0]

            print("{:^6} | {:^9} | {:^6} | {:^6} | {:^6} | {:^6} | {:^6} | {:^6} | {:^6}".format((i), (TimedaTabela[1]), (Tabela[2]), (Tabela[3]), (Tabela[4]), (Tabela[5]), (Tabela[6]), (Tabela[7]), (Tabela[8])))
            
    else:
        print("Ocorreu um erro na consulta, ou a lista é vazia.")

def atualizarTabela():

    listaTimes = conexaoBanco.consultarBanco('''
    SELECT * FROM "Times"
    ORDER BY "ID" ASC
    ''')

    for idTime in listaTimes:
        idTime = idTime[0]

        vitoria = 0
        empate = 0
        derrota = 0
        pontosV = 0
        pontosE = 0
        pontosD = 0
        golsPros = 0
        golsContras = 0
        golsProsTotal = 0
        golsContrasTotal = 0
        saldodeGolsTotais = 0
        vitoriaF = 0
        empateF = 0
        derrotaF = 0
        pontosVF = 0
        pontosEF = 0
        pontosDF = 0
        golsProsF = 0
        golsContrasF = 0

        Time = conexaoBanco.consultarBanco(f'''SELECT * FROM "Times"
        WHERE "ID" = {idTime}
        ''')

        if Time:
            Time = Time[0]
            print("Time Escolhido: ")
            print(f'''
            ID - {Time[0]}
            Nome - {Time[1]}
            ''')

            listaPartidas = conexaoBanco.consultarBanco(f'''
            SELECT * FROM "Partidas"
            WHERE "Time1" = '{Time[0]}'
            ''')

            for partida in listaPartidas:

                if partida[2]<partida[3]:
                    vitoria = vitoria + 1
                    pontosV = pontosV + 3 
                if partida[2]==partida[3]:
                    empate = empate + 1
                    pontosE = pontosE + 1
                if partida[2]>partida[3]:
                    derrota = derrota + 1
                    pontosD = pontosD + 0

                golsPros = golsPros + partida[2]
                golsContras = golsContras + partida[3]

            listaPartidasFora = conexaoBanco.consultarBanco(f'''
            SELECT * FROM "Partidas"
            WHERE "Time2" = '{Time[0]}'
            ''')

            for partidaF in listaPartidasFora:

                if partidaF[2]<partidaF[3]:
                    vitoriaF = vitoriaF + 1
                    pontosVF = pontosVF + 3
                if partidaF[2]==partidaF[3]:
                    empateF = empateF + 1
                    pontosEF = pontosEF + 1
                if partidaF[2]>partidaF[3]:
                    derrotaF = derrotaF + 1
                    pontosDF = pontosDF + 0

                golsProsF = golsProsF + partidaF[3]
                golsContrasF = golsContrasF + partidaF[2]


                vitoriasTotais = vitoria + vitoriaF
                empatesTotais = empate + empateF
                derrotasTotais = derrota + derrotaF
                pontosTotais = pontosV + pontosE + pontosVF + pontosEF

            golsProsTotal = golsProsTotal +(golsPros + golsProsF)
            golsContrasTotal = golsContrasTotal + (golsContras + golsContrasF)
                
            saldodeGolsTotais = saldodeGolsTotais + (golsProsTotal - golsContrasTotal)

        sqlInserir = f'''
        INSERT INTO "Tabela"
        Values(default, {idTime},{pontosTotais},{vitoriasTotais},{empatesTotais},{derrotasTotais},{golsProsTotal},{golsContrasTotal},{saldodeGolsTotais})
        '''
    
        if conexaoBanco.manipularBanco(sqlInserir):

            print(f"A Tabela foi atualizada com sucesso.")
        else:
            print("Falha ao atualizar tabela!")

    else:
        print("O time não foi encontrado!")
    
def zerarTabela():

    print("Tela de remoção de tabela:")
    print("Lista de Tabela")
    
    verListaDeTabela()

    listaTabela = conexaoBanco.consultarBanco('''
    SELECT * FROM "Tabela"
    ORDER BY "ID" ASC
    ''')

    confirmar = input("Deseja remover zerar tabela? (S/N)").upper()

    match confirmar:
        case "S":
           
           for idTabela in  listaTabela:
            sqlRemocao = f'''
            DELETE FROM "Tabela"
            WHERE "ID" = '{idTabela[0]}'
            '''
            
            if conexaoBanco.manipularBanco(sqlRemocao):
                print("Tabela zerada com sucesso.")
            else:
                print("Tabela não existe ou não foi removido.")
        case "N":
            print("Ok voltando ao menu principal")
        case _:
            print("Você digitou um comando inválido. Voltando ao menu.")

# #----------------------------------------------------------------------------------------------------------------------#

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
            menuCadastroPaciente()
        case "0":
            print("Saindo da programa...")
            break
        case _:
            print("Escolha uma opção válida.")