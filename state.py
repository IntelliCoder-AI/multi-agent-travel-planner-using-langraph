from typing import TypedDict
from typing import Annotated

import operator

from langchain_core.messages import (
    AnyMessage
)


class TravelState(TypedDict):

    messages: Annotated[
        list[AnyMessage],
        operator.add
    ]

    user_query: str

    destination: str

    duration: int

    budget: str

    flights: list

    hotels: list

    attractions: list

    weather: dict

    visa: dict

    budget_summary: dict

    itinerary: str

    llm_calls: int

