# agents/weather_agent.py

from state import TravelState

from tools.weather_tool import (
    get_weather
)


def weather_agent(
    state: TravelState
):

    weather = get_weather(
        state["destination"]
    )

    return {

        "weather":
            weather,

        "llm_calls":
            state.get(
                "llm_calls",
                0
            ) + 1
    }

