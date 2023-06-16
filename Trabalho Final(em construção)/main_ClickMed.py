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
    "Sintomas2" int,
    "Sintomas3" int,
    "Sintomas4" int,
    "Remédio" varchar(255),
    "Tratamento" varchar(255),
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
    "Sintomas2" int,
    "Intensidade2" int NOT NULL default 0,
    "Sintomas3" int,
    "Intensidade3" int NOT NULL default 0,
    "Sintomas4" int,
    "Intensidade4" int NOT NULL default 0,
    "Doença" int,
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
            Bem vindo ao ClickMed
            1. Menu de Sintomas
            2. Menu das Doenças
            3. Menu de Atendimento
            0. Sair
            ''')

            op = input("Escolha o menu que deseja acessar:")

            match op:
                case "1":
                    verMenuSintomas()
                case "2":
                    verMenuDoenças()
                case "3":
                    verMenuAtendimento()
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
    else:
        return "Escolha uma opção válida."

def verSintomaEspecifico(idSintoma):
    Sintoma = conexaoBanco.consultarBanco(f'''SELECT * FROM "Sintomas"
    WHERE "ID" = '{idSintoma}'
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

    else:
        return "Escolha uma opção válida."

# #----------------------------------------------------------------------------------------------------------------------#

def verMenuDoenças():

    while True:
        print('''
        Opções menu Times:
        1. Ver Doenças
        2. Criar Doença
        3. Ver Tratamento/Remedio da Doença
        4. Criar/Atualizar Tratamento/Remedio da Doença
        5. Atualizar Doença
        6. Remover Doença
        0. Voltar ao menu principal
        ''')
        op = input("Escolha uma das opções:")
        match op:
            case "1":
                verListaDeDoenças()
            case "2":
                criarDoença()
            case "3":
                verTratamentodeDoença()
            case "4":
                criarAtualizarTratamentoparaDoença()
            case "5":
                atualizarDoença()
            case "6":
                removerDoença()
            case "0":
                print("Voltando ao menu principal...")
                break
            case _:
                print("Escolha uma opção válida.")

        input("Digite Enter para continuar...")

def verListaDeDoenças():

    listaDoenças = conexaoBanco.consultarBanco('''
    SELECT * FROM "Doenças"
    ORDER BY "ID" ASC
    ''')

    if listaDoenças:
        print("DOENÇAS   |   SINTOMAS APRESENTADOS")
        for Doença in listaDoenças:
            
            if Doença[3] == None:
                listadeSintomas1 = conexaoBanco.consultarBanco(f'''
                    SELECT * FROM "Sintomas"
                    WHERE "ID" = '{Doença[2]}'
                    ''')[0]
                print(f"{Doença[1]} | {listadeSintomas1[1]}")
                
            if Doença[4] == None:
                listadeSintomas1 = conexaoBanco.consultarBanco(f'''
                    SELECT * FROM "Sintomas"
                    WHERE "ID" = '{Doença[2]}'
                    ''')[0]
                listadeSintomas2 = conexaoBanco.consultarBanco(f'''
                    SELECT * FROM "Sintomas"
                    WHERE "ID" = '{Doença[3]}'
                    ''')[0]
                print(f"{Doença[1]} | {listadeSintomas1[1]} - {listadeSintomas2[1]}")
                
            if Doença[5] == None:
                listadeSintomas1 = conexaoBanco.consultarBanco(f'''
                    SELECT * FROM "Sintomas"
                    WHERE "ID" = '{Doença[2]}'
                    ''')[0]
                listadeSintomas2 = conexaoBanco.consultarBanco(f'''
                    SELECT * FROM "Sintomas"
                    WHERE "ID" = '{Doença[3]}'
                    ''')[0]
                listadeSintomas3 = conexaoBanco.consultarBanco(f'''
                    SELECT * FROM "Sintomas"
                    WHERE "ID" = '{Doença[4]}'
                    ''')[0]

                print(f"{Doença[1]} | {listadeSintomas1[1]} - {listadeSintomas2[1]} - {listadeSintomas3[1]}")
                    
            else:
                listadeSintomas1 = conexaoBanco.consultarBanco(f'''
                    SELECT * FROM "Sintomas"
                    WHERE "ID" = '{Doença[2]}'
                    ''')[0]
                listadeSintomas2 = conexaoBanco.consultarBanco(f'''
                    SELECT * FROM "Sintomas"
                    WHERE "ID" = '{Doença[3]}'
                    ''')[0]
                listadeSintomas3 = conexaoBanco.consultarBanco(f'''
                    SELECT * FROM "Sintomas"
                    WHERE "ID" = '{Doença[4]}'
                    ''')[0]
                listadeSintomas4 = conexaoBanco.consultarBanco(f'''
                    SELECT * FROM "Sintomas"
                    WHERE "ID" = '{Doença[5]}'
                    ''')[0]

                print(f"{Doença[1]} | {listadeSintomas1[1]} - {listadeSintomas2[1]} - {listadeSintomas3[1]} - {listadeSintomas4[1]}")

    else:
        print("Ocorreu um erro na consulta, ou a lista é vazia.")

