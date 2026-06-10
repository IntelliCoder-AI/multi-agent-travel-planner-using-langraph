from dotenv import load_dotenv

load_dotenv()

from langgraph.graph import (
    StateGraph,
    START,
    END
)

from langchain_core.messages import (
    HumanMessage
)

from state import TravelState

from memory.postgres import (
    get_checkpointer
)

from agents.supervisor_agent import (
    supervisor_agent
)

from agents.flight_agent import (
    flight_agent
)

from agents.hotel_agent import (
    hotel_agent
)

from agents.weather_agent import (
    weather_agent
)

from agents.visa_agent import (
    visa_agent
)

from agents.attraction_agent import (
    attraction_agent
)

from agents.budget_agent import (
    budget_agent
)

from agents.itinerary_agent import (
    itinerary_agent
)

# -----------------------------
# GRAPH
# -----------------------------

graph = StateGraph(
    TravelState
)

# -----------------------------
# NODES
# -----------------------------

graph.add_node(
    "supervisor",
    supervisor_agent
)

graph.add_node(
    "flight",
    flight_agent
)

graph.add_node(
    "hotel",
    hotel_agent
)

graph.add_node(
    "weather",
    weather_agent
)

graph.add_node(
    "visa",
    visa_agent
)

graph.add_node(
    "attraction",
    attraction_agent
)

graph.add_node(
    "budget",
    budget_agent
)

graph.add_node(
    "itinerary",
    itinerary_agent
)

# -----------------------------
# EDGES
# -----------------------------

graph.add_edge(
    START,
    "supervisor"
)

graph.add_edge(
    "supervisor",
    "flight"
)

graph.add_edge(
    "flight",
    "hotel"
)

graph.add_edge(
    "hotel",
    "weather"
)

graph.add_edge(
    "weather",
    "visa"
)

graph.add_edge(
    "visa",
    "attraction"
)

graph.add_edge(
    "attraction",
    "budget"
)

graph.add_edge(
    "budget",
    "itinerary"
)

graph.add_edge(
    "itinerary",
    END
)

# -----------------------------
# MEMORY
# -----------------------------

checkpointer = (
    get_checkpointer()
)

app = graph.compile(
    checkpointer=checkpointer
)

# -----------------------------
# CLI
# -----------------------------

if __name__ == "__main__":

    config = {
        "configurable": {
            "thread_id":
                "travel_user_001"
        }
    }

    user_query = input(
        "\nEnter Travel Request: "
    )

    result = app.invoke(
        {
            "messages": [
                HumanMessage(
                    content=user_query
                )
            ],

            "user_query":
                user_query,

            "destination": "",

            "duration": 0,

            "budget": "",

            "flights": [],

            "hotels": [],

            "attractions": [],

            "weather": {},

            "visa": {},

            "budget_summary": {},

            "itinerary": "",

            "llm_calls": 0
        },
        config=config
    )

    print(
        "\n"
        + "=" * 80
    )

    print(
        "FINAL TRAVEL PLAN"
    )

    print(
        "=" * 80
    )

    print()

    print(
        result["itinerary"]
    )

    print(
        "\n"
        + "=" * 80
    )

    print(
        f"Total Agent Calls: "
        f"{result['llm_calls']}"
    )

    print(
        "=" * 80
    )
