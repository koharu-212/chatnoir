from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID as UUIDType
from sqlalchemy.dialects.postgresql import UUID

db = SQLAlchemy()

class Answer(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(50), nullable=False)
    question1 = db.Column(db.String(100), nullable=False)
    question2 = db.Column(db.String(100), nullable=False)
    question3 = db.Column(db.String(100), nullable=False)
    question4 = db.Column(db.String(100), nullable=False)
    question5 = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class MatchResult(db.Model):
    __tablename__ = 'match_results'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    employee_name = db.Column(db.String(50), nullable=False)
    superior_name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)