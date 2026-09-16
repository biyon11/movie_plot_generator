🎬 CineGen — AI Movie Plot Generator

CineGen is an AI-powered movie plot generator built with Python, Streamlit, and Google Gemini.

The application allows users to provide different movie ingredients such as genre, main character, location, conflict, mood, and plot twist. CineGen sends these inputs to a Gemini language model, which generates an original movie concept with characters, story structure, climax, plot twist, ending, and trailer description.

Users can also use the "Surprise Me!" feature to randomly combine movie elements and generate unique story ideas.

✨ Features

🎭 Select a movie genre

👤 Select a main character

🌍 Select a movie location

⚔️ Select the main conflict

🎨 Select the story mood

😱 Select a plot twist

🎲 Generate random movie combinations

🤖 Generate movie plots using Google Gemini

📝 Generate structured movie stories

🎬 Generate movie titles and taglines

👥 Generate main characters

📖 Generate a three-act story

😱 Generate a plot twist

🎞️ Generate an ending and trailer description

📥 Download the generated movie plot as a text file

🛠️ Technologies Used
Technology	Purpose
Python	Application logic
Streamlit	Web interface
Google Gemini	AI story generation
Google GenAI SDK	Communication with Gemini API
python-dotenv	Environment variable management
📁 Project Structure
movie_plot_generator/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md

File Description

app.py

Contains the main Streamlit application, user interface, movie-generation logic, prompt creation, and Gemini API integration.

.env

Stores the Gemini API key securely.

.gitignore

Prevents sensitive files such as .env from being uploaded to GitHub.

requirements.txt

Contains the Python packages required to run the project.

README.md

Contains project documentation and setup instructions.

⚙️ Requirements

Before running the project, make sure you have:

Python 3.10 or newer

VS Code

Internet connection

A Google Gemini API key

🚀 Installation
1. Clone or download the project

Open the project folder in VS Code.

2. Create a virtual environment

Windows:

python -m venv venv


Activate it:

venv\Scripts\activate


macOS/Linux:

python3 -m venv venv


Activate it:

source venv/bin/activate

3. Install dependencies

Run:

pip install -r requirements.txt


If you don't have requirements.txt yet, install the packages directly:

pip install streamlit google-genai python-dotenv

🔑 Gemini API Configuration

Create a file named:

.env


inside the project folder.

Add your Gemini API key:

GEMINI_API_KEY=your_actual_api_key_here


Replace your_actual_api_key_here with your own API key.

⚠️ Security

Never share your API key publicly.

Do not upload .env to GitHub.

Your .gitignore should contain:

.env
__pycache__/
*.pyc

▶️ Running the Application

After installing the dependencies and configuring your API key, run:

streamlit run app.py


Streamlit will start a local web server.

Open the URL displayed in the terminal, usually:

http://localhost:8501

🎬 How CineGen Works

The application follows this process:

                USER
                  │
                  ▼
        ┌──────────────────┐
        │ Movie Preferences │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │  Python Program  │
        │                  │
        │ Builds Prompt    │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │   Gemini LLM     │
        │                  │
        │ Story Generation │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ Generated Movie  │
        └──────────────────┘

🎲 Surprise Me Feature

The application includes a random generation feature.

When the user clicks "🎲 Surprise Me!", Python randomly selects:

Genre
   +
Character
   +
Location
   +
Conflict
   +
Mood
   +
Plot Twist


For example:

Genre: Horror
Character: Chef
Location: Mars
Conflict: Missing Person
Mood: Dark
Plot Twist: Hidden Identity


These ingredients are then sent to Gemini, which creates a movie plot based on the combination.

📖 Generated Movie Format

CineGen asks Gemini to generate the movie using a structured format:

🎬 Movie Title

🏷️ Tagline

📝 Logline

👥 Main Characters

📖 Story

    Act 1 - Setup

    Act 2 - Rising Conflict

    Act 3 - Climax

😱 Plot Twist

🎞️ Ending

🎥 Trailer Description

🧠 Example
Input
Genre: Science Fiction

Main Character: Young Scientist

Location: Chennai

Main Conflict: A mysterious disappearance

Mood: Suspenseful

Plot Twist: Hidden Identity

Output

The AI generates an original movie concept containing:

Movie title

Tagline

Logline

Character profiles

Act 1

Act 2

Act 3

Major conflict

Plot twist

Ending

Trailer description

🔄 Error Handling

CineGen includes basic error handling for temporary Gemini API problems.

For example, if Gemini temporarily returns a 503 UNAVAILABLE response, the application automatically retries the request.

Gemini Request
      │
      ▼
   Success? ───── Yes ────> Show Movie
      │
      No
      │
      ▼
   Wait and Retry
      │
      ▼
   Try Again

🎯 Project Objective

The main objective of CineGen is to demonstrate how a Large Language Model can be integrated into an interactive application to perform creative text generation.

The project combines:

User input processing

Randomized content generation

Prompt engineering

Large Language Models

API integration

Structured text generation

Interactive UI development

🔮 Future Improvements

Possible future versions could include:

🎭 Advanced character generation

🎞️ Scene-by-scene generation

💬 Automatic dialogue generation

😱 Advanced plot twist generation

🔀 Multiple alternate endings

🎬 Sequel generation

🖼️ AI-generated movie posters

🎵 AI-generated soundtrack concepts

🧠 Character memory

📚 Story memory

💾 Save generated movies

👥 Multiple-user support

⭐ User rating system

📊 Automatic story evaluation

📌 Future Architecture

A more advanced version could use:

                  Streamlit UI
                       │
                       ▼
                Python Backend
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Prompt       Story        Character
       Manager      Manager       Manager
          │            │            │
          └────────────┼────────────┘
                       ▼
                  Gemini LLM
                       │
                       ▼
                Generated Story
                       │
              ┌────────┴────────┐
              ▼                 ▼
           Database          User Interface

👨‍💻 Project Type

Domain: Artificial Intelligence / Generative AI

Project: AI Movie Plot Generator

Model: Google Gemini

Programming Language: Python

Framework: Streamlit

📜 Disclaimer

CineGen is an experimental generative-AI application designed for creative storytelling and educational purposes.

Generated stories are AI-generated and may contain fictional or inaccurate information. The application should not be used as a source of factual information about real people, events, or movies.

🎬 CineGen

Turn random ideas into movie stories with AI. 🍿
<img width="1290" height="651" alt="Screenshot from 2026-09-16 15-28-40" src="https://github.com/user-attachments/assets/2daf4f3d-7d09-47dc-912d-8d31c7ec851c" />
