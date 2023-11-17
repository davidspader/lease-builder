from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.routes.template_routes import router as template_router

app = FastAPI()

app.include_router(user_router)
app.include_router(template_router)