def criarDoença():

    nomeD = input("Digite o nome do Sintoma:")
    if nomeD == "":
        print("Inserira um nome valido!")

    listaSintomas = conexaoBanco.consultarBanco('''
    SELECT * FROM "Sintomas"
    ORDER BY "ID" ASC
    ''')

    if listaSintomas:
        print("Esses são os sintomas cadastrados no sistema:")
        print("ID | NOME")
        for Sintoma in listaSintomas:
            print(f"{Sintoma[0]} | {Sintoma[1]}")


    Sintoma1 = input("Digite o id do Sintoma desejado:")
    if Sintoma1.isdigit():

        confirmar = input("Deseja adicionar mais um Sintoma? (S/N)").upper()

        match confirmar:
            case "S":
                Sintoma2 = input(f"Digite o id do segundo Sintoma:")
                if Sintoma1 != Sintoma2 and Sintoma2.isdigit():

                    confirmar = input("Deseja adicionar mais um Sintoma? (S/N)").upper()

                    match confirmar:
                        case "S":
                            Sintoma3 = input(f"Digite o id do terceiro Sintoma:")
                            if Sintoma1 != Sintoma3 and Sintoma2 != Sintoma3 and Sintoma3.isdigit():
                                match confirmar:
                                    case "S":
                                        Sintoma4 = input(f"Digite o id do quarto Sintoma:")
                                        if Sintoma1 != Sintoma4 and Sintoma2 != Sintoma4 and Sintoma3 != Sintoma4 and Sintoma4.isdigit():
                                            sqlInserir = f'''
                                            INSERT INTO "Doenças"
                                            Values(default,'{nomeD}','{Sintoma1}','{Sintoma2}','{Sintoma3}','{Sintoma4}')
                                            '''
                                    case "N":
                                        sqlInserir = f'''
                                            INSERT INTO "Doenças"
                                            Values(default,'{nomeD}','{Sintoma1}','{Sintoma2}','{Sintoma3}')
                                            '''
                                    case _:
                                        print("Você digitou um comando inválido. Voltando ao menu.")
                        case "N":
                            sqlInserir = f'''
                                INSERT INTO "Doenças"
                                Values(default,'{nomeD}','{Sintoma1}','{Sintoma2}')
                                '''
                        case _:
                            print("Você digitou um comando inválido. Voltando ao menu.")

            case "N":
                sqlInserir = f'''
                    INSERT INTO "Doenças"
                    Values(default,'{nomeD}','{Sintoma1}')
                    '''
            case _:
                print("Você digitou um comando inválido. Voltando ao menu.")
                                
        if conexaoBanco.manipularBanco(sqlInserir):
            return "Partida gerada com sucesso."
        else:
            return "Falha ao gerar Partida!"
    else:
       return "Escolha uma opção válida."

def verTratamentodeDoença():

    print("Lista de doenças:")
    verListaDeDoenças()
    doençadesejada = input("Digite o ID da Doença que deseja ver o Tratamento:")
    if doençadesejada == "" and not doençadesejada.isdigit():
        print("Inserira um ID valido!")
    else:
        doençadesejada1 = conexaoBanco.consultarBanco(f'''
            SELECT * FROM "Doenças"
            WHERE "ID" = '{doençadesejada}'
            ''')[0]
        
        if doençadesejada1[6] == None and doençadesejada1[7] == None:
            print("Doença não possui um tratamento cadastrado.")

        if doençadesejada1[6] == None:
            print("Doença    |     Tratamento")
            print(f"{doençadesejada1[1]} | {doençadesejada1[7]}")

        if doençadesejada1[7] == None:
            print("Doença    |     Tratamento")
            print(f"{doençadesejada1[1]} | {doençadesejada1[6]}")

        else:
            print("Doença    |     Tratamento")
            print(f"{doençadesejada1[1]} | {doençadesejada1[6]}\{doençadesejada1[7]}")

