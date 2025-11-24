from pydantic import BaseModel, Field

class CountryInput(BaseModel):
    country: str = Field(description="The country to get information about.")

class CapitalInfoOutput(BaseModel):
    country: str = Field(description="The country to get information about.")
    capital: str = Field(description="The capital city of the country.")

from google.adk.agents import Agent

root_agent = Agent(
    name="country_agent",
    model="gemini-2.5-flash",
    input_schema=CountryInput,
    output_schema=CapitalInfoOutput,
    output_key="capital_info",
)
