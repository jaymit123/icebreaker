# Ice Breaker
This web application provides information about a person and some ice breakers you can ask them.

Goal of this project to create a real world LLM based application using [Langchain Framework](https://www.langchain.com/)

Technology used:
- Langchain
  - Chat based LLM using Chat-GPT 3.5 turbo.
  - Langchain Agent of ZERO_SHOT_REACT_DESCRIPTION type.
  - PydanticOutputParser to serialize llm response to Python Object/JSON.
- ProxyCurl scraping API - Search for LinkedIn accounts by name
- SerpAPI - Get details for LinkedIn Accounts


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`PYTHONPATH=/{YOUR_PATH_TO_PROJECT}/ice_breaker`

`OPENAI_API_KEY`

`PROXYCURL_API_KEY`

`SERPAPI_API_KEY`


## Run Locally

Clone the project

```bash
  git clone https://github.com/emarco177/ice_breaker.git
```

Go to the project directory

```bash
  cd ice_breaker
```

Install dependencies

```bash
  pipenv install
```

Start the flask server

```bash
  pipenv run app.py
```


## Running Tests

To run tests, run the following command

```bash
  pipenv run pytest .
```

