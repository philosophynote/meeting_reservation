from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional

class Booking(BaseModel):
    booking_id: int
    user_id: int
    room_id: int
    booked_num: int
    start_datetime: datetime
    end_datetime: datetime

class User(BaseModel):
    user_id: int
    user_name: str = Field(max_length=12)
    
class Room(BaseModel):
    room_id: int
    room_name: str = Field(max_length=12)
    capacity: int

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/")
async def index():
    return {"message": "Success"}

@app.post("/users")
async def users(users: User):
    return {"users": users}

@app.post("/rooms")
async def rooms(rooms: Room):
    return {"rooms": rooms}

@app.post("/bookings")
async def bookings(bookings: Booking):
    return {"bookings": bookings}