from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import create_db_and_tables
from app.dependencies import api_key_validation
from app.routers import channel, cronjob, user, dndbeyond, interactions

import env

@asynccontextmanager
async def lifespan(app: FastAPI):
    import env
    create_db_and_tables()

    yield 
    
    print("Application shutdown!")

app = FastAPI(dependencies=[Depends(api_key_validation)], lifespan=lifespan)

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# CORS configuration to allow localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=env.CORS_ALLOWED_ORIGIN,  # Add any other origins you want to allow
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

app.include_router(user.router)
app.include_router(cronjob.router)
app.include_router(channel.router)
app.include_router(dndbeyond.router)
app.include_router(interactions.router)

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=env.API_PORT)
