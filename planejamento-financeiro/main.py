from rich.console import Console


console = Console()

entradas = []
gastos_permanentes = []
sobraSalario = 0   
porcentagemGuardar = 0.25

nome = input("qual seu nome? ")
sobraSalario = float(input("qual seu salário? "))
print("-----------------------------------------")
print("\n")

print(f"olá {nome} bem vindo(a)\n")
print("\n")

def menu():
    while True:
        print("---------------------------------")
        print("---sistema financeiro pessoal----")
        print("---------------------------------")
        console.print("1.[bold green] acrescentar entradas [/bold green]")
        console.print("2.[bold red] acrescentar saidas  [/bold red]")
        console.print("3.[bold yellow] metas e investimentos [/bold yellow]")  
        console.print("4.[bold cyan] sair [/bold cyan]")

        try:
            opcao = int(input("escolha uma opção (1-4): "))
        except:
            console.print("[bold red]por favor, digite um número válido[/bold red]")
            continue

        if opcao == 1:
            acrescentar_entradas()
        elif opcao == 2:
            acrescentar_saidas()
        elif opcao == 3:
            juntar_dinheiro()
        elif opcao == 4:
            print("\nsaindo....\n")
            print("------------------------------------")
            break
        else:
            console.print("[bold red]opção inválida, tente novamente[/bold red]")


def acrescentar_entradas():
    print("\nvoce escolheu: acrescentar entradas")
    print("------------------------------------")

    try:
        quantidade = int(input("qual foi a quantidade de entradas que voce teve no mês? (ex: 3) "))
    except:
        console.print("[bold red]valor inválido, tente de novo[/bold red]")
        return

    print("-------------------------------------------------------------------------------")

    for c in range(quantidade):
        try:
            valorEntradas = float(input(f"digite o valor da {c+1} entrada:\n R$ "))
        except:
            console.print("[bold red]valor inválido, pulando essa entrada[/bold red]")
            continue
        entradas.append(valorEntradas)

    print("--------------------------------------------------------------------")
    Total = sum(entradas)
    print(entradas)
    print("\n")
    console.print(f"a soma dos seus ganhos nesse mês é de: [bold green]{Total:.2f} [/bold green]\n")
    print("\n")


def acrescentar_saidas():
    global sobraSalario
    print("\n voce escolheu acrescentar saidas")
    print("------------------------------------")

    try:
        qntd = int(input("\nquantos gastos permanentes você tem no mês? (ex: 5) "))
    except:
        console.print("[bold red]valor inválido, tente de novo[/bold red]")
        return

    print("------------------------------------------------------------------")

    for i in range(qntd):
        try:
            valor = float(input(f"digite o valor do {i+1} gasto permanente:\n R$ "))
        except:
            console.print("[bold red]valor inválido, pulando esse gasto[/bold red]")
            continue
        gastos_permanentes.append(valor)

    print("--------------------------------------------------------------------")
    soma = sum(gastos_permanentes)
    console.print(f"a soma das suas dividas nesse mês é de: [bold red]{soma:.2f} [/bold red]\n")
    print(gastos_permanentes)
    print("\n")

    escolha = input("voce deseja ver quanto vai sobrar do seu salário? (s/n) ").lower()
    if escolha == "s":
        print("-------------------------")
        print("calculo com base salarial")
        print("-------------------------")
        try:
          
            qntdSobra = sobraSalario - soma
            console.print(f"o que vai restar do seu salário é R$ [bold green]{qntdSobra:.2f} [/bold green]\n")
        except:
            console.print("[bold red]valor inválido para salário[/bold red]")


def juntar_dinheiro():
    global sobraSalario, porcentagemGuardar
    resposta = input("voce possui alguma meta em especifíco pra juntar? (s/n) ").lower()

    if resposta == 's':
        try:
            meta = float(input("qual valor? R$\n"))
            meses = int(input("em até quantos meses você deseja juntar? "))
            if meses <= 0:
                console.print("[bold red]número de meses inválido[/bold red]")
                return
        except:
            console.print("[bold red]valor inválido, tente de novo[/bold red]")
            return

        print("\n-----------------------------------------------------------------------")
        valorMensal = meta / meses
        limite = sobraSalario * porcentagemGuardar  # 25% da sobra do salário

        if sobraSalario <= 0:
            console.print("[bold red]não há sobra no salário para juntar dinheiro[/bold red]")
        elif valorMensal > limite:
            
            console.print(f"[bold red]não é possível[/bold red] juntar R$ {valorMensal:.2f} por mês, ")
            console.print(f"porque ultrapassa 25% da sua sobra salarial (limite: R$ {limite:.2f})" )
            
        else:
            console.print(f"para atingir a sua meta você precisa guardar R$ [bold yellow]{valorMensal:.2f} [/bold yellow] ")
            console.print(f"por mês, o que está dentro do limite de 25% da sua sobra salarial.\n")
            

    else:
        if sobraSalario > 0:
            recomendacao = sobraSalario * porcentagemGuardar
            
            print(f"\njá que você não tem uma meta em específico, é recomendado que invista {int(porcentagemGuardar*100)}% ")
            print(f"do que sobra do seu salário todos os meses. Isso daria R$ {recomendacao:.2f} por mês.\n")
        else:
            console.print("[bold red]como não há sobra no salário, não é possível investir[/bold red]\n")



menu()
