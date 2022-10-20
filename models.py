from app import database

class Task(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    title = database.Column(database.String(100), nullable = False)
    date = database.Column(database.Date, nullable = False)
    
    def __repr__(self):
        return f'{self.title} created on {self.date}'