def criarAtualizarTratamentoparaDoença():

    print("Lista de doenças:")
    verListaDeDoenças()
    doençadesejada = input("Digite o ID da Doença que deseja ver o Tratamento:")
    if doençadesejada == "" and not doençadesejada.isdigit():
        print("Inserira um ID valido!")
    else:
        doençadesejada1 = conexaoBanco.consultarBanco(f'''
            SELECT * FROM "Doenças"
            WHERE "ID" = '{doençadesejada}'
            ''')[0]
        
        if doençadesejada1[6] == None and doençadesejada1[7] == None:
            print("Doença não possui um tratamento cadastrado.")

        if doençadesejada1[6] == None:
            print("Doença    |     Tratamento")
            print(f"{doençadesejada1[1]} | {doençadesejada1[7]}")

        if doençadesejada1[7] == None:
            print("Doença    |     Tratamento")
            print(f"{doençadesejada1[1]} | {doençadesejada1[6]}")

        else:
            print("Doença    |     Tratamento")
            print(f"{doençadesejada1[1]} | {doençadesejada1[6]}\{doençadesejada1[7]}")

    confirmar = input("Deseja criar um tratamento para essa doença? (S/N)").upper()

    match confirmar:
        case "S":
            remedio = input("Digite o remédio da Doença:(Deixe vazio caso não queria adicionar)")
            tratamento = input("Digite o tratamento da Doença:(Deixe vazio caso não queria adicionar)")

            if remedio == None and tratamento == None:
                print("Remédio e tratamento vazio. Voltando ao menu.")

            if remedio == None:
                sqlInserir = f'''
                    UPDATE "Doenças"
                    SET "Tratamento" = '{tratamento}'
                    WHERE "ID" = {doençadesejada}
                    '''
                if conexaoBanco.manipularBanco(sqlInserir):
                        print("Tratamento gerado com sucesso.")
                else:
                    print("Falha ao criar tratamento para doença!")

            if tratamento == None:
                sqlInserir = f'''
                    UPDATE "Doenças"
                    SET "Remédio" = '{remedio}'
                    WHERE "ID" = {doençadesejada}
                    '''
                if conexaoBanco.manipularBanco(sqlInserir):
                        print("Tratamento gerado com sucesso.")
                else:
                    print("Falha ao criar tratamento para doença!")

            else:
                sqlInserir = f'''
                    UPDATE "Doenças"
                    SET "Remédio" = '{remedio}', "Tratamento" = '{tratamento}'
                    WHERE "ID" = {doençadesejada}
                    '''
                if conexaoBanco.manipularBanco(sqlInserir):
                        print("Tratamento gerado com sucesso.")
                else:
                    print("Falha ao criar tratamento para doença!")

        case "N":
            print("Ok voltando ao menu principal")
        case _:
            print("Você digitou um comando inválido. Voltando ao menu.")

