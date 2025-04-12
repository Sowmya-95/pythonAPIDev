from fastapi import FastAPI
from .routers import post, user, auth, vote
from . import models
from .database import engine  # Import the engine from the database module
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# models.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")  # Decorator
async def root():
    return {"message": "Hello World successfully deployed from CI/CD pipeline!"}
