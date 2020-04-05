import os


ENVIROMENTS = os.environ

HOME = ENVIROMENTS['HOME']


aplications = '/Applications'

arquivos = os.listdir(aplications)

apps = [app for app in arquivos]

# ---- APP ----
while True:
    print()
    print('LISTAR E EXECUTAR APLICATIVOS INSTALADOS NO MAC.\n')
    head =  "[1] Listar Aplicativos.\n[2] Listar Diretorios.\n[3] Executar Aplicativo.\n[4] Sair."
    print(head)
    print()
    opcao = int(input('Option: '))
    print()
    if opcao == 1:
        applics = [a for a in apps if '.app' in a]
        for i in applics:
            a = i[:-4]
            print(a)
    elif opcao == 2:
        dirs = [a for a in apps if not '.app' in a]
        for d in dirs:
            print(d)
    elif opcao == 3:
        program = input('Nome do Programa: ').strip()

        try:
            os.system(f'open -a "{program}"')
        except Exception as e:
            print(e)
    elif opcao == 4:
        print('Saindo ...\nAté a proxima.')
        break