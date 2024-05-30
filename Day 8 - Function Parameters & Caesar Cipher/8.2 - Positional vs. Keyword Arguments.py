# Functions with more than 1 Input

def greet_with(name, location):
    print(f"Hello! {name}")
    print(f"How is the weather at {location}?")


greet_with("Mujeeb", "Hyderabad")

greet_with("Hyderabad", "Mujeeb")  # Positional arguments

greet_with(location="Hyderabad", name="Mujeeb")  # Keyword arguments
