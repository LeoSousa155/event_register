def decision(answer):
    while True:
        if answer in ["0", "1"]:
            if answer == "0":
                return False
            if answer == "1":
                return True
        else:
            print("Escolha uma opção válida.")


def numeric_input(message, min_value = 1, max_value = 1 * 10 **20):
    while True:
        data = input(f"{message}")
        if len(data) == 0:
            print("Porfavor não deixe o nome vazio.")
        try:
            data = int(data)
        except:
            print("Porfavor introduza um valor númerico.")
        else:
            if data not in range(min_value, max_value + 1):
                print(f"Porfavor adicione um ano entre {min_value} e {max_value}")
            else:
                return data
