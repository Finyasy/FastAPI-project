from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy import func
from sqlalchemy.orm import relationship
from db.config import Base

class TaskModel(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    note = Column(String, nullable=False)
    completed = Column(Boolean, nullable=False)
    created_on = Column(DateTime(timezone=True), default=func.now(), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    owner = relationship('UserModel', back_populates='tasks')
    