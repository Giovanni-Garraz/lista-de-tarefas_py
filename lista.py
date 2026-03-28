tarefas = []
ARQUIVO = "tarefas.txt"

def adicionar_tarefa():
    tarefa = input("Insira a tarefa: ")
    tarefas.append({"nome": tarefa, "concluida": False})
    salvar_tarefas()

def listar_tarefas():
    if not tarefas:
        print("\nSem tarefa.\n")
        return

    for i, t in enumerate(tarefas):
        status = "V" if t["concluida"] else "X"
        print(f"{i} - {t['nome']} {status}")

    print("------------------\n")

def concluir_tarefas():
    listar_tarefas()
    try:
        i = int(input("Coloca o número da tarefa: "))
        tarefas[i]["concluida"] = True
        salvar_tarefas()
    except:
       print("Erro!")

def remover_tarefa():
    listar_tarefas()

    try:
        i = int(input("Coloca o número da tarefa para remover: "))
        tarefa_removida = tarefas.pop(i)
        salvar_tarefas()
        print(f"\nRemovida: {tarefa_removida['nome']}\n")
    except:
        print("Erro ao remover tarefa!\n")

def editar_tarefa():
    listar_tarefas()

    try:
        i = int(input("Coloca o número da tarefa para editar: "))
        novo_nome = input("Insira o novo nome: ")

        tarefas[i]["nome"] = novo_nome

        print("\nTarefa atualizada!\n")

    except:
        print("Erro ao editar tarefa!\n")

def carregar_tarefas():
    try:
        with open(ARQUIVO, "r") as f:
            for linha in f:
                partes = linha.strip().split("|")

            if len(partes) >= 2 and partes[0] != "":
                tarefas.append({
                    "nome": partes[0],
                    "concluida": bool(int(partes[1])),
                })
    except FileNotFoundError:
        pass

def salvar_tarefas():
    with open(ARQUIVO, "w") as f:
        for t in tarefas:
            linha = f"{t['nome']}|{int(t['concluida'])}\n"
            f.write(linha)

def buscar_tarefa():
    termo = input("Insira a tarefa: ").lower()

    print("\n----- RESULTADO -----")

    encontrou = False

    for i, t in enumerate(tarefas):
        if termo in t['nome'].lower():
            status = "V" if t["concluida"] else "X"
            print(f"{i} - {t['nome']} {status}")
            encontrou = True

    if not encontrou:
        print("Nenhuma tarefa encontrada.")

    print("-------------------\n")

def alterar_tarefa():
    listar_tarefas()

    try:
        i = int(input("Insira o número da tarefa: "))

        tarefas[i]["concluida"] = not tarefas[i]["concluida"]

        salvar_tarefas()

        print("\nTarefa alterada!\n")
    except:
        print("Erro ao alterar tarefa!\n")



def menu():
    carregar_tarefas()
    while True:

        print("1 - Adicionar tarefa")
        print("2 - Listar tarefa")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Editar tarefa")
        print("6 - Buscar tarefa")
        print("7 - Alterar tarefa")
        print("0 - Sair")
        print("===============")

        op = input("Escolha: ")

        if op == "1":
            adicionar_tarefa()
        elif op == "2":
            listar_tarefas()
        elif op == "3":
            concluir_tarefas()
        elif op == "4":
            remover_tarefa()
        elif op == "5":
            editar_tarefa()
        elif op == "6":
            buscar_tarefa()
        elif op == "7":
            alterar_tarefa()
        elif op == "0":
            break
        else:
           print("Erro!")

menu()


