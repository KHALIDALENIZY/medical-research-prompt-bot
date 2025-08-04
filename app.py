import streamlit as st
import random

st.title("Medical Research Prompt Generator")

# Research Question Generator
def generate_research_question():
    conditions = ["chronic kidney disease", "heart failure", "diabetes mellitus", "hypertension", "sepsis"]
    interventions = ["SGLT2 inhibitors", "ACE inhibitors", "beta-blockers", "early goal-directed therapy", "continuous renal replacement therapy"]
    outcomes = ["mortality reduction", "hospitalization rates", "renal function preservation", "cardiac remodeling", "infection control"]

    population = f"Patients with {random.choice(conditions)}"
    intervention = random.choice(interventions)
    outcome = random.choice(outcomes)

    question = f"What is the efficacy of {intervention} in {population} regarding {outcome}?"
    return population, intervention, "Placebo or standard care", outcome, question

if st.button("Generate Random Research Question"):
    population, intervention, comparison, outcome, research_topic = generate_research_question()
    st.session_state["population"] = population
    st.session_state["intervention"] = intervention
    st.session_state["comparison"] = comparison
    st.session_state["outcome"] = outcome
    st.session_state["research_topic"] = research_topic

# Input Fields
research_topic = st.text_input("Research Topic", st.session_state.get("research_topic", ""))
population = st.text_input("Population (P)", st.session_state.get("population", ""))
intervention = st.text_input("Intervention (I)", st.session_state.get("intervention", ""))
comparison = st.text_input("Comparison (C)", st.session_state.get("comparison", ""))
outcome = st.text_input("Outcome (O)", st.session_state.get("outcome", ""))
study_types = st.multiselect("Study Types", ["systematic reviews", "meta-analyses", "RCTs"], default=["systematic reviews", "meta-analyses", "RCTs"])
publication_year_limit = st.slider("Publication Year Limit (years)", 1, 10, 5)
preferred_sources = st.multiselect("Preferred Sources", ["PubMed", "Cochrane Library", "Guidelines"], default=["PubMed", "Cochrane Library", "Guidelines"])
output_format = st.selectbox("Output Format", ["bullet points", "detailed report", "table"])

# Generate PubMed Search Query
def generate_pubmed_query(population, intervention, comparison, outcome):
    query_parts = []
    if population:
        query_parts.append(f"({population})")
    if intervention:
        query_parts.append(f"({intervention})")
    if comparison:
        query_parts.append(f"({comparison})")
    if outcome:
        query_parts.append(f"({outcome})")
    return " AND ".join(query_parts)

if st.button("Generate Prompt & PubMed Query"):
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

    pubmed_query = generate_pubmed_query(population, intervention, comparison, outcome)

    st.subheader("Generated Research Prompt")
    st.text_area("Prompt", prompt, height=400)

    st.subheader("Generated PubMed Search Query")
    st.code(pubmed_query, language="text")

st.markdown("---")
st.markdown("Developed by Khalid Al — Medical Research Prompt Bot")
