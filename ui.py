import streamlit as st
from langchain_core.messages import HumanMessage

from main import app

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown("""
<style>

.stApp {
    background: #0f172a;
}

.hero-title {
    text-align:center;
    font-size:3rem;
    font-weight:800;
    background: linear-gradient(
        90deg,
        #06b6d4,
        #8b5cf6
    );
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.hero-subtitle {
    text-align:center;
    color:#cbd5e1;
    font-size:1.2rem;
    margin-bottom:30px;
}

.glass-card {
    background: rgba(255,255,255,0.05);
    border-radius:20px;
    padding:20px;
    backdrop-filter: blur(15px);
    border:1px solid rgba(255,255,255,0.1);
}

.metric-box {
    background:#111827;
    border-radius:15px;
    padding:15px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# SIDEBAR
# -----------------------------------

with st.sidebar:

    st.title("🌍 Travel Copilot")

    st.success(
        "Multi-Agent System Active"
    )

    st.markdown("---")

    st.write("🧠 Supervisor Agent")
    st.write("✈️ Flight Agent")
    st.write("🏨 Hotel Agent")
    st.write("☀️ Weather Agent")
    st.write("🛂 Visa Agent")
    st.write("📍 Attraction Agent")
    st.write("💰 Budget Agent")
    st.write("📝 Itinerary Agent")

# -----------------------------------
# HERO
# -----------------------------------

st.markdown(
    """
    <div class='hero-title'>
    AI Travel Planner
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='hero-subtitle'>
    Plan your next adventure using LangGraph Multi-Agent AI
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------------
# METRICS
# -----------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Agents",
        "8"
    )

with col2:
    st.metric(
        "Memory",
        "Postgres"
    )

with col3:
    st.metric(
        "Weather",
        "Live"
    )

with col4:
    st.metric(
        "LLM",
        "Llama 3.3"
    )

st.divider()

# -----------------------------------
# INPUT
# -----------------------------------

query = st.text_area(
    "",
    placeholder=
    "Plan a 10 day Japan trip from India under ₹2 lakh",
    height=120
)

generate = st.button(
    "🚀 Generate Travel Plan",
    use_container_width=True
)

# -----------------------------------
# GENERATE
# -----------------------------------

if generate:

    if not query.strip():

        st.warning(
            "Please enter a travel request."
        )

    else:

        progress = st.progress(0)

        status = st.empty()

        agents = [
            "Supervisor Agent",
            "Flight Agent",
            "Hotel Agent",
            "Weather Agent",
            "Visa Agent",
            "Attraction Agent",
            "Budget Agent",
            "Itinerary Agent"
        ]

        for i, agent in enumerate(agents):

            status.info(
                f"Running {agent}"
            )

            progress.progress(
                (i + 1) / len(agents)
            )

        config = {
            "configurable": {
                "thread_id":
                    "streamlit_user"
            }
        }

        result = app.invoke(
            {
                "messages": [
                    HumanMessage(
                        content=query
                    )
                ],

                "user_query":
                    query,

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

        status.success(
            "Travel Plan Generated"
        )

        st.divider()

        # -----------------------------------
        # MAIN RESULT
        # -----------------------------------

        st.subheader(
            "🗺️ Final Travel Plan"
        )

        st.markdown(
            result["itinerary"]
        )

        st.divider()

        # -----------------------------------
        # TABS
        # -----------------------------------

        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            [
                "✈️ Flights",
                "🏨 Hotels",
                "☀️ Weather",
                "🛂 Visa",
                "📍 Attractions"
            ]
        )

        with tab1:

            st.json(
                result["flights"]
            )

        with tab2:

            st.json(
                result["hotels"]
            )

        with tab3:

            st.json(
                result["weather"]
            )

        with tab4:

            st.json(
                result["visa"]
            )

        with tab5:

            st.json(
                result["attractions"]
            )

        st.divider()

        st.metric(
            "Total Agent Calls",
            result["llm_calls"]
        )