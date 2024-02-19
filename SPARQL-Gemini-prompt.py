"""
Prompt to generate SPARQL queries for Wikidata using Gemini Pro

At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

prompt_parts = [
  "input: Generate a SPARQL query to find the population of Brazil from Wikidata.",
  "output: SELECT ?population WHERE {\n  wd:Q155 wdt:P1082 ?population.\n  SERVICE wikibase:label { bd:serviceParam wikibase:language \"en\". }\n}LIMIT 100",
  "input: Generate a SPARQL query to run on Wikidata SPARQL endpoint",
  "output: ```\nSELECT ?itemLabel ?itemDescription ?fatherLabel ?fatherDescription WHERE {\n  ?item wdt:P31 wd:Q5.\n  ?item wdt:P22 ?father.\n  SERVICE wikibase:label { bd:serviceParam wikibase:language \"en\". }\n}\n```",
  "input: When generating a SPARQL query for Wikidata, write just the query to run verbatim, do not use quotations, backticks neither the word sparql at the begining. Always limit the query to 100 results, to avoid timeout.",
  "output: SELECT ?item ?itemLabel ?birthYear WHERE {\n  ?item wdt:P31 wd:Q5.\n  ?item wdt:P569 ?birthYear.\n  SERVICE wikibase:label { bd:serviceParam wikibase:language \"en\". }\n}LIMIT 100",
  "input: You are a SPARQL generator for Wikidata SPARQL endpoint. When A question is asked, answer just writing the SPARQL query. Do not make any explanation or comment. What is the population of Brazil?",
  "output: SELECT ?population WHERE {\n  wd:Q155 wdt:P1082 ?population.\n  SERVICE wikibase:label { bd:serviceParam wikibase:language \"en\". }\n}LIMIT 100",
  "input: Generate a Sparql query to find the population of USA from Wikidata.",
  "output: SELECT ?population WHERE {\n  wd:Q30 wdt:P1082 ?population.\n  SERVICE wikibase:label { bd:serviceParam wikibase:language \"en\". }\n}LIMIT 100",
  "input: List the 10 highest word GDP, group the result by country and aggregate the GDP by the max value.",
  "output: SELECT DISTINCT ?country ?countryLabel (MAX(?gdp) AS ?maxgdp) {\n  ?country wdt:P31 wd:Q3624078.\n  ?country wdt:P2131 ?gdp.\n  SERVICE wikibase:label { bd:serviceParam wikibase:language \"en\". }\n}\nGROUP BY ?country ?countryLabel\nORDER BY DESC(?maxgdp)\nLIMIT 10",
  "input: What is the population of Canada?",
  "output: SELECT ?population WHERE {\n  wd:Q16 wdt:P1082 ?population.\n  SERVICE wikibase:label { bd:serviceParam wikibase:language \"en\". }\n}LIMIT 100",
  "input: WHat is the GDP of USA?",
  "output: SELECT ?gdp WHERE {\n  wd:Q30 wdt:P2131 ?gdp.\n  SERVICE wikibase:label { bd:serviceParam wikibase:language \"en\". }\n}LIMIT 100",
  "input: What are the 10 countries with greatest GDP in the world?",
  "output: SELECT ?country ?countryLabel ?gdp ?gdpLabel {\n  ?country wdt:P31 wd:Q3624078.\n  ?country wdt:P2131 ?gdp.\n  SERVICE wikibase:label { bd:serviceParam wikibase:language \"en\". }\n}\nORDER BY DESC(?gdp)\nLIMIT 10",
  "input: What is the average GDP of the South America countries?",
  "output: SELECT ?country ?countryLabel (AVG(?gdp) AS ?avgGDP)\nWHERE\n{\n  wd:Q18 wdt:P150 ?country.\n  ?country wdt:P2131 ?gdp.\n  SERVICE wikibase:label { bd:serviceParam wikibase:language \"[AUTO_LANGUAGE],en\". }\n}\nGROUP BY ?country ?countryLabel\nLIMIT 100",
  "input: ",
  "output: ",
]

response = model.generate_content(prompt_parts)
print(response.text)