def atualizarDoença():

    print("Tela de atualização de Doença:")
    print("Lista de Doenças")
    
    verListaDeDoenças()
    DoençaEscolhido = input("Digite o id do Doença escolhida:")

    if DoençaEscolhido.isdigit() and not DoençaEscolhido == None:
        verDoençaEspecifico(DoençaEscolhido)

        confirmar = input("Deseja realmente atualizar essa doença? (S/N)").upper()

        match confirmar:
            case "S":
                nomeD = input("Digite o nome do Doença:")
                if nomeD == "":
                    print("Inserira um nome valido!")

                listaSintomas = conexaoBanco.consultarBanco('''
                SELECT * FROM "Sintomas"
                ORDER BY "ID" ASC
                ''')

                if listaSintomas:
                    print("Esses são os sintomas cadastrados no sistema:")
                    print("ID | NOME")
                    for Sintoma in listaSintomas:
                        print(f"{Sintoma[0]} | {Sintoma[1]}")


                Sintoma1 = input("Digite o id do Sintoma desejado:")
                if Sintoma1.isdigit():

                    confirmar = input("Deseja adicionar um segundo Sintoma? (S/N)").upper()

                    match confirmar:
                        case "S":
                            Sintoma2 = input(f"Digite o id do segundo Sintoma:")
                            if Sintoma1 != Sintoma2 and Sintoma2.isdigit():

                                confirmar = input("Deseja adicionar um terceiro Sintoma? (S/N)").upper()

                                match confirmar:
                                    case "S":
                                        Sintoma3 = input(f"Digite o id do terceiro Sintoma:")
                                        if Sintoma1 != Sintoma3 and Sintoma2 != Sintoma3 and Sintoma3.isdigit():

                                            confirmar = input("Deseja adicionar um quarto Sintoma? (S/N)").upper()

                                            match confirmar:
                                                case "S":
                                                    Sintoma4 = input(f"Digite o id do quarto Sintoma:")
                                                    if Sintoma1 != Sintoma4 and Sintoma2 != Sintoma4 and Sintoma3 != Sintoma4 and Sintoma4.isdigit():
                                                        sqlInserir = f'''
                                                            UPDATE "Doenças"
                                                            SET "Nome" = '{nomeD}', "Sintomas1" = '{Sintoma1}', "Sintomas2" = '{Sintoma2}', "Sintomas3" = '{Sintoma3}', "Sintomas4" = '{Sintoma4}'
                                                            WHERE "ID" = '{DoençaEscolhido}'
                                                            '''
                                                case "N":
                                                    sqlInserir = f'''
                                                        UPDATE "Doenças"
                                                        SET "Nome" = '{nomeD}', "Sintomas1" = '{Sintoma1}', "Sintomas2" = '{Sintoma2}', "Sintomas3" = '{Sintoma3}'
                                                        WHERE "ID" = '{DoençaEscolhido}'
                                                        '''
                                                case _:
                                                    print("Você digitou um comando inválido. Voltando ao menu.")
                                    case "N":
                                        sqlInserir = f'''
                                            UPDATE "Doenças"
                                            SET "Nome" = '{nomeD}', "Sintomas1" = '{Sintoma1}', "Sintomas2" = '{Sintoma2}'
                                            WHERE "ID" = '{DoençaEscolhido}'
                                            '''
                                    case _:
                                        print("Você digitou um comando inválido. Voltando ao menu.")

                        case "N":
                            sqlInserir = f'''
                                UPDATE "Doenças"
                                SET "Nome" = '{nomeD}', "Sintomas1" = '{Sintoma1}'
                                WHERE "ID" = '{DoençaEscolhido}'
                                '''
                        case _:
                            print("Você digitou um comando inválido. Voltando ao menu.")
                                                
                    if conexaoBanco.manipularBanco(sqlInserir):
                        return "Doença atualizada com sucesso."
                    else:
                        return "Falha ao atualizar Doença!"
            case "N":
                print("Ok voltando ao menu principal")
            case _:
                print("Você digitou um comando inválido. Voltando ao menu.")
    else:
        return "Escolha uma opção válida."

def verDoençaEspecifico(idAtendimento):

    listaAtendimentos = conexaoBanco.consultarBanco(f'''
    SELECT * FROM "Atendimentos"
    WHERE "Doença" = '{idAtendimento}'
    ''')

    if listaAtendimentos:
        print("{:^9} | {:^15} ".format("ID" , "Paciente"))
        for Atendimento in listaAtendimentos:
            
            Time1daAtendimento = conexaoBanco.consultarBanco(f'''
                SELECT * FROM "Pacientes"
                WHERE "ID" = '{Atendimento[1]}'
                ''')[0]
            
            print("{:^9} | {:^15} ".format((Atendimento[0]), (Time1daAtendimento[1])))


    else:
        return "O Atendimentos não foram encontradas!"

def removerDoença():
    print("Tela de remoção de Doença:")
    print("Lista de Doenças")
    
    verListaDeDoenças()
    DoençaEscolhido = input("Digite o id do Doença escolhida:")

    if DoençaEscolhido.isdigit() and not DoençaEscolhido == None:
        verDoençaEspecifico(DoençaEscolhido)
    
        confirmar = input("Deseja remover esta Doença? (S/N)").upper()

        match confirmar:
            case "S":
                resultadoRemocao = conexaoBanco.manipularBanco(f'''
                DELETE FROM "Doenças"
                WHERE "ID" = '{DoençaEscolhido}'
                ''')
           
                if resultadoRemocao:
                    print("Doença removida com sucesso.")
                else:
                    print("Doença não existe ou não foi removido.")

            case "N":
                print("Ok voltando ao menu principal")
            case _:
                print("Você digitou um comando inválido. Voltando ao menu.")
                
    else:
        return "Escolha uma opção válida."

# #----------------------------------------------------------------------------------------------------------------------#

