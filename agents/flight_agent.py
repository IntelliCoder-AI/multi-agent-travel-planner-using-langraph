from state import TravelState

from tools.flight_tool import (
    search_flights
)


def flight_agent(
    state: TravelState
):

    destination = state[
        "destination"
    ]

    flights = search_flights(
        "India",
        destination
    )

    return {

        "flights":
            flights,

        "llm_calls":
            state.get(
                "llm_calls",
                0
            ) + 1
    }
