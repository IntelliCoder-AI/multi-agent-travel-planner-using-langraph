# 🌍 AI Travel Planner using LangGraph Multi-Agent System

An intelligent travel planning application built using **LangGraph**, **Groq LLM**, **PostgreSQL Memory**, **Streamlit**, and multiple specialized AI agents.

The system automatically creates personalized travel plans by coordinating multiple AI agents responsible for flights, hotels, weather, visa requirements, attractions, budgeting, and itinerary generation.

---

# 🚀 Features

### Multi-Agent Architecture

The application uses multiple specialized agents:

| Agent               | Responsibility                                            |
| ------------------- | --------------------------------------------------------- |
| 🧠 Supervisor Agent | Extracts destination, duration, budget and travel details |
| ✈️ Flight Agent     | Retrieves flight recommendations                          |
| 🏨 Hotel Agent      | Finds suitable hotels                                     |
| ☀️ Weather Agent    | Fetches live weather data                                 |
| 🛂 Visa Agent       | Provides visa requirements                                |
| 📍 Attraction Agent | Discovers popular attractions                             |
| 💰 Budget Agent     | Estimates travel expenses                                 |
| 📝 Itinerary Agent  | Generates the final travel itinerary                      |

---

# 🏗️ Architecture

```text
                User Request
                       │
                       ▼
             ┌─────────────────┐
             │ Supervisor Agent │
             └────────┬────────┘
                      │
     ┌────────────────┼────────────────┐
     ▼                ▼                ▼
 Flight Agent    Hotel Agent     Weather Agent
     │                │                │
     ▼                ▼                ▼
 Visa Agent     Attraction Agent   Budget Agent
                      │
                      ▼
              Itinerary Agent
                      │
                      ▼
                Final Travel Plan
```

---

# 🧠 Memory

The application uses:

* PostgreSQL
* LangGraph Checkpointer
* Persistent conversation memory

This allows:

* User travel history
* Session persistence
* Agent state recovery
* Long-running conversations

---

# 🛠️ Tech Stack

### Backend

* Python
* LangGraph
* LangChain
* Groq
* PostgreSQL
* Psycopg

### Frontend

* Streamlit

### APIs

* Tavily Search API
* OpenWeather API
* TravelPayouts API

---

# 📂 Project Structure

```text
AI-Travel-Planner/

│
├── agents/
│   ├── supervisor_agent.py
│   ├── flight_agent.py
│   ├── hotel_agent.py
│   ├── weather_agent.py
│   ├── visa_agent.py
│   ├── attraction_agent.py
│   ├── budget_agent.py
│   └── itinerary_agent.py
│
├── components/
│   ├── cards.py
│   ├── agent_tracker.py
│   ├── hotel_cards.py
│   ├── visa_cards.py
│   ├── attraction_cards.py
│   └── travel_map.py
│
├── memory/
│   ├── postgres.py
│   └── history.py
│
├── tools/
│   ├── flight_tool.py
│   ├── tavily_tool.py
│   ├── weather_tool.py
│   └── visa_tool.py
│
├── utils/
│   └── pdf_export.py
│
├── config.py
├── state.py
├── main.py
├── ui.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/AI-Travel-Planner.git

cd AI-Travel-Planner
```

---

## 2. Create Virtual Environment

Windows:

```bash
python -m venv myvenv

myvenv\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv myvenv

source myvenv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🐘 PostgreSQL Setup

Install PostgreSQL locally.

Create database:

```sql
CREATE DATABASE travel_planner;
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key

TAVILY_API_KEY=your_tavily_api_key

OPENWEATHER_API_KEY=your_openweather_api_key

TRAVELPAYOUTS_API_TOKEN=your_travelpayouts_api_token

DATABASE_URL=postgresql://postgres:password@localhost:5432/travel_planner
```

---

# ▶️ Running the Application

## Start Streamlit UI

```bash
streamlit run ui.py
```

The application will open automatically in your browser.

Default URL:

```text
http://localhost:8501
```

---

# 💻 Running CLI Version

```bash
python main.py
```

Example:

```text
Enter Travel Request:

Plan a 10 day Japan trip from India under ₹2 lakh
```

---

# 📸 Example Query

```text
Plan a 7 day Japan trip from India under ₹2 lakh
```

The system will automatically:

* Find flights
* Recommend hotels
* Check weather
* Check visa requirements
* Find attractions
* Calculate budget
* Generate itinerary

---

# 🔮 Future Improvements

* Parallel LangGraph execution
* Real flight search integration
* Real hotel booking APIs
* Interactive maps
* Voice-based travel planning
* RAG-powered travel recommendations
* Multi-user authentication
* Cloud deployment

---

It helps the project reach more developers and AI enthusiasts.
