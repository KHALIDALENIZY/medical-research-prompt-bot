
import streamlit as st

st.title("Medical Research Prompt Generator")

research_topic = st.text_input("Research Topic", "Efficacy of SGLT2 inhibitors in CKD patients to reduce cardiovascular mortality")
population = st.text_input("Population (P)", "Adult diabetic patients with CKD stages 3-4")
intervention = st.text_input("Intervention (I)", "SGLT2 inhibitors")
comparison = st.text_input("Comparison (C)", "Placebo or other antidiabetic agents")
outcome = st.text_input("Outcome (O)", "Cardiovascular mortality, hospitalization, CKD progression")
study_types = st.multiselect("Study Types", ["systematic reviews", "meta-analyses", "RCTs"], default=["systematic reviews", "meta-analyses", "RCTs"])
publication_year_limit = st.slider("Publication Year Limit (years)", 1, 10, 5)
preferred_sources = st.multiselect("Preferred Sources", ["PubMed", "Cochrane Library", "Guidelines"], default=["PubMed", "Cochrane Library", "Guidelines"])
output_format = st.selectbox("Output Format", ["bullet points", "detailed report", "table"])

if st.button("Generate Prompt"):
    prompt = f"""
Act as a clinical researcher specialized in evidence-based medicine. I need you to conduct a structured literature review on the following topic:

**Research Topic:** {research_topic}

Use the PICO framework:
- **Population (P):** {population}
- **Intervention (I):** {intervention}
- **Comparison (C):** {comparison}
- **Outcome (O):** {outcome}

**Instructions:**
1. Retrieve evidence from the following study types: {', '.join(study_types)}.
2. Only include studies published within the last {publication_year_limit} years.
3. Prefer references from: {', '.join(preferred_sources)}.
4. Provide references with PubMed links or DOI.
5. Present the findings in {output_format}.
6. Summarize key conclusions and highlight gaps in current research.

Optional: If applicable, suggest potential future research directions.
"""

    st.text_area("Generated Prompt", prompt, height=400)

st.markdown("---")
st.markdown("Developed by Khalid Al — Medical Research Prompt Bot")
