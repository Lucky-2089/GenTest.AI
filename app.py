import os
import json
from dotenv import load_dotenv
import streamlit as st
from google.api_core.exceptions import GoogleAPIError
from google.generativeai import configure, GenerativeModel

# Load environment variables from .env
load_dotenv()

class TestDataGenerator:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")

        try:
            configure(api_key=api_key)
            self.model = GenerativeModel("gemini-2.0-flash-exp")
        except Exception as e:
            raise Exception(f"Failed to initialize Gemini model: {str(e)}")

    def generate(self, scenario, num_records):
        prompt = f"""You are a data generator. Generate exactly {num_records} realistic JSON records for the '{scenario}' scenario.

Rules:
- Return ONLY raw JSON array (no markdown, no explanation)
- Format: [{{"key1": "value1", "key2": "value2"}}, ...]
- Ensure the output is valid JSON
- Do NOT include any text outside the JSON array

Example for open_banking:
[
  {{"transaction_id": "txn_001", "amount": 100.0, "currency": "GBP"}},
  ...
]"""

        try:
            response = self.model.generate_content(
                prompt,
                generation_config={
                    "temperature": 0.5,
                    "max_output_tokens": 1024
                }
            )

            # Get only the response text
            if response and response.candidates:
                parts = response.candidates[0].content.parts
                if parts and hasattr(parts[0], "text"):
                    return self._parse_response(parts[0].text)

            raise Exception("Empty or invalid response from Gemini model")

        except GoogleAPIError as e:
            raise Exception(f"API error: {str(e)}")
        except Exception as e:
            raise Exception(f"Generation failed: {str(e)}")

    def _parse_response(self, text):
        try:
            # Clean up markdown artifacts and extra lines
            clean_text = text.strip()
            clean_text = clean_text.replace("```json", "").replace("```", "")
            clean_text = clean_text.split("\n", 1)[-1].strip() if clean_text.startswith("{") else clean_text
            return json.loads(clean_text)
        except json.JSONDecodeError as e:
            raise Exception(f"Invalid JSON response from model: {e}")

    def _parse_response(self, text):
        try:
            clean_text = text.strip().replace('```json', '').replace('```', '')
            return json.loads(clean_text)
        except json.JSONDecodeError:
            raise Exception("Invalid JSON response from model")


def main():
    st.set_page_config(page_title="GenTest.AI", page_icon="🛠️")
    st.title("🛠️ GenTest.AI - Synthetic Data Generator")

    if 'data' not in st.session_state:
        st.session_state.data = None

    with st.sidebar:
        st.header("Configuration")
        scenario = st.selectbox(
            "Select Scenario",
            ("open_banking", "kyc", "payments", "fraud_detection"),
            index=0
        )
        records = st.slider("Number of Records", 1, 100, 10)

        if st.button("🔄 Clear Cache"):
            st.session_state.data = None
            st.rerun()

    if st.button("🚀 Generate Data"):
        if not os.getenv("GEMINI_API_KEY"):
            st.error("Missing GEMINI_API_KEY in .env file")
            st.info("Create a `.env` file with your API key as: `GEMINI_API_KEY=your-key-here`")
        else:
            try:
                with st.spinner(f"Generating {records} {scenario} records..."):
                    generator = TestDataGenerator()
                    st.session_state.data = generator.generate(scenario, records)
                    st.success(f"✅ Generated {len(st.session_state.data)} records!")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.session_state.data = None

    if st.session_state.data:
        with st.expander("📊 View Data (First 5 Records)"):
            st.json(st.session_state.data[:5])

        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                label="📥 Download JSON",
                data=json.dumps(st.session_state.data, indent=2),
                file_name=f"{scenario}_data.json",
                mime="application/json"
            )
        with col2:
            if st.button("📋 Copy to Clipboard"):
                st.session_state.clipboard = json.dumps(st.session_state.data)
                st.toast("Copied to clipboard!", icon="✅")


if __name__ == "__main__":
    main()
