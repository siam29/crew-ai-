from crewai import LLM, Agent, Task, Crew

# Initialize the LLM (Large Language Model) for the agents
llm = LLM(
    model="gpt-4o", 
    base_url="https://openai.prod.ai-gateway.quantumblack.com/0b0e19f0-3019-4d9e-bc36-1bd53ed23dc2/v1", 
    api_key="5f393389-5fc3-4904-a597-dd56e3b00f42:7ggTi5OqYeCqlLm1PmJ9kkAVk69iWuWI" 
)


# Super Agent: Initialize and manage security agents
super_agent = Agent(
    role="AI Security Supervisor",
    goal="Initialize, monitor, and coordinate security agents to detect and respond to security threats.",
    backstory="You are responsible for initializing and managing various security agents to ensure the safety and integrity of the system.",
    allow_delegation=False,
    llm=llm,
    verbose=True
)

# Specialized Security Agent for monitoring suspicious UI changes
ui_monitoring_agent = Agent(
    role="UI Monitoring Agent",
    goal="Monitor UI changes and prevent unauthorized modifications.",
    backstory="You are tasked with watching for suspicious UI changes that could indicate a potential attack, like DOM manipulation or UI injection.",
    allow_delegation=False,
    llm=llm,
    verbose=True
)

# Specialized Security Agent for preventing injection attacks
injection_prevention_agent = Agent(
    role="Injection Prevention Agent",
    goal="Detect and prevent SQL or script injection attacks.",
    backstory="You monitor the system for signs of injection attacks (e.g., SQL, XSS), and take action to prevent malicious requests.",
    allow_delegation=False,
    llm=llm,
    verbose=True
)

# Specialized Security Agent for DOM integrity
dom_integrity_agent = Agent(
    role="DOM Integrity Agent",
    goal="Monitor and ensure the integrity of the DOM to prevent unauthorized changes.",
    backstory="You are responsible for checking the structure and integrity of the DOM, ensuring no malicious modifications occur.",
    allow_delegation=False,
    llm=llm,
    verbose=True
)



# Task for the Super Agent: Initialize and start all security agents
initialize_security_agents_task = Task(
    description="Initialize and configure all security monitoring agents.",
    expected_output="All security agents initialized and configured successfully.",
    agent=super_agent,
)

# Create the Crew with the Super Agent and specialized agents
crew = Crew(
    agents=[super_agent, ui_monitoring_agent, injection_prevention_agent, dom_integrity_agent],
    tasks=[initialize_security_agents_task]
)

# Run the Crew and monitor the security system
result = crew.kickoff(inputs={})

# Output the result
print(result)
