last_id = 0 

class Tarefa:
    def __init__(self, titulo, prioridade, concluida, descricao=None):
        global last_id
        last_id += 1 
        self.id = last_id
        self.titulo = titulo
        self.prioridade = prioridade
        self.concluida = concluida 
        self.descricao = descricao 

    def simples(self):
        return f"{ self.id } : { self.titulo }"

    def detalhada(self):
        return self.id + self.titulo + self.descricao + self.prioridade + self.concluida 
    
    def __lt__(self, other):
        return self.prioridade < other.prioridade 
    
class Lista: 
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa) 
        """Acessando o array tarefa que foi definido no método init, depois acessando o método append do array que vai adicionar
        o que está sendo colocado dentro de (tarefa)"""

    def remover_tarefa(self, id):
        self.tarefas = [t for t in self.tarefas if t.id != id]

    def editar_tarefa(self, id, titulo=None, descricao=None, prioridade=None, concluida=None):
        for t in self.tarefas:
            if t.id == id:
                if titulo !=None:
                    t.titulo=titulo
                if descricao !=None:
                    t.descricao=descricao
                if prioridade !=None:
                    t.prioridade=prioridade
                if concluida !=None:
                    t.concluida=concluida 

    def obter_tarefa(self, filtro=None, nao_concluidas=None):
        tarefas = sorted(self.tarefas, reverse = True)
        if nao_concluidas == True:
            tarefas = [t for t in tarefas if t.concluida != True]