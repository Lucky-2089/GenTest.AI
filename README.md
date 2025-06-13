# 🛠️ GenTest.AI - Synthetic Test Data Generator (Powered by Gemini)

GenTest.AI is an enterprise-grade synthetic data generation platform designed for QA engineers, developers, and data scientists. It uses **Google Gemini 1.5 / 2.0 Flash** to dynamically generate realistic, schema-aligned, production-ready test data—tailored to your use case, in seconds.

Built using [Streamlit](https://streamlit.io) and [Google Generative AI](https://ai.google), it ensures quality, privacy, and scale for internal testing and AI prototyping.

---

## 🎯 Features

- ✅ Realistic test data generation using Gemini AI
- 🔒 No third-party storage — everything runs securely on your machine
- 🧠 Scenario-specific intelligent prompt tuning (e.g. KYC, payments, fraud, open banking)
- 📥 One-click download or copy of clean JSON data
- ⚙️ Lightweight UI built in Streamlit
- 🧪 Ideal for QA, sandbox testing, and ML prototyping
- 🧬 Schema-free, bias-controlled generation
- 🚀 Gemini 1.5 Flash or 2.0 Flash support for blazing-fast results

---

## ⚙️ Installation & Run Guide

> 🐍 Requires **Python 3.10+**  
> 🧪 Tested on **Windows**, **macOS**, and **Linux**

```bash
# 1. Clone this repository
git clone https://github.com/YOUR_USERNAME/GenTest-AI.git
cd GenTest-AI

# 2. Create and activate a virtual environment
python -m venv venv

# For Windows
venv\Scripts\activate

# For macOS/Linux
source venv/bin/activate

# 3. Install required packages
pip install -r requirements.txt

# 4. Set up Gemini API key
# Create a `.env` file in the root directory:
GEMINI_API_KEY=your-google-gemini-api-key-here

# 5. Run the app
streamlit run app.py
Then open http://localhost:8501 in your browser.

🧪 Supported Scenarios
Scenario	Description
open_banking	Simulated transaction-level banking data
kyc	Identity verification test records
payments	Payment processing and remittance simulation
fraud_detection	Suspicious activity for fraud detection models

💡 Why GenTest.AI?
🧬 Data Privacy: Generate 100% synthetic data — no real customer data ever used.

🧪 QA Velocity: Automate test data generation instead of crafting manually.

⚡ CI/CD Integration: Embed into GitHub Actions or Jenkins pipelines.

🛡️ Regulatory Ready: Avoid GDPR, PCI-DSS violations by using synthetic data.

🧠 AI Aligned: Ready for LLM fine-tuning and model testing.

🎯 Business Use-case Focused: Covers critical banking/fintech domains.

📊 Output Flexibility: JSON-first output for use in Postman, JMeter, etc.

🏦 Built for Banks: Created at Lloyds Bank GenAI Hackathon with enterprise in mind.

📈 Roadmap
 Add support for CSV, Parquet, SQL output

 Schema validator & JSON Schema inference

 Admin UI to save templates and scenarios

 LangChain and Vertex AI pipeline integrations

📁 Project Structure
bash
Copy
Edit
GenTest-AI/
├── app.py                # Streamlit UI
├── .env.example          # Sample environment config
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── .gitignore            # Ignore venv, cache, etc.
└── venv/                 # Local environment (ignored)




🤝 Contribution
Want to improve GenTest.AI or add new scenarios?
Feel free to fork and submit a pull request. For major changes, please open an issue first to discuss.

🛡️ License
This project is licensed under the MIT License — free to use, modify, and distribute.

🧠 Maintainers
Built with ❤️ by the Lloyds Bank QA Innovation Team for the 2025 GenAI Hackathon
Maintainer: @laxmantelang













