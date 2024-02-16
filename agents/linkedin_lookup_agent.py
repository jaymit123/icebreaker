from langchain_openai import ChatOpenAI
from langchain import PromptTemplate
from langchain.agents import initialize_agent, Tool, AgentType

from tools.tools import get_profile_url


def lookup(name: str) -> str:
    # agent creation
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """
    Given the full name {name_of_person} I want you to get me a link to their linkedin profile page.
    Your answer should contain only a URL.
    """
    tools_for_agent = [
        Tool(
            name="Crawl Google for Linkedin Profile Page",
            func=get_profile_url,
            description="useful for when you need to get the linkedin profile",

        )
    ]
    agent = initialize_agent(
        tools_for_agent, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    #giving agent a prompt template with linkedin search name
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    linkedin_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))
    return linkedin_profile_url
