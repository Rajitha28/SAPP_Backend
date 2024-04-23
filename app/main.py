from fastapi import Depends, FastAPI
from mongoalchemy.session import Session
from app.models import Item
from database import get_mongo_session

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/itemsn/")
async def get_items(session: Session = Depends(get_mongo_session)):
    try:
        # Use the session to query items
        items = Item.objects(session)
        return items
    except Exception as e:
        print(f"Error getting items: {e}")
        return None
