import time
import random
from rich.console import Console
from rich.align import Align

console = Console()

class Trplm:
    """Main Game Class"""
    
    def __init__(self):
        self.menu = Menu()
        self.settings_menu = SettingsMenu()
        self.game_loop()

    def game_loop(self) -> None:
        """Main game loop"""
        self.menu.display_menu()
        try:
            user_input = int(input("Enter: "))
        except ValueError:
            console.print("ERROR: ENTER VALID NUMBER", style="bold red")
            user_input = 0

        while user_input != 3:
            if user_input == 1:
                self.play_game()
            elif user_input == 2:
                self.settings_menu.display_menu()
            
            self.menu.display_menu()
            try:
                user_input = int(input("Enter: "))
            except ValueError:
                console.print("ERROR: ENTER VALID NUMBER", style="bold red")
                user_input = 0

        console.print("Till next time!", style="bold red")
        time.sleep(0.6)
        console.clear()

    def play_game(self):
        """Play the game"""
        console.clear()
        console.print("[bold red]MENTAL MATH MASTER[/bold red]")

        # Let the user choose between manual or random mode
        while True:
            console.print("(1) Choose Starting Range\n(2) Random Questions")
            mode = input("Enter: ").strip()
            if mode in {"1", "2"}:
                break
            console.print("Enter 1 or 2", style="bold red")
            console.clear()

        questions = []
        if mode == "1":
            while True:
                try:
                    start_num = int(input("Starting Range: ").strip())
                    if 2 <= start_num <= 20:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    console.print("Enter A Valid Number (Between 2 and 20).", style="bold red")

            num_range = range(start_num, 21)
            questions = [(a, b) for a in num_range for b in range(2, 21)]

        else:  # Random mode
            questions = [(a, b) for a in range(2, 21) for b in range(2, 21)]
            random.shuffle(questions)

        operation = "x"
        start_time = time.time()

        for a, b in questions:
            answer = a * b
            attempts = 0  

            while True:  
                console.clear()
                console.print("[bold red]MENTAL MATH MASTER[/bold red]")
                question_text = f"[bold red]{a} {operation} {b}[/bold red]"
                console.print(Align.left(question_text))

                user_answer = input().strip()

                if user_answer.lower() == "exit":
                    elapsed_time = round(time.time() - start_time)
                    minutes, seconds = divmod(elapsed_time, 60)
                    console.print(f"Time played: [bold green]{minutes}m {seconds}s[/bold green]")
                    input("Press Enter To Return")
                    return

                if user_answer.isdigit() and int(user_answer) == answer:
                    break  

                attempts += 1
                if attempts == 2:
                    console.print(f"[red]{answer}[/red]")
                    time.sleep(0.8)
                    break  

        elapsed_time = round(time.time() - start_time)
        minutes, seconds = divmod(elapsed_time, 60)
        console.print(f"\n[bold red]Total time played:[/bold red] [bold green]{minutes}m {seconds}s[/bold green]")
        input("Press Enter To Return")

class Menu:
    """Main Menu"""
    
    def __init__(self):
        self.title = "MENTAL MATH MASTER"
        self.menu = "(1) PLAY\n(2) SETTINGS\n(3) EXIT"
    
    def display_menu(self) -> None:
        """Display the main menu"""
        console.clear()
        console.print(f"[bold red]{self.title}[/bold red]\n{self.menu}")

class SettingsMenu:
    """Settings Menu"""
    
    def __init__(self):
        self.menu = "(1) OPERATIONS\n(2) TIMER\n(3) QUESTION COUNT/TYPE\n(4) MAIN MENU"

    def display_menu(self) -> None:
        console.clear()
        console.print(f"[bold red]MENTAL MATH MASTER (SETTINGS)[/bold red]\n{self.menu}")
        
        choice = input("Enter: ")
        if choice == "4":
            return
        elif choice == "1":
            console.print("[bold red]Operations Settings Not Implemented Yet[/bold red]\n[bold red]Press Enter to continue...[/bold red]", style="italic")
            input("")
        elif choice == "2":
            console.print("[bold red]Timer Settings Not Implemented Yet[/bold red]\n[bold red]Press Enter to continue...[/bold red]", style="italic")
            input("")
        elif choice == "3":
            console.print("[bold red]Question Count/Type Settings Not Implemented Yet[/bold red]\n[bold red]Press Enter to continue...[/bold red]", style="italic")
            input("")

if __name__ == "__main__":
    try:
        Trplm()
    except KeyboardInterrupt:
        console.clear()
        console.print("Till Next Time.", style="red")
