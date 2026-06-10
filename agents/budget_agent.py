# agents/budget_agent.py

from state import TravelState


def budget_agent(
    state: TravelState
):

    duration = state.get(
        "duration",
        7
    )

    flight_cost = 75000

    hotel_cost = (
        duration * 6000
    )

    food_cost = (
        duration * 1500
    )

    transport_cost = (
        duration * 1000
    )

    total_cost = (
        flight_cost
        + hotel_cost
        + food_cost
        + transport_cost
    )

    summary = {
        "flight_cost":
            f"₹{flight_cost:,}",

        "hotel_cost":
            f"₹{hotel_cost:,}",

        "food_cost":
            f"₹{food_cost:,}",

        "transport_cost":
            f"₹{transport_cost:,}",

        "total_cost":
            f"₹{total_cost:,}"
    }

    return {

        "budget_summary":
            summary,

        "llm_calls":
            state.get(
                "llm_calls",
                0
            ) + 1
    }

