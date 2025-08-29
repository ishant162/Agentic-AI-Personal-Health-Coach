# Agentic-AI-Personal-Health-Coach

A digital health agent, powered by an LLM and deployed within each hospital or clinic, provides personalized recovery support to discharged patients. These agents are privacy-preserving, autonomous, and continuously learning across institutions using Federated Learning.

**Business Problem Being Solved**
- Current Challenges:
	- High readmission rates (especially for chronic conditions like heart disease, diabetes).
	- Lack of personalized care after discharge, leading to complications.
	- Patient non-adherence to medication or post-op care.
	- Data silos and privacy regulations prevent hospitals from sharing patient records.

**Value Delivered**
- Personalized, continuous care improves outcomes and patient satisfaction.
- FL ensures collaborative learning without violating privacy (no raw data sharing).
- AI agents automate repetitive tasks (follow-ups, reminders), saving nurse/doctor time.
- Hospitals reduce readmission penalties, and clinics can offer premium digital services.

**Technical Architechture**

<img width="2417" height="2889" alt="Health_Coach_Architechture" src="https://github.com/user-attachments/assets/d119b9a2-7e23-4695-89a2-e2ad2b35ec81" />

- Core Components:

	- Local Agentic AI:
    An LLM-powered agent deployed in each hospital, acting as the digital health companion.
	- LLMs:
    Fine-tuned models like OpenChat, LLaMA, or GPT variants (on private infrastructure).
	- Prompt Engineering:
    Used to scaffold reasoning paths, guide conversation tone, and ensure medical safety.
	- Federated Learning:
    Model updates (gradients, not patient data) shared across institutions for collective intelligence.
	- Electronic Health Record (EHR) Integration:
    Pulls in clinical data with patient consent to contextualize recommendations.
	- Mobile/Web App:
    Patient interface for interaction, alerts, vitals input, reminders.

## 🚀 Installation & Running Instructions

Follow the steps below to set up and run the project locally:

1. **Create a Python virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Mac/Linux
   venv\Scripts\activate      # On Windows

2.	**Clone the repository**
	```bash
 	git clone https://github.com/ishant162/Agentic-AI-Personal-Health-Coach.git
	cd Agentic-AI-Personal-Health-Coach

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   
4. **Create a .env file**
   Add your API key inside .env file in the project root:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
	# or
   GROQ_API_KEY=your_groq_api_key_here
   
5. **Run the app**
   ```bash
   python app.py
