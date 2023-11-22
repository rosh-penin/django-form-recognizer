from fastapi import Depends, Request

from engine import app
from events import shutdown_event, startup_event
from schemas import FormCreation


@app.post('/get_form')
async def get_forms_by_type():
    pass


@app.post('/add_form')
async def add_form(query_params: FormCreation = Depends()):
    print(query_params, flush=True)


app.router.add_event_handler("startup", startup_event)
app.router.add_event_handler("shutdown", shutdown_event)
