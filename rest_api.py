from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from model import Bank, Branch
from database import get_db

app = FastAPI()

@app.get("/banks/")
def get_banks(db: Session = Depends(get_db)):
    banks = db.query(Bank).all()
    return banks

@app.get("/branches/{branch_ifsc}")
def get_branch(branch_ifsc: str, db: Session = Depends(get_db)):
    branch = db.query(Branch).filter(Branch.ifsc == branch_ifsc).first()
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")
    return branch
