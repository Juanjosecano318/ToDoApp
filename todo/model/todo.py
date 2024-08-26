# TODO: Add code here
class Todo:
    def __init__(self,code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self,tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str: #retorna un string
        return f"{self.code_id} - {self.title}"

class TodoBook:

    def __init__(self,todos):
        self.todos: dict[int, Todo] = {}  #Inicializamos un diccionario vacio

    def add_todo(self, title: str, description : str) -> int: #retorna un entero
        id = len(self.todos) + 1
        new_object = Todo(title, description)
        self.todos_[id] = new_object
        return id














