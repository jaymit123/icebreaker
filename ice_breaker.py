from dotenv import load_dotenv
import os
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import person_intel_parser, PersonIntel
from third_parties.linkedin import scrape_linkedin_profile


def ice_breaker(name: str) -> [PersonIntel, str]:
    load_dotenv()
    # call linkedin agent to get url
    linkedin_profile_url = linkedin_lookup_agent(name=name)

    # prompt template with parameters added
    summary_template = """"
    given the information {information} about a person I want you to create:
    1. A Short Summary.
    2. Two Interesting facts about them
    3. A topic that may interest them
    4. 2 creative ice breakers to open a conversation with them
    \n${format_instructions}
    """
    # prompt template has input variables: string with keys we will populate with.
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )

    # create llm with tempeature 0 - (not creative) and gtp 3.5
    # chat open ai is wrapper around language model gpt-3.5
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)
    res = chain.run(information=linkedin_data)
    return [person_intel_parser.parse(res), linkedin_data.get("profile_pic_url")]


if __name__ == "__main__":
    print(ice_breaker("Jaymit Desai"))
