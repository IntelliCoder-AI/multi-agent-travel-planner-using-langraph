import streamlit as st
from langchain_core.messages import HumanMessage

from main import app

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');

/* Global and App */
.stApp {
    background-color: #0b0f19;
    background-image: 
        radial-gradient(at 0% 0%, hsla(253,16%,7%,1) 0, transparent 50%), 
        radial-gradient(at 50% 0%, hsla(225,39%,30%,0.05) 0, transparent 50%), 
        radial-gradient(at 100% 0%, hsla(339,49%,30%,0.05) 0, transparent 50%);
    font-family: 'Outfit', sans-serif !important;
    color: #e2e8f0;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: rgba(15, 23, 42, 0.7) !important;
    backdrop-filter: blur(20px) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.05);
}
[data-testid="stSidebar"] h1 {
    font-weight: 700;
    background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Typography */
h1, h2, h3, h4, h5, h6, span, p, div, label {
    font-family: 'Outfit', sans-serif;
}

/* Hero Title */
.hero-container {
    padding: 3rem 0 1rem 0;
    text-align: center;
    animation: fadeIn 1s ease-out;
}

.hero-title {
    font-size: 4.5rem;
    font-weight: 800;
    background: linear-gradient(to right, #00c6ff, #0072ff);
    background: linear-gradient(135deg, #12c2e9, #c471ed, #f64f59);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
    letter-spacing: -0.03em;
    line-height: 1.2;
}

.hero-subtitle {
    font-size: 1.3rem;
    color: #94a3b8;
    font-weight: 400;
    margin-bottom: 2.5rem;
}

/* Custom Metric Cards */
.premium-metric-card {
    background: rgba(30, 41, 59, 0.4);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 1.5rem;
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease, background 0.3s ease;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    margin-bottom: 1rem;
}

.premium-metric-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    background: rgba(30, 41, 59, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.15);
}

.metric-title {
    color: #94a3b8;
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 0.5rem;
    font-weight: 600;
}

.metric-value {
    color: #f8fafc;
    font-size: 2rem;
    font-weight: 700;
    background: linear-gradient(135deg, #ffffff 0%, #e2e8f0 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Input Area Styling */
.stTextArea label {
    font-weight: 600 !important;
    font-size: 1.1rem !important;
    color: #e2e8f0 !important;
    margin-bottom: 0.5rem !important;
}
.stTextArea textarea {
    background-color: rgba(15, 23, 42, 0.6) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    color: #f8fafc !important;
    border-radius: 16px !important;
    padding: 1.5rem !important;
    font-size: 1.1rem !important;
    box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.06) !important;
    transition: all 0.3s ease !important;
}

.stTextArea textarea:focus {
    border-color: #8b5cf6 !important;
    box-shadow: 0 0 0 2px rgba(139, 92, 246, 0.2), inset 0 2px 4px 0 rgba(0, 0, 0, 0.06) !important;
}

/* Button Styling */
.stButton button {
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.75rem 2rem !important;
    font-weight: 600 !important;
    font-size: 1.2rem !important;
    letter-spacing: 0.025em !important;
    transition: all 0.3s ease !important;
    width: 100% !important;
    box-shadow: 0 4px 14px 0 rgba(99, 102, 241, 0.39) !important;
    margin-top: 1rem !important;
}

.stButton button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4) !important;
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%) !important;
}

.stButton button:active {
    transform: translateY(1px) !important;
}

/* Tabs Styling */
.stTabs [data-baseweb="tab-list"] {
    gap: 12px;
    background-color: transparent;
    padding-bottom: 5px;
}
.stTabs [data-baseweb="tab"] {
    background-color: rgba(30, 41, 59, 0.4);
    border-radius: 8px;
    border: 1px solid rgba(255,255,255,0.05);
    color: #94a3b8;
    padding: 12px 24px;
    font-weight: 500;
    transition: all 0.2s;
}
.stTabs [data-baseweb="tab"]:hover {
    background-color: rgba(30, 41, 59, 0.8);
    color: #f8fafc;
}
.stTabs [aria-selected="true"] {
    background-color: rgba(139, 92, 246, 0.15) !important;
    border: 1px solid rgba(139, 92, 246, 0.5) !important;
    color: #fff !important;
    box-shadow: 0 0 15px rgba(139, 92, 246, 0.2);
}

