from pydantic import BaseModel

class ExtractTextResponse(BaseModel):
    filename: str
    text: str

