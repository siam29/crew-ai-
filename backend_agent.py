from crewai import Crew, Agent, Task

# Define the agent
backend_agent = Agent(
    name="Backend Monitor",
    description="Monitors backend for unusual access patterns and prevents injection attacks.",
    model="gpt-4",
    tools=[]
)

# Define tasks for the agent
backend_tasks = [
    Task(
        name="Monitor Data Access",
        description="Monitor backend for unusual data access patterns.",
        agent=backend_agent
    ),
    Task(
        name="Detect Injection Attacks",
        description="Detect and prevent SQL or code injection attacks.",
        agent=backend_agent
    )
]

# Initialize the Crew object
crew = Crew(
    name="Backend Agent",
    description="An agent for monitoring backend activities and preventing injection attacks.",
    version="1.0",
    agents=[backend_agent],
    tasks=backend_tasks
)

# Run the agent
result = crew.kickoff(inputs={"topic": "Monitor and prevent suspicious activities in the backend"})
print(result)
