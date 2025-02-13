import streamlit as st
import duckdb
import pandas as pd
import datetime

# Database file (stores data locally)
DB_PATH = "mood_tracker.db"

# Function to initialize DuckDB table
def initialize_db():
    con = duckdb.connect(DB_PATH)
    con.execute("""
        CREATE TABLE IF NOT EXISTS moods (
            date DATE,
            mood_score INTEGER,
            energy_score INTEGER,
            notes TEXT
        )
    """)
    con.close()

# Save mood entry
def save_entry(date, mood, energy, notes):
    con = duckdb.connect(DB_PATH)
    con.execute("INSERT INTO moods VALUES (?, ?, ?, ?)", (date, mood, energy, notes))
    con.close()

# Retrieve past entries
def get_entries():
    con = duckdb.connect(DB_PATH)
    df = con.execute("SELECT * FROM moods ORDER BY date DESC").fetchdf()
    con.close()
    return df

# Initialize the database
initialize_db()

# UI Title
st.title("📊 Mood Tracker")

# Form Input
with st.form("mood_form"):
    st.subheader("How are you feeling today?")
    
    date = st.date_input("Select Date", datetime.date.today())
    mood = st.slider("Mood Score (1-10)", 1, 10, 5)
    energy = st.slider("Energy Level (1-10)", 1, 10, 5)
    notes = st.text_area("Notes (Optional)")
    
    submitted = st.form_submit_button("Save Entry")

    if submitted:
        save_entry(date, mood, energy, notes)
        st.success("Mood entry saved!")

# Display Past Entries
st.subheader("📅 Past Mood Entries")
entries = get_entries()

if not entries.empty:
    st.dataframe(entries)

    # Mood Trends Visualization
    st.subheader("📈 Mood & Energy Trends")
    st.line_chart(entries.set_index("date")[["mood_score", "energy_score"]])
else:
    st.info("No entries yet. Start tracking your mood!")