/* Sidebar Elements */
.agent-list {
    display: flex;
    flex-direction: column;
    gap: 0.85rem;
    margin-top: 1.5rem;
}
.agent-item {
    display: flex;
    align-items: center;
    background: rgba(255, 255, 255, 0.03);
    padding: 0.85rem 1rem;
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.05);
    transition: all 0.3s;
}
.agent-item:hover {
    background: rgba(255, 255, 255, 0.08);
    transform: translateX(5px);
    border-color: rgba(255, 255, 255, 0.15);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.agent-icon {
    font-size: 1.4rem;
    margin-right: 1rem;
}
.agent-name {
    font-size: 1rem;
    font-weight: 500;
    color: #e2e8f0;
}
.status-dot {
    width: 10px;
    height: 10px;
    background-color: #10b981;
    border-radius: 50%;
    margin-left: auto;
    box-shadow: 0 0 8px #10b981;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.4); }
    70% { box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }
    100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Divider styling */
hr {
    border-color: rgba(255, 255, 255, 0.08) !important;
    margin: 2.5rem 0 !important;
}

/* Subheaders */
.stMarkdown h3 {
    font-weight: 700;
    color: #f8fafc;
    letter-spacing: -0.01em;
}

/* JSON Output */
.stJson {
    background-color: rgba(15, 23, 42, 0.5) !important;
    border-radius: 12px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
}

/* Alerts */
.stAlert {
    border-radius: 12px !important;
    border: none !important;
}

/* Progress bar container */
.stProgress > div > div > div {
    background-color: #8b5cf6 !important;
    background-image: linear-gradient(90deg, #6366f1, #8b5cf6, #ec4899) !important;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# SIDEBAR
# -----------------------------------

with st.sidebar:
    st.markdown("<h1>🌍 Travel Copilot</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.2); padding: 10px; border-radius: 8px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;'>
        <div class='status-dot' style='margin: 0 10px 0 0;'></div>
        <span style='color: #10b981; font-weight: 600; font-size: 0.9rem;'>Multi-Agent System Active</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='margin: 1rem 0 !important;'>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='font-size: 1.1rem; color: #94a3b8; font-weight: 600; margin-bottom: 10px;'>Active Agents</h3>", unsafe_allow_html=True)
    
    agents_html = """
    <div class="agent-list">
        <div class="agent-item"><span class="agent-icon">🧠</span><span class="agent-name">Supervisor Agent</span><div class="status-dot"></div></div>
        <div class="agent-item"><span class="agent-icon">✈️</span><span class="agent-name">Flight Agent</span><div class="status-dot"></div></div>
        <div class="agent-item"><span class="agent-icon">🏨</span><span class="agent-name">Hotel Agent</span><div class="status-dot"></div></div>
        <div class="agent-item"><span class="agent-icon">☀️</span><span class="agent-name">Weather Agent</span><div class="status-dot"></div></div>
        <div class="agent-item"><span class="agent-icon">🛂</span><span class="agent-name">Visa Agent</span><div class="status-dot"></div></div>
        <div class="agent-item"><span class="agent-icon">📍</span><span class="agent-name">Attraction Agent</span><div class="status-dot"></div></div>
        <div class="agent-item"><span class="agent-icon">💰</span><span class="agent-name">Budget Agent</span><div class="status-dot"></div></div>
        <div class="agent-item"><span class="agent-icon">📝</span><span class="agent-name">Itinerary Agent</span><div class="status-dot"></div></div>
    </div>
    """
    st.markdown(agents_html, unsafe_allow_html=True)

# -----------------------------------
# HERO
# -----------------------------------

st.markdown(
    """
    <div class='hero-container'>
        <div class='hero-title'>AI Travel Planner</div>
        <div class='hero-subtitle'>Plan your next adventure using LangGraph Multi-Agent AI architecture</div>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------------
# METRICS
# -----------------------------------

def create_metric_card(title, value):
    return f"""
    <div class='premium-metric-card'>
        <div class='metric-title'>{title}</div>
        <div class='metric-value'>{value}</div>
    </div>
    """

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(create_metric_card("Agents", "8"), unsafe_allow_html=True)
with col2:
    st.markdown(create_metric_card("Memory", "Postgres"), unsafe_allow_html=True)
with col3:
    st.markdown(create_metric_card("Weather", "Live"), unsafe_allow_html=True)
with col4:
    st.markdown(create_metric_card("LLM", "Llama 3.3"), unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------------
# INPUT
# -----------------------------------

input_container = st.container()
with input_container:
    query = st.text_area(
        "Describe your dream trip",
        placeholder="e.g. Plan a 10 day Japan trip from India under ₹2 lakh exploring culture and food",
        height=140,
        label_visibility="visible"
    )

    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        generate = st.button("✨ Generate Travel Plan", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------------
# GENERATE
# -----------------------------------

if generate:
    if not query.strip():
        st.warning("Please enter a travel request.")
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
            status.info(f"Running {agent}")
            progress.progress((i + 1) / len(agents))

        config = {
            "configurable": {
                "thread_id": "streamlit_user"
            }
        }

        result = app.invoke(
            {
                "messages": [HumanMessage(content=query)],
                "user_query": query,
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

        status.success("Travel Plan Generated")
        st.divider()

        # -----------------------------------
        # MAIN RESULT
        # -----------------------------------

        st.subheader("🗺️ Final Travel Plan")
        
        st.markdown(result["itinerary"])

        st.divider()

        # -----------------------------------
        # TABS
        # -----------------------------------
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            ["✈️ Flights", "🏨 Hotels", "☀️ Weather", "🛂 Visa", "📍 Attractions"]
        )

        with tab1:
            st.json(result["flights"])
        with tab2:
            st.json(result["hotels"])
        with tab3:
            st.json(result["weather"])
        with tab4:
            st.json(result["visa"])
        with tab5:
            st.json(result["attractions"])

        st.divider()

        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; align-items: center; padding: 1.5rem; background: rgba(139, 92, 246, 0.1); border-radius: 12px; border: 1px solid rgba(139, 92, 246, 0.3); box-shadow: 0 4px 20px rgba(139, 92, 246, 0.15);">
                <span style="font-size: 1.2rem; color: #e2e8f0; font-weight: 500;">
                    🤖 Total LLM Agent Calls Used: <strong style="color: #a78bfa; font-size: 1.5rem; margin-left: 10px;">{result['llm_calls']}</strong>
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )