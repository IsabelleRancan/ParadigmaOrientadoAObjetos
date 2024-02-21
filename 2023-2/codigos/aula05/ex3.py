class Employee:
    "Criando o método __init__ para começar a class"

    def __init__(self, name= "", salary=0):
        self.name = name
        self.salary = salary

    "Criando o método raise_salary para calcular o aumento de salário"
    def raise_salary(self, aumento):
        self.salary = self.salary + (self.salary * aumento/100)
        return self.salary
    
    "Retornando as informações do funcionario"
    def get_info(self):
        return self.name, self.salary

"Criando dois objetos para a classe"

Funcionario1 = Employee("John Doe", 50000.0)
Funcionario2 = Employee("Jane Smith", 65000.0)

print(Funcionario1.get_info())
print(Funcionario2.get_info())

Funcionario1.raise_salary(10)    
Funcionario2.raise_salary(10) 

print(Funcionario1.get_info())
print(Funcionario2.get_info())

