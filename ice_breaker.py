from dotenv import load_dotenv
import os
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    load_dotenv()
    linkedin_profile_url=linkedin_lookup_agent(name="Jaymit Desai")

    # prompt template with parameters added
    summary_template = """"
    given the information {information} about a person I want you to create:
    1. A Short Summary.
    2. Two Interesting facts about them
    """
    # prompt template has input variables: string with keys we will populate with.
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # create llm with tempeature 0 - (not creative) and gtp 3.5
    # chat open ai is wrapper around language model gpt-3.5
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)
    res = chain.run(information=linkedin_data)
    print(res)
