from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os

class StockAnalysisAgent:
    def __init__(self, model_name="llama-3.3-70b-versatile", temperature=0.7):
        self.llm = ChatGroq(
            model_name=model_name,
            api_key=os.getenv('GROQ_API_KEY'),
            temperature=temperature
        )

        self.analysis_prompt = PromptTemplate(
            input_variables=["stock_data"],
            template=(
                "You are a stock market analyst. Based on the following data, "
                "provide a detailed analysis and recommendation:\n\n{stock_data}"
            )
        )

        self.custom_prompt = PromptTemplate(
            input_variables=["analysis", "custom_query"],
            template=(
                "Here’s the detailed analysis:\n\n{analysis}\n\n"
                "Now answer this custom question: {custom_query}"
            )
        )

        self.analysis_chain = LLMChain(llm=self.llm, prompt=self.analysis_prompt)
        self.custom_chain = LLMChain(llm=self.llm, prompt=self.custom_prompt)

    def generate_analysis(self, stock_data):
        return self.analysis_chain.run(stock_data=stock_data)

    def generate_custom_insight(self, analysis, custom_query):
        return self.custom_chain.run(
            analysis=analysis,
            custom_query=custom_query
        )
