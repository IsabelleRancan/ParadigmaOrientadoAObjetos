import re 
texto = "Computer programs/The bugs try to eat my code/I must not let them."

def linhas():
    return re.findall(r"\w+", texto)

print(linhas())