from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field


class PersonIntel(BaseModel):
    summary: str = Field(description="Summary of the person")
    facts: list[str] = Field(description="Interesting facts about the person")
    topics_of_interests: list[str] = Field(
        description="Topics that interest the person"
    )
    ice_breaker: list[str] = Field(
        description="Create ice breakers to open a conversation for the person"
    )

    def to_dict(self):
        return {
            "summary": self.summary,
            "facts": self.facts,
            "topics": self.topics_of_interests,
            "ice_breaker": self.ice_breaker,
        }


person_intel_parser: PydanticOutputParser = PydanticOutputParser(
    pydantic_object=PersonIntel
)
