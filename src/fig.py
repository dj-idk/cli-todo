import pyfiglet
from rich.console import Console

# Create a console instance
console = Console()

# Generate text with pyfiglet
text = pyfiglet.figlet_format("Meow!")

# Print the text with a color using rich
console.print(f"[bold magenta]{text}[/bold magenta]")
