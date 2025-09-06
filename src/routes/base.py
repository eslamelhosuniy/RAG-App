from fastapi import FastAPI,APIRouter
import os

base_router = APIRouter(prefix="/api/v1",tags = ["api v1"])


@base_router.get("/")
def welcome():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return{
        "Status" : 200,
        "message":{
            "app_name":app_name,
            "app_version":app_version
        }
    }