from fastapi import APIRouter

router = APIRouter()


@router.get("/sensors/{sensor_id}")
async def test():
    # some async operation could happen here
    # example: `notes = await get_all_notes()`
    return {"ping": "test!"}
