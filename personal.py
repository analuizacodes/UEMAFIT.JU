
class PersonalTrainer:
    def __init__(self):
        self.alunos = []

    # Cadastrar aluno
    def cadastrar_aluno(self):
        print("\n===== CADASTRO DE ALUNO =====")

        nome = input("Nome do aluno: ")
        idade = input("Idade do aluno: ")

        if not idade.isdigit():
            print("Digite uma idade válida!")
            return

        idade = int(idade)

        if idade < 13:
            print("Cadastro não permitido! A academia aceita alunos a partir de 13 anos.")
            return

        novo_aluno = {
            "Nome": nome,
            "Idade": idade,
            "Meta": "",
            "Dias": 0,
            "Horas": 0,
            "Lesao": ""
        }

        self.alunos.append(novo_aluno)
        print("Cadastro realizado com sucesso!")

    # Listar alunos
    def listar_alunos(self):
        print("\n===== ALUNOS CADASTRADOS =====")

        if len(self.alunos) == 0:
            print("Não existem alunos cadastrados.")
            return

        for posicao, aluno in enumerate(self.alunos):
            idade = aluno["Idade"]

            if idade <= 17:
                tipo = "Adolescente"
            elif idade < 60:
                tipo = "Adulto"
            else:
                tipo = "Idoso"

            print(f"{posicao} - {aluno['Nome']} | {tipo}")

    # Atualizar dados
    def atualizar_aluno(self):
        self.listar_alunos()

        if not self.alunos:
            return

        escolha = input("Informe o índice do aluno: ")

        if not escolha.isdigit():
            print("Índice inválido!")
            return

        escolha = int(escolha)

        if escolha < 0 or escolha >= len(self.alunos):
            print("Aluno não encontrado!")
            return

        nova_idade = input("Informe a nova idade: ")

        if not nova_idade.isdigit():
            print("Idade inválida!")
            return

        nova_idade = int(nova_idade)

        if nova_idade < 13:
            print("Não é permitido cadastrar alunos menores de 13 anos!")
            return

        self.alunos[escolha]["Idade"] = nova_idade
        print("Informações atualizadas!")

    # Excluir aluno
    def remover_aluno(self):
        self.listar_alunos()

        if not self.alunos:
            return

        escolha = input("Qual índice deseja remover? ")

        if not escolha.isdigit():
            print("Digite um índice válido!")
            return

        escolha = int(escolha)

        if 0 <= escolha < len(self.alunos):
            aluno = self.alunos.pop(escolha)
            print(f"{aluno['Nome']} foi removido do sistema.")
        else:
            print("Aluno não encontrado!")

    # Realizar entrevista
    def entrevistar_aluno(self):
        self.listar_alunos()

        if not self.alunos:
            return

        escolha = input("Escolha o índice do aluno: ")

        if not escolha.isdigit():
            print("Opção inválida!")
            return

        escolha = int(escolha)

        if escolha < 0 or escolha >= len(self.alunos):
            print("Aluno não encontrado!")
            return

        aluno = self.alunos[escolha]

        if aluno["Idade"] < 13:
            print("Aluno não possui idade mínima para treinar.")
            return

        print("\n===== ENTREVISTA =====")
        print("1 - Emagrecer")
        print("2 - Ganhar massa muscular")
        print("3 - Melhorar condicionamento físico")

        opcao = input("Escolha sua meta: ")

        if not opcao.isdigit():
            print("Opção inválida!")
            return

        opcao = int(opcao)

        metas = {
            1: "Emagrecer",
            2: "Ganhar massa muscular",
            3: "Melhorar condicionamento físico"
        }

        if opcao not in metas:
            print("Meta inexistente!")
            return

        dias = input("Dias disponíveis por semana: ")

        if not dias.isdigit():
            print("Quantidade inválida!")
            return

        horas = input("Horas disponíveis por dia: ")

        if not horas.isdigit():
            print("Quantidade inválida!")
            return

        lesao = input("Possui lesão ou doença? (1-SIM / 2-NÃO): ")

        if not lesao.isdigit() or int(lesao) not in [1, 2]:
            print("Resposta inválida!")
            return

        aluno["Meta"] = metas[opcao]
        aluno["Dias"] = int(dias)
        aluno["Horas"] = int(horas)
        aluno["Lesao"] = int(lesao)

        print("Entrevista concluída!")

    # Criar ficha de treino
    def gerar_treino(self):
        self.listar_alunos()

        if not self.alunos:
            return

        escolha = input("Digite o índice do aluno: ")

        if not escolha.isdigit():
            print("Índice inválido!")
            return

        escolha = int(escolha)

        if escolha < 0 or escolha >= len(self.alunos):
            print("Aluno não encontrado!")
            return

        aluno = self.alunos[escolha]

        if aluno["Idade"] < 13:
            print("Não é permitido gerar treino para menores de 13 anos.")
            return

        if aluno["Meta"] == "":
            print("O aluno precisa realizar a entrevista primeiro!")
            return

        print("\n===== FICHA DE TREINO =====")
        print(f"Aluno: {aluno['Nome']}")
        print(f"Meta: {aluno['Meta']}")
        print(f"Dias por semana: {aluno['Dias']}")
        print(f"Horas por dia: {aluno['Horas']}")

        if aluno["Lesao"] == 1:
            print("\nAtenção! É necessária uma avaliação profissional.")
        else:
            idade = aluno["Idade"]

            if idade <= 17:
                print("\nCategoria: Adolescente")
                print("Treinamento adaptado e supervisionado.")
            elif idade < 60:
                print("\nCategoria: Adulto")
                print("Treinamento de força e condicionamento.")
            else:
                print("\nCategoria: Idoso")
                print("Treinamento adaptado à idade.")

            print("\nExercícios recomendados:")

            if aluno["Meta"] == "Emagrecer":
                exercicios = [
                    "Caminhada",
                    "Bicicleta ergométrica",
                    "Agachamento",
                    "Polichinelo adaptado",
                    "Fortalecimento muscular"
                ]

            elif aluno["Meta"] == "Ganhar massa muscular":
                exercicios = [
                    "Agachamento",
                    "Supino",
                    "Remada",
                    "Desenvolvimento de ombros",
                    "Fortalecimento muscular"
                ]

            else:
                exercicios = [
                    "Caminhada rápida",
                    "Bicicleta ergométrica",
                    "Corrida leve",
                    "Corda adaptada",
                    "Circuito de exercícios"
                ]

            for item in exercicios:
                print("- " + item)

        print("============================")

    # Menu principal
    def menu(self):
        while True:
            print("\n===== UEMAFIT =====")
            print("1 - Cadastrar aluno")
            print("2 - Listar alunos")
            print("3 - Atualizar aluno")
            print("4 - Remover aluno")
            print("5 - Fazer entrevista")
            print("6 - Gerar ficha de treino")
            print("7 - Sair")

            opcao = input("Escolha uma opção: ")

            if not opcao.isdigit():
                print("Digite uma opção numérica!")
                continue

            opcao = int(opcao)

            if opcao == 1:
                self.cadastrar_aluno()
            elif opcao == 2:
                self.listar_alunos()
            elif opcao == 3:
                self.atualizar_aluno()
            elif opcao == 4:
                self.remover_aluno()
            elif opcao == 5:
                self.entrevistar_aluno()
            elif opcao == 6:
                self.gerar_treino()
            elif opcao == 7:
                print("Sistema encerrado!")
                break
            else:
                print("Opção inexistente!")


# Iniciar o programa
sistema = PersonalTrainer()
sistema.menu()
