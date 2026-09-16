import os
import time
import random

import streamlit as st
from dotenv import load_dotenv
from google import genai


# ============================================================
# CONFIGURATION
# ============================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error(
        "❌ Gemini API key not found.\n\n"
        "Please create a .env file and add:\n\n"
        "GEMINI_API_KEY=your_api_key"
    )
    st.stop()


# Create Gemini client
client = genai.Client(api_key=API_KEY)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CineGen - AI Movie Plot Generator",
    page_icon="🎬",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 48px;
        font-weight: bold;
        color: #ff4b4b;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #777;
        margin-bottom: 30px;
    }

    .movie-box {
        padding: 20px;
        border-radius: 15px;
        background-color: #111827;
        color: white;
        margin-top: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# TITLE
# ============================================================

st.markdown(
    '<div class="main-title">🎬 CineGen</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-Powered Movie Plot Generator'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# MOVIE OPTIONS
# ============================================================

genres = [
    "Action",
    "Comedy",
    "Horror",
    "Romance",
    "Science Fiction",
    "Fantasy",
    "Mystery",
    "Thriller",
    "Drama",
    "Adventure",
    "Crime",
    "Psychological"
]


characters = [
    "Young Scientist",
    "Detective",
    "College Student",
    "Journalist",
    "Hacker",
    "Chef",
    "Police Officer",
    "Astronaut",
    "Doctor",
    "Teacher",
    "Time Traveler",
    "Struggling Artist"
]


locations = [
    "Chennai",
    "Mumbai",
    "New York",
    "Tokyo",
    "London",
    "A Remote Village",
    "An Abandoned Hotel",
    "Mars",
    "An Underwater City",
    "A Space Station",
    "Ancient Rome",
    "A Mysterious Island"
]


conflicts = [
    "A mysterious disappearance",
    "A murder mystery",
    "An alien invasion",
    "A dangerous secret",
    "A stolen invention",
    "A time loop",
    "A supernatural curse",
    "A betrayal",
    "A race against time",
    "A missing person",
    "A mysterious disease",
    "A powerful enemy"
]


moods = [
    "Dark",
    "Funny",
    "Emotional",
    "Suspenseful",
    "Mysterious",
    "Romantic",
    "Epic",
    "Terrifying",
    "Inspirational"
]


twists = [
    "Hidden identity",
    "Unexpected betrayal",
    "The villain was right",
    "The hero is secretly responsible",
    "Time travel revelation",
    "The story happens differently than expected",
    "The character has been manipulated",
    "The apparent enemy is actually helping",
    "Completely unpredictable"
]


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header("🎥 Movie Settings")

st.sidebar.write(
    "Choose your movie ingredients or let CineGen "
    "randomly create them."
)


# Random button
random_movie = st.sidebar.button(
    "🎲 Surprise Me!"
)


# ============================================================
# RANDOM GENERATION
# ============================================================

if random_movie:

    st.session_state.genre = random.choice(genres)
    st.session_state.character = random.choice(characters)
    st.session_state.location = random.choice(locations)
    st.session_state.conflict = random.choice(conflicts)
    st.session_state.mood = random.choice(moods)
    st.session_state.twist = random.choice(twists)


# Set defaults
if "genre" not in st.session_state:
    st.session_state.genre = "Science Fiction"

if "character" not in st.session_state:
    st.session_state.character = "Young Scientist"

if "location" not in st.session_state:
    st.session_state.location = "Chennai"

if "conflict" not in st.session_state:
    st.session_state.conflict = "A mysterious disappearance"

if "mood" not in st.session_state:
    st.session_state.mood = "Suspenseful"

if "twist" not in st.session_state:
    st.session_state.twist = "Hidden identity"


# ============================================================
# INPUTS
# ============================================================

genre = st.sidebar.selectbox(
    "🎭 Genre",
    genres,
    index=genres.index(st.session_state.genre)
)


character = st.sidebar.selectbox(
    "👤 Main Character",
    characters,
    index=characters.index(st.session_state.character)
)


location = st.sidebar.selectbox(
    "🌍 Location",
    locations,
    index=locations.index(st.session_state.location)
)


conflict = st.sidebar.selectbox(
    "⚔️ Main Conflict",
    conflicts,
    index=conflicts.index(st.session_state.conflict)
)


mood = st.sidebar.selectbox(
    "🎨 Mood",
    moods,
    index=moods.index(st.session_state.mood)
)


twist = st.sidebar.selectbox(
    "😱 Plot Twist",
    twists,
    index=twists.index(st.session_state.twist)
)


# ============================================================
# STORY LENGTH
# ============================================================

story_length = st.sidebar.select_slider(
    "📖 Story Detail",
    options=[
        "Short",
        "Medium",
        "Detailed"
    ],
    value="Medium"
)


# ============================================================
# GENERATE PROMPT
# ============================================================

def create_prompt(
    genre,
    character,
    location,
    conflict,
    mood,
    twist,
    story_length
):

    prompt = f"""
You are an expert professional movie screenwriter.

Create a completely ORIGINAL movie concept.

Use these ingredients:

Genre:
{genre}

Main Character:
{character}

Location:
{location}

Main Conflict:
{conflict}

Mood:
{mood}

Plot Twist:
{twist}

Story Detail Level:
{story_length}


IMPORTANT REQUIREMENTS:

1. Create original characters.
2. Create an original story.
3. Do not copy an existing movie.
4. Make the story logically consistent.
5. Make the conflict important to the main character.
6. Make the location important to the story.
7. The plot twist should connect naturally to earlier events.
8. The ending should resolve the main conflict.
9. Make the story cinematic and entertaining.


OUTPUT FORMAT:

# 🎬 Movie Title

Create a creative movie title.


# 🏷️ Tagline

Create a short memorable tagline.


# 📝 Logline

Summarize the entire movie in 2-3 sentences.


# 👥 Main Characters

For each major character provide:

- Name
- Age
- Personality
- Goal
- Conflict
- Character arc


# 📖 Story

## Act 1 - Setup

Explain how the story begins and introduce the main characters.


## Act 2 - Rising Conflict

Explain how the main conflict develops and becomes more dangerous.


## Act 3 - Climax

Explain the major confrontation.


# 😱 Plot Twist

Explain the major twist and why it changes the story.


# 🎞️ Ending

Explain how the movie ends.


# 🎥 Trailer Description

Write a short cinematic trailer description.

"""


    return prompt


# ============================================================
# GEMINI GENERATION WITH RETRIES
# ============================================================

def generate_movie(prompt):

    # Use a model available to your Gemini API account.
    # If this model is unavailable, the error message will
    # tell you what needs to be changed.
    model_name = "gemini-3.6-flash"

    max_retries = 3

    for attempt in range(max_retries):

        try:

            response = client.models.generate_content(
                model=model_name,
                contents=prompt
            )

            return response.text

        except Exception as error:

            error_message = str(error)

            # Temporary Gemini server error
            if (
                "503" in error_message
                or "UNAVAILABLE" in error_message
                or "high demand" in error_message.lower()
            ):

                if attempt < max_retries - 1:

                    wait_time = 2 ** attempt

                    st.warning(
                        f"⚠️ Gemini is temporarily busy. "
                        f"Retrying in {wait_time} seconds..."
                    )

                    time.sleep(wait_time)

                else:

                    st.error(
                        "❌ Gemini is currently experiencing "
                        "high demand.\n\n"
                        "Please wait a little and try again."
                    )

                    return None

            else:

                st.error(
                    f"❌ Gemini API Error:\n\n{error_message}"
                )

                return None

    return None


# ============================================================
# GENERATE BUTTON
# ============================================================

st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    generate_button = st.button(
        "🎬 GENERATE MY MOVIE",
        type="primary",
        use_container_width=True
    )


# ============================================================
# GENERATE MOVIE
# ============================================================

if generate_button:

    # Save selections
    st.session_state.genre = genre
    st.session_state.character = character
    st.session_state.location = location
    st.session_state.conflict = conflict
    st.session_state.mood = mood
    st.session_state.twist = twist

    # Create prompt
    prompt = create_prompt(
        genre,
        character,
        location,
        conflict,
        mood,
        twist,
        story_length
    )

    # Display selected ingredients
    st.subheader("🎲 Your Movie Ingredients")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(f"🎭 **Genre:** {genre}")
        st.info(f"👤 **Character:** {character}")

    with col2:
        st.info(f"🌍 **Location:** {location}")
        st.info(f"⚔️ **Conflict:** {conflict}")

    with col3:
        st.info(f"🎨 **Mood:** {mood}")
        st.info(f"😱 **Twist:** {twist}")

    st.markdown("---")

    # Generate
    with st.spinner(
        "🎬 Gemini is writing your movie..."
    ):

        movie = generate_movie(prompt)

    # Display result
    if movie:

        st.success(
            "🎉 Your movie has been generated!"
        )

        st.markdown(
            '<div class="movie-box">',
            unsafe_allow_html=True
        )

        st.markdown(movie)

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        # Download button
        st.download_button(
            label="📥 Download Movie Plot",
            data=movie,
            file_name="my_movie_plot.txt",
            mime="text/plain"
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "🎬 CineGen — Turn random ideas into movie stories with AI."
)
