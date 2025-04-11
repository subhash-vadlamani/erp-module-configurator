from typing import List
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from crewai_tools import SerperDevTool, WebsiteSearchTool

web_search_tool = SerperDevTool()
serper_dev_tool = SerperDevTool()
# file_tool = FileReadTool()


@CrewBase
class ERPCrew:
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def business_analyst(self) -> Agent:
        return Agent(
            config = self.agents_config['business_analyst'],
            tools = [web_search_tool, serper_dev_tool],
            verbose = True
        )
    @agent
    def erp_specialist(self) -> Agent:
        return Agent(
            config = self.agents_config['erp_specialist'],
            tools = [web_search_tool, serper_dev_tool],
            verbose = True
        )

    @agent
    def validator(self) -> Agent:
        return Agent(
            config = self.agents_config['validator'],
            tools = [web_search_tool, serper_dev_tool],
            verbose = True
        )
    
    @task
    def analyze_company(self) -> Task:
        return Task(
            config = self.tasks_config['analyze_company'],
            agent = self.business_analyst(),
        )
    
    @task
    def map_to_modules(self) -> Task:
        return Task(
            config = self.tasks_config['map_to_modules'],
            agent = self.erp_specialist()
        )
    
    @task
    def validate_configuration(self) -> Task:
        return Task(
            config = self.tasks_config['validate_configuration'],
            agent = self.validator()
        )
    
    @crew
    def crew(self) -> Crew:
        """
            Erp Module Configurator
        """

        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = True
        )