import time
from rich.panel import Panel
from rich.console import Console

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
        user_input = int(input("Enter: "))
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
        console.print(Panel("MENTAL MATH MONSTER", style="bold red"))

    def auto_answer(self, correct_answer):
        """Auto answer (not yet implemented)"""
        pass


class Menu:
    """Main Menu"""
    
    def __init__(self):
        self.title = "MENTAL MATH MONSTER"
        self.menu = "(1) PLAY\n(2) SETTINGS\n(3) EXIT"
    
    def display_menu(self) -> None:
        """Display the main menu"""
        console.clear()
        console.print(Panel(self.menu, title=self.title, style="bold red", title_align="left"))


class SettingsMenu:
    """Settings Menu"""
    
    def __init__(self):
        self.menu = "SETTINGS\n(1) OPERATIONS\n(2) TIMER\n(3) QUESTION COUNT/TYPE\n(4) MAIN MENU"
        self.Menu = Menu()
    def display_menu(self) -> None:
        console.clear()
        console.print(Panel(self.menu, title="MENTAL MATH MONSTER", style="bold red", title_align="left"))

        user_input = int(input("Enter: "))
        while user_input != 4:
            if user_input == 1:
                pass
               
            elif user_input == 2:
                pass
   
            elif user_input == 3:
                pass              
            try:
                user_input = int(input("Enter: "))
                console.print(Panel(renderable="WIP", title="TIMER", style="bold red", title_align="left"))
            except ValueError:
                console.print("ERROR: ENTER VALID NUMBER", style="bold red")
                user_input = 0

        


if __name__ == "__main__":
    try:
        Trplm()
    except KeyboardInterrupt:
        console.clear()
        console.print("Till Next Time.", style="red")
