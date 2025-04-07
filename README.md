
# Buddy4U - Future Starts NOW! 📱🎓

Buddy4U is a mobile-style productivity and wellness dashboard web app built using Python and Streamlit. Designed with ASU students in mind, Buddy4U combines study tracking, exam mode, personalized insights, and an AI buddy to help users stay on top of their academic life.

---

## 🚀 Features

- **📅 Home Dashboard**  
  A clean, modern landing page that greets the user and summarizes daily progress.

- **🤖 Chatbot AI**  
  A smart assistant that chats, motivates, and notifies users when they seem to be falling behind.

- **🧠 Exam Mode**  
  A focused, distraction-free study mode to prep effectively within short timeframes.

- **📊 Insights**  
  Visual charts that break down time spent, productivity streaks, and task completion.

- **📈 Semester Wrapped**  
  An end-of-term summary of your academic journey.

- **🔔 Notification System**  
  Smart alerts from your AI buddy based on activity patterns and upcoming deadlines.

---

## 📂 Project Structure

```plaintext
📁 Buddy4U/
│
├── main.py                  # Main entry point for the app
├── Home.py                  # Dashboard and home screen UI logic
├── Chatbot_AI.py            # AI buddy logic and conversation handling
├── ExamMode.py              # Study mode layout and features
├── Insights.py              # Visualized feedback and statistics
├── SemesterWrapped.py       # Semester summary module
│
├── API.env                  # API keys or environment configurations (not tracked by Git)
├── .gitignore               # Files and folders to ignore in version control
├── .replit                  # Replit app configuration
├── replit.nix               # Replit environment setup
├── requirements.txt         # Python dependencies
├── pyproject.toml           # Optional project metadata
├── generated-icon.png       # App icon
```

---

## 🛠 Installation

To run the app locally:

```bash
# Clone the repository
git clone <your-repo-url>
cd Buddy4U

# Install dependencies
pip install -r requirements.txt

# Start the app
streamlit run main.py
```

Or run it online using [Replit](https://replit.com/) with the provided `.replit` and `replit.nix` configuration.

---

## 📦 Dependencies

- `streamlit`
- `openai`
- `matplotlib` or `plotly`

All required packages are listed in `requirements.txt`.

---

## 🔐 Configuration

Create a `.env` or `API.env` file with your API keys, for example:

```env
OPENAI_API_KEY=your-openai-api-key-here
```

---

## 👥 Authors

Developed by a passionate team of students for the **ASU Principled Innovation Hackathon 2025**:

- **Lead Dev:** Aruzhan Suimbayeva  
- **AI Integration Dev:** Aryan Purohit  
- **Characters/Drawings:** Rex Pugh  
- **Research/UI Design:** Zoshan Sharifi  
- **Presentation/Design:** Chiara Moore  

---

🧡 *Future Starts NOW — Let Buddy4U guide your success!*
