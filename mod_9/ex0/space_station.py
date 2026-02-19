from pydantic import BaseModel, field_validator, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str
    name: str
    crew_size: int
    power_level: float
    oxygen_level: float
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = None

    @field_validator("station_id")
    def is_valid_id(cls, value):
        if len(value) >= 3 and len(value) <= 10:
            return value
        raise ValueError("ID should be between 3 and 10")

    @field_validator("name")
    def is_valid_name(cls, value):
        if len(value) >= 1 and len(value) <= 50:
            return value
        raise ValueError("Name should be between 1 and 50")

    @field_validator("crew_size")
    def is_valid_size(cls, value):
        if value >= 1 and value <= 20:
            return value
        raise ValueError("crew_size must be between 1 and 20")

    @field_validator("power_level")
    def is_valid_power(cls, value):
        if value >= 0.0 and value <= 100.0:
            return value
        raise ValueError("power level must be between 0.0 and 100.0")

    @field_validator("oxygen_level")
    def is_valid_oxygen(cls, value):
        if value >= 0.0 and value <= 100.0:
            return value
        raise ValueError("oxygen level must be between 0.0 and 100.0")

    @field_validator("last_maintenance")
    def is_valid_maintenance(cls, value):
        if value < datetime.now():
            return value
        raise ValueError("last_maintenance cannot be in the future")

    @field_validator("is_operational")
    def is_valid_operation(cls, value):
        if value:
            return "Operational"
        return "Offline"


def main() -> None:
    mydict = {
            "station_id": "IGF584",
            "name": "International Space Station",
            "crew_size": 8,
            "power_level": 50.0,
            "oxygen_level": 909.0,
            "last_maintenance": datetime(2025, 12, 1),
            "is_operational": True
        }

    try:
        user = SpaceStation(**mydict)

        print("Space Station Data Validation")
        print("========================================")
        print("Valid station created:")
        print(f"ID: {user.station_id}")
        print(f"Name: {user.name}")
        print(f"Crew: {user.crew_size} people")
        print(f"Power: {user.power_level}%")
        print(f"Oxygen: {user.oxygen_level}%")
        print(f"Status: {user.is_operational}")

    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])

    print()
    print("Expected validation error:")
    try:
        user = SpaceStation(
            station_id="IGF584",
            name="International Space Station",
            crew_size=20,
            power_level=50.0,
            oxygen_level=60.8,
            last_maintenance=datetime(2026, 1, 1, 6, 9),
            is_operational=True,
            notes=65
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"].replace("Value error, ", ""))


if __name__ == "__main__":

    main()
