from textual.containers import Grid
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Digits, Label

class TrplM(App):

    BINDINGS = [
                ("q", "quit", "Quit Game"),
                ]
    CSS_PATH = "styles.tcss"
    menu_options = ["PLAY", "VS", "SETTINGS", "EXIT"]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app"""
        yield Header()
        yield Footer()
        yield Label("MENTAL MATH MONSTER", id="title")

    
    def quit_app(self) -> None:
        """An action to quit the game"""
        self.action_quit()
 

if __name__ == "__main__":
    app = TrplM()
    app.run()
