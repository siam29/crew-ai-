# Warning control
import warnings
warnings.filterwarnings('ignore')


from crewai import LLM, Agent, Task, Crew
from IPython.display import Markdown


llm = LLM(
    model="gpt-4o", 
    base_url="https://openai.prod.ai-gateway.quantumblack.com/0b0e19f0-3019-4d9e-bc36-1bd53ed23dc2/v1", 
    api_key="5f393389-5fc3-4904-a597-dd56e3b00f42:7ggTi5OqYeCqlLm1PmJ9kkAVk69iWuWI" 
)


# Define the Detector Agent
detector = Agent(
    role="Anomaly Detector",
    goal="Monitor and detect unusual access patterns in travel data.",
    backstory=(
        "You are responsible for analyzing logs of access to travel data, "
        "identifying patterns that deviate from normal behavior, "
        "and flagging potentially suspicious activity."
    ),
    allow_delegation=False,
    llm=llm,
    verbose=True
)

# Define the Analyzer Agent
analyzer = Agent(
    role="Anomaly Analyzer",
    goal="Analyze flagged anomalies to determine their cause and risk level.",
    backstory=(
        "You are responsible for examining flagged anomalies to assess their nature. "
        "You identify whether the anomaly is a false positive or a genuine security threat."
    ),
    allow_delegation=False,
    llm=llm,
    verbose=True
)

# Define the Responder Agent
responder = Agent(
    role="Incident Responder",
    goal="Respond to verified anomalies and mitigate potential threats.",
    backstory=(
        "You are responsible for taking appropriate action in response to verified anomalies. "
        "This includes notifying the security team, restricting access, or mitigating any identified risks."
    ),
    allow_delegation=False,
    llm=llm,
    verbose=True
)

# Define the Detection Task
detect_task = Task(
    description=(
        "1. Review access logs to identify unusual patterns of access to travel data.\n"
        "2. Use statistical methods and predefined thresholds to detect anomalies.\n"
        "3. Flag suspicious activities and prepare them for analysis."
    ),
    expected_output="A report of flagged anomalies with details of the suspicious activity.",
    agent=detector
)

# Define the Analysis Task
analyze_task = Task(
    description=(
        "1. Examine the flagged anomalies to assess their cause.\n"
        "2. Determine whether each anomaly is a false positive or a genuine threat.\n"
        "3. Provide a risk level assessment for each verified anomaly."
    ),
    expected_output="A detailed analysis report categorizing anomalies with their risk levels.",
    agent=analyzer
)

# Define the Response Task
respond_task = Task(
    description=(
        "1. Take appropriate actions for verified anomalies.\n"
        "2. Notify the relevant security team for high-risk activities.\n"
        "3. Implement mitigation measures such as restricting access or locking accounts if needed."
    ),
    expected_output="A response plan and actions taken to mitigate the identified risks.",
    agent=responder
)

# Create the Crew
crew = Crew(
    agents=[detector, analyzer, responder],
    tasks=[detect_task, analyze_task, respond_task]
)

# Run the Crew for Monitoring Travel Data Access
result = crew.kickoff(inputs={"topic": "Monitoring unusual access to travel data"})

# Print Results
print(result)