def verMenuAtendimento():

    while True:
        print('''
        Opções menu Atendimento:
        1. Ver Atendimento
        2. Atualizar Atendimento
        3. remover Atendimento
        4. Quero Atendimento
        5. Ver meus Atendimentos
        0. Voltar ao menu principal
        ''')
        op = input("Escolha uma das opções:")
        match op:
            case "1":
                verListaDeAtendimento()
            case "2":
                atualizarAtendimento()
            case "3":
                removerAtendimento()
            case "4":
                queroAtendimento()
            case "5":
                verMeusAtendimento()
            case "0":
                print("Voltando ao menu principal...")
                break
            case _:
                print("Escolha uma opção válida.")

        input("Digite Enter para continuar...")

def verListaDeAtendimento():

    listaAtendimentos = conexaoBanco.consultarBanco('''
    SELECT * FROM "Atendimento"
    ORDER BY "ID" DESC
    ''')

    if listaAtendimentos:
        print("ID  |   Paciente  |    Sintomas    |    Doença")
        for Atendimento in listaAtendimentos:
            
            ListadaPacientes = conexaoBanco.consultarBanco(f'''
                SELECT * FROM "Pacientes"
                WHERE "ID" = '{Atendimento[1]}'
                ''')[0]

            ListadaDoenças = conexaoBanco.consultarBanco(f'''
                SELECT * FROM "Doenças"
                WHERE "ID" = '{Atendimento[10]}'
                ''')[0]

            ListadaSintomas1 = conexaoBanco.consultarBanco(f'''
                SELECT * FROM "Sintomas"
                WHERE "ID" = '{Atendimento[2]}'
                ''')[0]
            
            if Atendimento[4] == None:
                print(f"{Atendimento[0]}, {ListadaPacientes[1]}, {ListadaSintomas1[1]}, {ListadaDoenças[1]}")

            if Atendimento[6] == None:
                ListadaSintomas2 = conexaoBanco.consultarBanco(f'''
                    SELECT * FROM "Sintomas"
                    WHERE "ID" = '{Atendimento[4]}'
                    ''')[0]
                print(f"{Atendimento[0]}, {ListadaPacientes[1]}, {ListadaSintomas1[1]}, {ListadaSintomas2[1]}, {ListadaDoenças[1]}")

            if Atendimento[8] == None:
                ListadaSintomas2 = conexaoBanco.consultarBanco(f'''
                    SELECT * FROM "Sintomas"
                    WHERE "ID" = '{Atendimento[4]}'
                    ''')[0]
                ListadaSintomas3 = conexaoBanco.consultarBanco(f'''
                    SELECT * FROM "Sintomas"
                    WHERE "ID" = '{Atendimento[6]}'
                    ''')[0]
                print(f"{Atendimento[0]}, {ListadaPacientes[1]}, {ListadaSintomas1[1]},  {ListadaSintomas2[1]},  {ListadaSintomas3[1]}, {ListadaDoenças[1]}")
                
            else:
                ListadaSintomas2 = conexaoBanco.consultarBanco(f'''
                    SELECT * FROM "Sintomas"
                    WHERE "ID" = '{Atendimento[4]}'
                    ''')[0]
                ListadaSintomas3 = conexaoBanco.consultarBanco(f'''
                    SELECT * FROM "Sintomas"
                    WHERE "ID" = '{Atendimento[6]}'
                    ''')[0]
                ListadaSintomas4 = conexaoBanco.consultarBanco(f'''
                    SELECT * FROM "Sintomas"
                    WHERE "ID" = '{Atendimento[8]}'
                    ''')[0]
                print(f"{Atendimento[0]}, {ListadaPacientes[1]}, {ListadaSintomas1[1]},  {ListadaSintomas2[1]},  {ListadaSintomas3[1]},  {ListadaSintomas4[1]}, {ListadaDoenças[1]}")
   
    else:
        print("Ocorreu um erro na consulta, ou a lista é vazia.")

