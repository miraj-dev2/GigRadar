from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import models, schemas, auth

router = APIRouter(prefix="/applications", tags=["applications"])


@router.post("/",response_model=schemas.ApplicationOut)
def create_application(
    application: schemas.ApplicationCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
    ):
    gig = db.query(models.Gig).filter(models.Gig.id == application.gig_id, models.Gig.user_id == current_user.id).first()
    if not gig:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gig not found")
    new_application = models.Application(**application.dict())
    db.add(new_application)
    db.commit()
    db.refresh(new_application)
    return new_application


@router.get("/",response_model=List[schemas.ApplicationOut])
def list_applications(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user),

):
    return {
        db.query(models.Application)
        .join(models.Gig)
        .filter(models.Gig.user_id == current_user.id).all()
    }


@router.put("/{application_id}",response_model=schemas.ApplicationOut)
def update_application(
    application_id: int,
    updated: schemas.ApplicationCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    application = (
        db.query(models.Application).join(models.Gig).filter(models.Application.id == application_id, models.Gig.user_id == current_user).first()

    )
    if not application:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found")
    application.status = updated.status
    application.notes = updated.notes
    db.commit()
    db.refresh(application)
    return application


@router.delete("/{application_id}", response_model=schemas.ApplicationOut)
def delete_application(
    application_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
    ):
    application = (
        db.query(models.application)
        .join(models.Gig)
        .filter(models.Application.id == application_id, models.Gig.user_id == current_user).first()

    )
    if not application:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found")
    db.delete(application)
    db.commit()
    return {
        "detail": "application deleted successfully."
    }