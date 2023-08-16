from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError
from pydantic import BaseModel
import pymysql

pymysql.install_as_MySQLdb()

#Cadena de conexion a la base de datos
#db_url = process.env.DATABASE_URL
DATABASE_URL="mysql://admin:secret@192.168.0.4/fastapi"

app = FastAPI()

# Configuración de la base de datos
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Función de dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}


# Definición del modelo Usuario
class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    correo = Column(String(255), index=True)
    password = Column(String(255))

# Definición de la clase UsuarioCreate
class UsuarioCreate(BaseModel):
    correo: str
    password: str

# Crea las tablas en la base de datos
Base.metadata.create_all(bind=engine)

@app.post("/api/user")
def create_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    try:
        db_usuario = Usuario(**usuario.dict())
        db.add(db_usuario)
        db.commit()
        db.refresh(db_usuario)
        return db_usuario
    except SQLAlchemyError as e:
        db.rollback()  # Revierte la transacción si ocurre un error
        raise HTTPException(status_code=500, detail="Error al insertar en la base de datos")