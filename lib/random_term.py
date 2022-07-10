from random import randint

terminals = ["alacritty", "st"]

shells = ["fish", "bash", "pwsh"]

#returns a random terminal and shell
def random_term() -> str:
    
    term = terminals[randint(0, len(terminals)-1)]

    shell = shells[randint(0, len(shells)-1)]

    return f"{term} -e {shell}"