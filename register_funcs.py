# opções do programa e seleção
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
          '\n3 --> Editar um evento')
    print('-' * 32)


#fazer tratamento de erros
def event_register():  #Cria uma instancia da classe "Evento"
    print("OK, vamos registar um evento")
    name = str(input("Nome do evento: ")).upper().replace(" ", "")
    year = int(input("Ano: "))
    month = int(input("Mês: "))
    day = int(input("Dia: "))
    date = datetime.datetime(year, month, day)
    budget = float(input("Orçamento: "))
    print(f"Evento '{name}' registado com sucesso.")
    return Evento(name, date, budget)


#Função concluida
def show_events(list): #mostra todos os eventos registados
    print("Mostrando todos os eventos")
    print("[indice]Nome: Ano, Mês, Dia, Orçamento(€)")
    print("")
    if len(list) == 0:
        print("Não existem elementos registados")
    else:
        for index, element in enumerate(list):
            print(f"[{index}]{element.name}: {element.date}, {element.budget:.2f}")


#função por implementar
def edit_event(list): #edit 1 event registered
    print("ok")


#função por implementar
def export_events(list):
    print("tentando exportar")
