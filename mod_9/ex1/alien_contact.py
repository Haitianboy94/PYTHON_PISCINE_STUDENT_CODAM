from pydantic import BaseModel, model_validator, ValidationError
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str
    timestamp: datetime
    location: str
    contact_type: ContactType
    signal_strength: float
    duration_minutes: int
    witness_count: int
    message_received: str | None
    is_verified: bool = True

    @model_validator(mode='after')
    def validate_rules(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError("Telepathic contact requires at least 3 wtnesses")

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) "
                             "should include received messages")

        return self


def main():

    try:
        contact = ContactType.radio
        my_dict = {
                    "contact_id": "AC_2024_001",
                    "timestamp": datetime(2024, 1, 1, 9, 6),
                    "location": "Area 51, Nevada",
                    "contact_type": contact,
                    "signal_strength": 8.5,
                    "duration_minutes": 45,
                    "witness_count": 5,
                    "message_received": "Greetings from Zeta Reticuli"
                    }

        alien_con = AlienContact(**my_dict)
        print("Valid Contact repport:")
        print("========================================")
        print(f"ID: {alien_con.contact_id}")
        print(f"Type: {alien_con.contact_type}")
        print(f"Location: {alien_con.location}")
        print(f"Signal: {alien_con.signal_strength}/10")
        print(f"Duration: {alien_con.duration_minutes} minutes")
        print(f"Witnesses: {alien_con.witness_count}")
        print(f"Message: {alien_con.message_received}")
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])

    print("======================================")
    try:
        contact = ContactType.telepathic
        my_dict = {
                    "contact_id": "AC_2024_001",
                    "timestamp": datetime(2024, 1, 1, 9, 6),
                    "location": "Area 51, Nevada",
                    "contact_type": contact,
                    "signal_strength": 8.5,
                    "duration_minutes": 45,
                    "witness_count": 1,
                    "message_received": "Greetings from Zeta Reticuli"
                    }

        alien_con = AlienContact(**my_dict)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