def atualizarAtendimento():

    print("Tela de atualizar de Atendimento:")
    print("Lista de Atendimentos")

    verListaDeAtendimento()
    AtendimentoEscolhido = input("Digite o id do Atendimento escolhida:")

    if AtendimentoEscolhido.isdigit() and not AtendimentoEscolhido == None:

        confirmar = input("Deseja realmente atualizar essa doença? (S/N)").upper()

        match confirmar:
            case "S":

                listaSintomas = conexaoBanco.consultarBanco('''
                SELECT * FROM "Sintomas"
                ORDER BY "ID" ASC
                ''')

                if listaSintomas:
                    print("Esses são os sintomas cadastrados no sistema:")
                    print("ID | NOME")
                    for Sintoma in listaSintomas:
                        print(f"{Sintoma[0]} | {Sintoma[1]}")

                Sintoma1 = input("Digite o id do primeiro Sintoma deseja atualizar:")
                if Sintoma1.isdigit():

                    confirmar = input("Deseja adicionar ou atualizar um segundo Sintoma? (S/N)").upper()

                    match confirmar:
                        case "S":
                            Sintoma2 = input(f"Digite o id do segundo Sintoma:")
                            if Sintoma1 != Sintoma2 and Sintoma2.isdigit():

                                confirmar = input("Deseja adicionar ou atualizar um terceiro Sintoma? (S/N)").upper()

                                match confirmar:
                                    case "S":
                                        Sintoma3 = input(f"Digite o id do terceiro Sintoma:")
                                        if Sintoma1 != Sintoma3 and Sintoma2 != Sintoma3 and Sintoma3.isdigit():

                                            confirmar = input("Deseja adicionar ou atualizar um quarto Sintoma? (S/N)").upper()

                                            match confirmar:
                                                case "S":
                                                    Sintoma4 = input(f"Digite o id do quarto Sintoma:")
                                                    if Sintoma1 != Sintoma4 and Sintoma2 != Sintoma4 and Sintoma3 != Sintoma4 and Sintoma4.isdigit():
                                                        sqlInserir = f'''
                                                            UPDATE "Atendimentos"
                                                            SET "Sintomas1" = '{Sintoma1}', "Sintomas2" = '{Sintoma2}', "Sintomas3" = '{Sintoma3}', "Sintomas4" = '{Sintoma4}'
                                                            WHERE "ID" = '{AtendimentoEscolhido}'
                                                            '''
                                                case "N":
                                                    sqlInserir = f'''
                                                        UPDATE "Atendimentos"
                                                        SET "Sintomas1" = '{Sintoma1}', "Sintomas2" = '{Sintoma2}', "Sintomas3" = '{Sintoma3}'
                                                        WHERE "ID" = '{AtendimentoEscolhido}'
                                                        '''
                                                case _:
                                                    print("Você digitou um comando inválido. Voltando ao menu.")
                                    case "N":
                                        sqlInserir = f'''
                                            UPDATE "Atendimentos"
                                            SET "Sintomas1" = '{Sintoma1}', "Sintomas2" = '{Sintoma2}'
                                            WHERE "ID" = '{AtendimentoEscolhido}'
                                            '''
                                    case _:
                                        print("Você digitou um comando inválido. Voltando ao menu.")

                        case "N":
                            sqlInserir = f'''
                                UPDATE "Atendimentos"
                                SET "Sintomas1" = '{Sintoma1}'
                                WHERE "ID" = '{AtendimentoEscolhido}'
                                '''
                        case _:
                            print("Você digitou um comando inválido. Voltando ao menu.")
                                                
                    if conexaoBanco.manipularBanco(sqlInserir):
                        return "Atendimento atualizada com sucesso."
                    else:
                        return "Falha ao atualizar Atendimento!"
            case "N":
                print("Ok voltando ao menu principal")
            case _:
                print("Você digitou um comando inválido. Voltando ao menu.")

    else:
        return "Escolha uma opção válida."

def removerAtendimento():

    print("Tela de remoção de Atendimento:")
    print("Lista de Atendimentos")
    
    verListaDeAtendimento()
    AtendimentoEscolhido = input("Digite o id do Atendimento escolhida:")

    if AtendimentoEscolhido.isdigit() and not AtendimentoEscolhido == None:
    
        confirmar = input("Deseja remover esta Atendimento? (S/N)").upper()

        match confirmar:
            case "S":
                resultadoRemocao = conexaoBanco.manipularBanco(f'''
                DELETE FROM "Atendimentos"
                WHERE "ID" = '{AtendimentoEscolhido}'
                ''')
           
                if resultadoRemocao:
                    print("Atendimento removida com sucesso.")
                else:
                    print("Atendimento não existe ou não foi removido.")

            case "N":
                print("Ok voltando ao menu principal")
            case _:
                print("Você digitou um comando inválido. Voltando ao menu.")

    else:
        return "Escolha uma opção válida."

def queroAtendimento():

def verMeusAtendimento():
    id = menuLogin.loginl[0]

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