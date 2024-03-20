from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app import database
from app.sensors import schemas, models, crud

from app.sensors import routers as sensor
from app.measurements_type import routers as measurements_type
from app.meteostatins import routers as meteostatins
from app.measurements import routers as measurements
from app.sensors.routers import tags_metadata as Sen
from app.measurements_type.routers import tags_metadata as Mea_type
from app.meteostatins.routers import tags_metadata as Meteost
from app.measurements.routers import tags_metadata as Measurem

description = """
My WeatherStation App API enables the management and tracking of meteorological stations, their sensors, and measurements. 🌦️

## Meteostations

Manage meteorological stations:
* **Create meteostations**
* **Read meteostations**
* **Update meteostations**
* **Delete meteostations**

## Sensors

Manage sensors attached to meteorological stations:
* **Add sensors to meteostations**
* **List sensors of meteostations**
* **Update sensor details**
* **Remove sensors from meteostations**

## Measurements

Handle sensor measurements:
* **Add new measurements**
* **Retrieve measurements**
* **Delete measurements**


## Measurements Type

Operations related to the types of measurements sensors can perform:
* **Define new measurements types**
* **View available measurements types**
* **Update existing measurements types**
* **Remove unused measurements types**
"""


tags_metadata = Sen + Mea_type + Meteost + Measurem
app = FastAPI(
    title="WeatherStation Management App",
    description=description,
    version="1.0.0",
    terms_of_service="https://example.com/terms/",
    contact={
        "name": "Admin",
        "url": "https://weatherstation.example.com/contact/",
        "email": "contact@weatherstation.example.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
    openapi_tags=tags_metadata
)




models.Base.metadata.create_all(bind=database.engine)

app.include_router(sensor.router, tags=["Sensors"])
app.include_router(measurements_type.router, tags=["Measurements Type"])
app.include_router(meteostatins.router, tags=["Meteostation Sensors"])
app.include_router(measurements.router, tags=["Measurements"])

# Запуск сервера FastAPI (при необходимости)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)