from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app import database
from app.sensors import schemas, models, crud

from app.sensors import routers as sensor
from app.measurements_type import routers as measurements_type
from app.meteostatins import routers as meteostatins
from app.measurements import routers as measurements


app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)

app.include_router(sensor.router)
app.include_router(measurements_type.router)
app.include_router(meteostatins.router)
app.include_router(measurements.router)

# Запуск сервера FastAPI (при необходимости)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)