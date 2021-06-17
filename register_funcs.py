# opções do programa e seleção
import xlsxwriter
import datetime
#classe que produz os eventos a serem guardados
class Evento:
    def __init__(self, name, date, budget):
        self.name = name
        self.date = date
        self.budget = budget


#função concluida
def info(): #Mostra as ações que o usuário pode fazer
    print('-' * 32)
    print('Opções:'
          '\n0 --> Sair do programa'
          '\n1 --> Registar um evento'
          '\n2 --> Mostrar dados dos evento'
          '\n3 --> Editar um evento'
          '\n4 --> Exportar eventos em Excel')
    print('-' * 32)


def decision(answer):
    while True:
        if answer in ["0", "1"]:
            if answer == "0":
                return False
            if answer == "1":
                return True
        else:
            print("Escolha uma opção válida.")


#fazer tratamento de erros
def event_register():  #Cria uma instancia da classe "Evento"
    print("OK, vamos registar um evento")
    name = str(input("Nome do evento: ")).upper().replace(" ", "")
    year = int(input("Ano: "))
    month = int(input("Mês: "))
    day = int(input("Dia: "))
    budget = float(input("Orçamento: "))
    date = datetime.date(year, month, day)
    print(f"Evento '{name}' registado com sucesso.")
    return Evento(name, date, budget)


#Função concluida
def show_events(regist): #mostra todos os eventos registados
    print("Mostrando todos os eventos")
    print("[indice]Nome: Ano, Mês, Dia, Orçamento(€)")
    print("")
    if len(regist) == 0:
        print("Não existem elementos registados")
    else:
        for index, element in enumerate(regist):
            print(f"[{index}]{element.name}: {element.date}, {element.budget:.2f}")


#fazer tratamento de erros
def edit_event(regist): #edit 1 event registered
    print("-" * 32)
    if len(regist) == 0:
        print("Não existem elementos para editar, porfavor registe um evento antes de executar esta função.")
        return

    show_events(regist)
    #tratar o input do usuario para que n de erro
    while True: #Seleção do indice do evento a ser editado
        index = int(input("Seleciona o evento que pretendes editar (indice): "))
        if index  not in range(len(regist)):
            print("Porfavor selecione um indice válido")
        else:
            break

    #Tratamento de erros dependente do tratamento do "Event Register"
    #Seleção do evento a ser editado
    print(f"'{regist[index].name}' é o evento que pretende editar?"
          f"\n0 --> Não"
          f"\n1 --> Sim")
    edit = input()
    if decision(edit):
        regist[index] = event_register()
        print("Evento editado com sucesso")
    else: #Editar (Sobreescrever evento com "Event Register"
        print(f"Cancelando a edição do evento '{regist[index].name}'")



#função por implementar
def export_events(regist):
    print("Exportando...")
    excel = list()
    excel.append(["Nome", "Data", "Orçamento"])
    with xlsxwriter.Workbook('test.xlsx') as workbook:
        worksheet = workbook.add_worksheet()
        for event in regist:
            date = f"{event.date}"
            excel.append([event.name, date, event.budget])
        for index, event in enumerate(excel):
            worksheet.write_row(index, 0, event)
        print("Arquivo exportado com sucesso.")
