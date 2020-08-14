from typing import Union

from fastapi import FastAPI, Response, Request

from .schemas import OnePaste, ManyPastes, OnePasteLoaded


app = FastAPI()


@app.get('/')
async def many_pastes():  # TODO: return pydantic
    '''Gets all pastes available'''
    ...  # TODO: fetch query from DB
    resp = {"data":
            [
                {"name": ..., "content": ..., "expires": ..., "groups": []}
            ]
            }
    return resp


@app.get('/{file_name}/', response_model=OnePaste)
async def one_paste(file_name: str):
    paste = ...  # TODO: fetch one from DB
    if paste:
        return {"name": ..., "content": ..., "expires": ..., "groups": []}
    else:
        return Response(status_code=404)


@app.post('/')
async def load_paste(file: OnePasteLoaded):
    db_result = ...  # TODO: saved in the database
    name = db_result["name"]
    return {"name": name}


@app.delete('/{file_name}/')
async def one_paste(file_name: str):
    paste = ...  # TODO: fetch one from DB
    if paste:
        return Response(status_code=204)
    else:
        return Response(status_code=404)