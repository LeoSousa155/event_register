# opções do programa e seleção
import datetime


class Event:
    def __init__(self, name, date, budget):
        self.name = name
        self.date = date
        self.budget = budget


def info(): #Prints the options the user have
    print('-' * 32)
    print('Opções:'
          '\n0 --> Sair do programa'
          '\n1 --> Registar um evento'
          '\n2 --> Mostrar dados dos evento'
          '\n3 --> Comparar 2 eventos'
          '\n4 --> Editar um evento')
    print('-' * 32)


def event_register():  #Creates an instance of the class "Event"
    print("OK, vamos registar um evento")
    name = str(input("Nome do evento: ")).upper().replace(" ", "")
    year = int(input("Ano: "))
    month = int(input("Mês: "))
    day = int(input("Dia: "))
    date = datetime.datetime(year, month, day)
    budget = float(input("Orçamento: "))
    print(f"Evento '{name}' registado com sucesso.")
    return Event(name, date, budget)


def show_events(list): #show all the events registered
    print("Mostrando todos os eventos")
    print("[indice]Nome: Ano, Mês, Dia, Orçamento(€)")
    print("")
    if len(list) == 0:
        print("Não existem elementos registados")
    else:
        for index, element in enumerate(list):
            print(f"[{index}]{element.name}: {element.date}, {element.budget:.2f}")


def compare_events(): #compare 2 events registered
    print("3 ok")


def edit_event(list): #edit 1 event registered
    element_index = int(input("Indice do evento que pretende editar: "))
    event = list[element_index]
    print(event.name)
