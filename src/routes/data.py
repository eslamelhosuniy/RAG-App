from fastapi import FastAPI,APIRouter,Depends,UploadFile
from helpers.config import get_settings, Settings
from controllers import DataController
import os

data_router = APIRouter(prefix="/api/v1/data",tags = ["api v1/data"])

@data_router.post("/upload/{project_id}")
async def upload_data(project_id:str , file:UploadFile,app_settings: Settings = Depends(get_settings)):

        is_valid = DataController().validate_uploaded_file(file=file)
        return is_valid
