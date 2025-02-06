import CLI

if __name__ == "__main__":
     model = CLI.ModelCLI()
     input_cli = CLI.InputCLI(model)
     switch_cli = CLI.SwitchCLI(model)
     exit_cli = CLI.ExitCLI(model)
     help_cli = CLI.HelpCLI()

     help_cli.execute()
     while True:
          command = input("Digite o comando: ")
          if command == "1":
               ia = input("Digite o modelo: ").strip().lower()
               try:
                    model.switch(ia)
               except ValueError as e:
                    print(e)
                    continue
               input_cli.execute()
          elif command == "2":
               ia = input("Digite o modelo: ").strip().lower()
               try:
                    model.switch(ia)
               except ValueError as e:
                    print(e)
          elif command == "3":
               exit_cli.execute()
          elif command == "4":
               help_cli.execute()
          else:
               print("Comando inválido!\n")