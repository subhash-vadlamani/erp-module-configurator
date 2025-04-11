# 🧠 ERP Module Configurator

A multimodal AI agent system using **Crew AI** that enables dynamic ERP module configuration through natural language. This project allows users to configure ERP components like Material Management, Sales & Distribution, and Payroll by answering simple questions, which are processed by Crew AI agents to trigger your custom ERP configuration APIs.

---

## 🚀 Features

- 🤖 Crew AI–powered agents for ERP automation
- 💬 Natural language interface for configuration
- 🔌 Calls backend APIs to configure ERP modules
- 🧱 Modular setup with configurable flows, agents, and tools
- 📊 Support for:
  - Material Management (MM)
  - Sales and Distribution (SD)
  - Payroll Management
  - Role-based access control

---

## 📂 Project Structure

```
erp-module-configurator/
├── agents/              # Crew AI agent definitions
├── tools/               # Tools for calling ERP APIs
├── flows/               # Agent flows per module
├── configs/             # Config templates per module
├── .env                 # Environment variables (API keys, base URLs)
├── main.py              # Entry point for the system
└── README.md            # This file
```

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/erp-module-configurator.git
cd erp-module-configurator
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Setup Environment Variables

Create a `.env` file with your secret keys:

```
OPENAI_API_KEY=your_openai_api_key
ERP_API_BASE_URL=https://your-erp-api.com
```

Make sure `.env` is added to `.gitignore`.

### 4. Run the Application

```bash
python main.py
```

---

## 🧠 Example Prompt

> "Set the reorder level for raw materials to 500 and assign all items to warehouse WH12."

The agent:
- Understands the domain (Material Management)
- Extracts intent and parameters
- Calls your configured ERP API with the correct payload

---

## 🔐 Security Notice

If you accidentally commit secrets (e.g., OpenAI keys), remove them using:

```bash
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch .env" \
  --prune-empty --tag-name-filter cat -- --all

git push origin --force
```

Then **rotate your keys** immediately.

---

## 📌 TODO

- [ ] Add unit tests for each ERP tool
- [ ] Support multi-turn interactions
- [ ] Integrate Slack/Teams chatbot interface
- [ ] Dynamic form builder for API parameter entry

---

## 👨‍💻 Author

**Subhash Vadlamani**  
📧 v.vadlamani@outlook.com  
🔗 [LinkedIn](https://linkedin.com/in/vadlamanisubhash)  
🌐 [Portfolio](https://subhash-vadlamani.github.io)

---

## 📝 License

MIT License – feel free to use, modify, and contribute!
