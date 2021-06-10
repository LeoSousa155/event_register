from  register_funcs import *


def main():
      print('-' * 32)
      print('       Registo de eventos')
      events = list()
      while True:
            info()
            entrace = input("Escolha uma opção: ")
            print("-" * 32)
            if entrace in ["1", "2", "3", "0"]:
                  if entrace == "1":
                        event = event_register()
                        events.append(event)
                  if entrace == "2":
                        show_events(events)
                  if entrace == "3":
                        edit_event(events)
                  if entrace == "0":
                        export_events(events)
                        print("Programa concluido com sucesso.")
                        break
            else:
                  print("Escolha uma opção válida.")


if __name__ == "__main__":
      main()
