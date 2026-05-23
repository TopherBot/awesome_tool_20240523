from pydantic import BaseModel, Field

class Person(BaseModel):
    """A tiny data model representing a person to greet."""
    name: str = Field(..., description="The person's name")
    age: int | None = Field(None, ge=0, description="Optional age")
