from  register_funcs import *


def main():
      events = list()
      exported = False

      print('-' * 32)
      print('       Registo de eventos')
      while True:
            info()
            entrace = input("Escolha uma opção: ")
            print("-" * 32)
            if entrace in ["1", "2", "3", "4", "0"]:
                  if entrace == "1":
                        event = event_register()
                        events.append(event)
                  if entrace == "2":
                        show_events(events)
                  if entrace == "3":
                        edit_event(events)
                  if entrace == "4":
                        export_events(events)
                        exported = True
                  if entrace == "0":
                        if exported == False:
                              print("Você não exportou os eventos que registou.")
                              print("Pretende exportar os dados em formato 'xlsx'?"
                                    f"\n0 --> Não"
                                    f"\n1 --> Sim")
                              edit = input()
                              if decision(edit):
                                    export_events(events)
                              else:
                                    print("Programa concluido com sucesso.")
                        break
            else:
                  print("Escolha uma opção válida.")


if __name__ == "__main__":
      main()
