from secundary_functions import *
import xlsxwriter
import datetime

# opções do programa e seleção

#classe que produz os eventos a serem guardados
class Evento:
    def __init__(self, name, date, budget):
        self.name = name
        self.date = date
        self.budget = budget


def info(): #Mostra as ações que o usuário pode fazer
    print('-' * 32)
    print('Opções:'
          '\n0 --> Sair do programa'
          '\n1 --> Registar um evento'
          '\n2 --> Mostrar dados dos evento'
          '\n3 --> Editar um evento'
          '\n4 --> Exportar eventos em Excel')
    print('-' * 32)

#fazer tratamento de erros
def event_register():  #Cria uma instancia da classe "Evento"
    print("OK, vamos registar um evento")
    while True:
        name = input("Nome do evento: ")
        if len(name) != 0:
            break
        else:
            print("Porfavor não deixe o nome vazio.")

    year = numeric_input("Ano: ",1,  9999)
    month = numeric_input("Mês: ",1,  12)
    if month in (4, 6, 9, 11):
        max_day = 30
    elif month in (1, 3, 5, 7, 8, 12):
        max_day = 31
    elif month == 2 and (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:
        max_day = 29
    else:
        max_day = 28

    day = numeric_input("Dia: ",1,  max_day)
    budget = numeric_input("Orçamento: ")

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


def edit_event(regist): #edita um evento registado
    print("-" * 32)
    if len(regist) == 0:
        print("Não existem elementos para editar, porfavor registe um evento antes de executar esta função.")
        return

    show_events(regist)
    #Seleção do evento a ser editado
    index = numeric_input("Seleciona o evento que pretendes editar (indice): ", 0, len(regist) - 1)
    print(f"'{regist[index].name}' é o evento que pretende editar?"
          f"\n0 --> Não"
          f"\n1 --> Sim")
    edit = input()
    if decision(edit):
        regist[index] = event_register()
        print("Evento editado com sucesso")
    else: #Editar (Sobreescrever evento com "Event Register"
        print(f"Cancelando a edição do evento '{regist[index].name}'")


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
