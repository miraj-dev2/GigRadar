from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models, schemas,auth


router = APIRouter(prefix="/gigs", tags=["gigs"])



@router.post("/", response_model=schemas.GigOut)
def create_gig(gig: schemas.GigCreate, db: Session = Depends(get_db ), current_user: models.User = Depends(auth.get_current_user)):
    new_gig = models.Gig(title=gig.title, description=gig.description, price=gig.price, owner=current_user)
    db.add(new_gig)
    db.commit()
    db.refresh(new_gig)
    return new_gig

@router.get("/", response_model=List[schemas.GigOut])       
def list_gigs(db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user),):
    return db.query(models.Gig).filter(models.Gig.user_id == current_user.id).all()




@router.get("/{gig_id}", response_model=schemas.GigOut)
def get_gig(gig_id: int, db: Session = Depends(get_db), 
        current_user: models.User = Depends(auth.get_current_user)):
    gig = db.query(models.Gig).filter(models.Gig.id == gig_id, models.Gig.user_id == current_user.id).first()
    if not gig:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gig not found")
    return gig


@router.put("/{gig_id}", response_model=schemas.GigOut)
def update_gig(gig_id: int, gig: schemas.GigCreate, db: Session = Depends(get_db), 
        current_user: models.User = Depends(auth.get_current_user)):
    db_gig = db.query(models.Gig).filter(models.Gig.id == gig_id, models.Gig.user_id == current_user.id).first()
    if not db_gig:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gig not found")
    db_gig.title = gig.title
    db_gig.description = gig.description
    db_gig.price = gig.price
    db.commit()
    db.refresh(db_gig)
    return db_gig

@router.delete("/{gig_id}", status_code=status.HTTP_200_OK)
def delete_gig(gig_id: int, db: Session = Depends(get_db),
        current_user: models.User = Depends(auth.get_current_user)):
    db_gig = db.query(models.Gig).filter(models.Gig.id == gig_id, models.Gig.user_id == current_user.id).first()
    if not db_gig:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gig not found")
    db.delete(db_gig)
    db.commit()
    return { 
    "message": "Gig deleted successfully"}