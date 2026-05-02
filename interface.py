import subprocess
from rich.console import Console

console = Console()

banner = r"""
 _______                   __                         
|       \                 |  \                        
| $$$$$$$\  ______    ____| $$ __    __  __    __      
| $$__| $$ /      \  /      $$|  \  |  \|  \  /  \      
| $$    $$|  $$$$$$\|  $$$$$$$| $$  | $$ \$$\/  $$      
| $$$$$$$\| $$  | $$| $$  | $$| $$  | $$  >$$  $$      
| $$  | $$| $$__/ $$| $$__| $$| $$__/ $$ /  $$$$\      
| $$  | $$ \$$    $$ \$$    $$ \$$    $$|  $$ \$$\     
 \$$   \$$  \$$$$$$   \$$$$$$$  \$$$$$$  \$$   \$$     
"""


def mostrar_menu():
    console.print(f"[green]{banner}[/green]")
    print("\n1. Start Monitoring")
    print("2. Stop Monitoring")
    print("3. Logs")
    print("4. System Status")
    print("5. Exit")


def gerenciar_servico(acao):
    try:
        subprocess.run(["sudo", "systemctl", acao, "rodux"], check=True)
        console.print(f"[bold green]Success: Rodux {acao} with success![/bold green]")
    except:
        console.print(
            "[bold red]Error accessing systemctl. Is the service installed?[/bold red]"
        )


def ver_logs():
    console.print("[yellow]Press Ctrl+C to exit logs[/yellow]\n")
    try:
        subprocess.run(["tail", "-f", "/var/log/rodux.log"])
    except KeyboardInterrupt:
        pass


while True:
    mostrar_menu()
    opcao = input("\nChoose an option: ")

    if opcao == "1":
        gerenciar_servico("start")
    elif opcao == "2":
        gerenciar_servico("stop")
    elif opcao == "3":
        ver_logs()
    elif opcao == "4":
        gerenciar_servico("status")
    elif opcao == "5":
        console.print("[green] Leaving... [/green]")
        break
    else:
        console.print("[red]Invalid option![/red]")
