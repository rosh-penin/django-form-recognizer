from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient

from constants import (DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER,
                       DEFAULT_DB_NAME)

app = FastAPI()


@app.post('/get_form')
async def get_forms_by_type():
    pass


@app.on_event("startup")
async def startup_event():
    try:
        if DB_HOST:
            app.mongodb_client = AsyncIOMotorClient(  # type: ignore
                f'mongodb://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}'
            )
        else:
            app.mongodb_client = AsyncIOMotorClient(  # type: ignore
                'mongodb://localhost:27017'
            )

        if DB_NAME:
            app.mongodb = app.mongodb_client[DB_NAME]  # type: ignore
        else:
            app.mongodb = app.mongodb_client[DEFAULT_DB_NAME]  # type: ignore
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.on_event("shutdown")
async def shutdown_event():
    app.mongodb_client.close()  # type: ignore
