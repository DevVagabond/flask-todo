def initiateTaskModel(db):
    """
    TaskDbModel
    """
    class Task(db.Model):
        """
        Task
        """
        __tablename__ = 'tasks'
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        uuid = db.Column(db.String(255), nullable=False)
        title = db.Column(db.String(100), nullable=False)
        description = db.Column(db.Text, nullable=False)
        status = db.Column(db.String(20), nullable=False, default='todo')
        created_at = db.Column(db.DateTime, nullable=False,
                               default=db.func.current_timestamp())
        updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(
        ), onupdate=db.func.current_timestamp())

        def __init__(self, uuid, title, description, status):
            self.uuid = uuid
            self.title = title
            self.description = description
            self.status = status

        def __repr__(self):
            return f'<{self.id} {self.uuid} {self.title} {self.description} {self.status}>'

    return Task
