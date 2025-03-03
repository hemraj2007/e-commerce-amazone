from sqlalchemy.orm import Session
from api.database.models.student import Student
from api.database.schemas.student import StudentCreate

def create_student(db: Session, student: StudentCreate):
    db_student = Student(name=student.name, address=student.address, subject=student.subject)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
