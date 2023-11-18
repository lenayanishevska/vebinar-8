class Classroom:
    def __init__(self, classroom_id, name, capacity):
        self.classroom_id = classroom_id
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return f"Classroom {self.name} (ID: {self.classroom_id}) with a capacity of {self.capacity}."

