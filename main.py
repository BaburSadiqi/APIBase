from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel 
from typing import List, Annotated
import model
from database import engine, sessionlocal
from sqlalchemy.orm import Session

test_app = FastAPI()
model.Base.metadata.create_all(bind=engine)

class ChoiceBase(BaseModel):
    Choice_text: str
    is_correct: bool

class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

db_dependecy = Annotated[Session, Depends(get_db)]


@test_app.get("/question/{question_id}")
async def read_question(question_id: int, db: db_dependecy):
    result = db.query(model.Questions).filter(model.Questions.id == question_id).first
    if not result:
        raise HTTPException(status_code=404, details="Question is not found")
    return result



@test_app.post("/question/")
async def create_question(question: QuestionBase, db: db_dependecy):
    db_question = model.Questions(question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    for choice in question.choices:
        db_choices = model.Choices(choice_text=choice.Choice_text, is_correct=choice.is_correct, question_id=db_question.id)
        db.add(db_choices)
    db.commit()
