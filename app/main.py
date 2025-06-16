from fastapi import FastAPI
from app.routers.user import router as user_router
from app.routers.post import router as post_router

app = FastAPI()
app.include_router(user_router, prefix="/user", tags=["users"])
app.include_router(post_router, prefix="/post", tags=["posts"])

app.get("/")
async def root():
    return {"status": "okay"}
