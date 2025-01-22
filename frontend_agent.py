from crewai import LLM, Agent, Task, Crew

# Initialize LLM
llm = LLM(
    model="gpt-4o", 
    base_url="https://openai.prod.ai-gateway.quantumblack.com/0b0e19f0-3019-4d9e-bc36-1bd53ed23dc2/v1", 
    api_key="5f393389-5fc3-4904-a597-dd56e3b00f42:7ggTi5OqYeCqlLm1PmJ9kkAVk69iWuWI" 
)


# Define the UI Monitor Agent
ui_monitor = Agent(
    role="UI Monitor",
    goal="Detect suspicious changes in the travel form's user interface.",
    backstory=(
        "You are responsible for continuously monitoring the UI of the travel booking form. "
        "Your job is to identify unauthorized changes, such as altered input fields, "
        "malicious scripts injected into the DOM, or suspicious behaviors."
    ),
    allow_delegation=False,
    llm=llm,
    verbose=True
)

# Define the Security Analyzer Agent
security_analyzer = Agent(
    role="Security Analyzer",
    goal="Analyze suspicious UI changes for potential injection attacks.",
    backstory=(
        "You evaluate detected UI anomalies to determine if they result from injection attacks "
        "or other security vulnerabilities. You analyze the changes to recommend mitigation strategies."
    ),
    allow_delegation=False,
    llm=llm,
    verbose=True
)

# Define the Mitigation Agent
mitigation_agent = Agent(
    role="Mitigation Specialist",
    goal="Prevent and mitigate risks from detected injection attacks.",
    backstory=(
        "You implement measures to prevent injection attacks and mitigate risks from suspicious UI changes. "
        "Your role includes restoring the UI to its secure state and notifying the development team."
    ),
    allow_delegation=False,
    llm=llm,
    verbose=True
)

# Define the UI Monitoring Task
ui_monitor_task = Task(
    description=(
        "1. Monitor the DOM structure of the travel booking form for unauthorized changes.\n"
        "2. Detect malicious scripts or unusual input fields.\n"
        "3. Flag suspicious behaviors, such as unrecognized event listeners or changes in CSS properties."
    ),
    expected_output="A report detailing detected UI anomalies and suspicious activities.",
    agent=ui_monitor
)

# Define the Security Analysis Task
security_analysis_task = Task(
    description=(
        "1. Analyze flagged UI anomalies to determine if they are caused by injection attacks.\n"
        "2. Identify the nature of the attack (e.g., SQL injection, XSS).\n"
        "3. Assess the impact and provide recommendations for mitigation."
    ),
    expected_output="An analysis report categorizing anomalies and their security impact.",
    agent=security_analyzer
)

# Define the Mitigation Task
mitigation_task = Task(
    description=(
        "1. Implement measures to prevent identified injection attacks.\n"
        "2. Restore the travel form's UI to its secure and original state.\n"
        "3. Notify the development team with detailed findings and recommendations for future prevention."
    ),
    expected_output="A summary of actions taken to mitigate risks and restore UI security.",
    agent=mitigation_agent
)

# Create the Crew
crew = Crew(
    agents=[ui_monitor, security_analyzer, mitigation_agent],
    tasks=[ui_monitor_task, security_analysis_task, mitigation_task]
)

# Run the Crew for Monitoring Frontend Changes
result = crew.kickoff(inputs={"topic": "Monitoring suspicious UI changes and preventing injection attacks"})

# Print Results
print(result)
