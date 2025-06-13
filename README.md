# 🛠️ GenTest.AI - Synthetic Test Data Generator (Powered by Gemini)

GenTest.AI is an enterprise-grade synthetic data generation platform designed for QA engineers, developers, and data scientists. It uses **Google Gemini 1.5 / 2.0 Flash** to dynamically generate realistic, schema-aligned, production-ready test data—tailored to your use case, in seconds.

Built using [Streamlit](https://streamlit.io) and [Google Generative AI](https://ai.google), it ensures quality, privacy, and scale for internal testing and AI prototyping.

---

## 🎯 Features

- ✅ **Realistic test data** generation using Gemini AI
- 🔒 No third-party storage — everything runs securely on your machine
- 🧠 Intelligent prompt tuning for use-case accuracy (e.g. KYC, payments, fraud, open banking)
- 📥 Downloadable and copyable JSON output
- ⚙️ Scenario-specific config (amount, ID formats, etc.)
- 💡 Extensible for ML training, QA automation, or sandboxing

---

## 📦 Installation

> Tested with **Python 3.10+** on Windows, macOS, and Linux.

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/GenTest-AI.git
cd GenTest-AI

📁 2. Create and Activate a Virtual Environment
bash
Copy
Edit
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
📥 3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔐 4. Configure Environment Variables
Create a .env file in the root directory:

dotenv
Copy
Edit
GEMINI_API_KEY=your-google-gemini-api-key-here
✅ If you don’t have an API key yet, get one here.

🚀 How to Run the App
bash
Copy
Edit
streamlit run app.py
Then open the link (usually http://localhost:8501) in your browser.

🧪 Supported Scenarios
Scenario	Description
open_banking	Simulated transaction-level banking data
kyc	Identity verification test records
payments	Payment processing and remittance data
fraud_detection	Suspicious activity patterns

💡 Why GenTest.AI?
🧬 Data Privacy: Generate test data without using production data

🧪 QA Velocity: Eliminate manual test case authoring

🔗 CI/CD Friendly: Easily scriptable and GitHub Actions-compatible

🛡️ Regulatory Ready: Avoids data privacy violations (GDPR, etc.)

📈 Roadmap
 Add support for CSV export

 Prompt auto-validation & schema enforcement

 Admin dashboard for saved templates

 LangChain or Vertex AI pipeline support

🤝 Contribution
Pull requests are welcome! Please submit an issue first for any major change.

🛡️ License
This project is licensed under the MIT License.

🧠 Maintainers
Developed with ❤️ for internal use at Lloyds Bank (GenAI Hackathon)
Maintained by: @laxmantelang

yaml
Copy
Edit

---

### 📁 Final Output

Make sure these files exist in your root folder:

