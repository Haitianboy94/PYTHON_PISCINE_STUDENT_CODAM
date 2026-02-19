# flake8: noqa
from enum import Enum
from pydantic import BaseModel, ValidationError, model_validator
from datetime import datetime


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str
    name: str
    rank: Rank
    age: int
    specialization: str
    years_experience: int
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str
    mission_name: str
    destination: str
    launch_date: datetime
    duration_days: int
    crew: list[CrewMember]
    mission_status: str = "planned"
    budget_millions: float

    @model_validator(mode='after')
    def safety_requirements(self):
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with 'M'")

        if not any(m.rank in (Rank.commander, Rank.captain) for m in self.crew):
            raise ValueError("Mission must have at "
                             "least one Commander or Captain")

        if self.duration_days > 365:
            expe = []
            for member in self.crew:
                if member.years_experience >= 5:
                    expe.append(member)
            if len(expe) < len(self.crew) / 2:
                raise ValueError("Long missions (> 365 days) "
                                 "need 50% experienced crew (5+ years)")

        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")

        return self


def main():
    print("Space Mission Crew Validation")
    print("=========================================")
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 6, 1),
            duration_days=900,
            crew=[
                CrewMember(member_id="C001",
                           name="Sarah Connor",
                           rank=Rank.commander,
                           age=45, specialization="Mission Command",
                           years_experience=20
                           ),
                CrewMember(member_id="C002",
                           name="John Smith",
                           rank=Rank.lieutenant,
                           age=35, specialization="Navigation",
                           years_experience=10
                           ),
                CrewMember(member_id="C003",
                           name="Alice Johnson",
                           rank=Rank.officer,
                           age=30, specialization="Engineering",
                           years_experience=6
                           )
            ],
            budget_millions=2500.0
        )

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(f"  - {member.name} ({member.rank.value}) "
                  f"- {member.specialization}")

    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])

    print()
    print("=========================================")
    try:
        mission = SpaceMission(
            mission_id="M2024_FAIL",
            mission_name="Doomed Mission",
            destination="Venus",
            launch_date=datetime(2024, 8, 1, 5, 9),
            duration_days=100,
            crew=[
                CrewMember(member_id="C004", name="Bob Lee", rank=Rank.cadet,
                           age=22, specialization="Repairs", years_experience=1),
                CrewMember(member_id="C005", name="Jane Doe", rank=Rank.officer,
                           age=28, specialization="Science", years_experience=3),
            ],
            budget_millions=500.0
        )

    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":

    main()
