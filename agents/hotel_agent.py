from state import TravelState

from tools.tavily_tool import (
    tavily_search
)


def hotel_agent(
    state: TravelState
):

    destination = state[
        "destination"
    ]

    hotels = tavily_search(
        f"""
        Best hotels in {destination}

        Include:
        - luxury hotels
        - mid-range hotels
        - budget hotels
        """
    )

    return {

        "hotels":
            hotels,

        "llm_calls":
            state.get(
                "llm_calls",
                0
            ) + 1
    }

