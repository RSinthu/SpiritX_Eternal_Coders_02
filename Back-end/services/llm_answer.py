import os
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from db.db import db_connection

# Load environment variables
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

cursor = db_connection.cursor()  # Use dictionary=True to fetch results as a dictionary

# Define query prompt
query_prompt = PromptTemplate(
    input_variables=["user_query"],
    template=""" 
    # MySQL Query Generator
    
    ## Task
    Convert the following natural language request into a precise MySQL query
    
    ## MySQL Schema (cricketers Table)
    {{
        "cricketers": {{
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            university VARCHAR(255),
            category VARCHAR(50), # Options: "Batsman", "All-Rounder", "Bowler"
            totalRuns INT,
            ballsFaced INT,
            inningsPlayed INT,
            wickets INT,
            oversBowled INT,
            runsConceded INT,
            batting_strike_rate FLOAT,
            batting_average FLOAT,
            bowling_strike_rate FLOAT,
            economy_rate FLOAT,
            points FLOAT,
            value INT
        }}
    }}
    
    ## User Request
    "{user_query}"
    
    ## Output Requirements
    1. Provide ONLY a valid MySQL query without any other words or explanations.
    2. The query should be valid SQL for answering the user's question based on the schema.
    3. Consider Schema before generating query.
    4. Do NOT include the word 'sql' or 'Generated query:'. Just provide the raw SQL query.
    5. Do NOT include comments or placeholders.
    7. If the user is asking about the highest or lowest metric, retrieve the actual value and player name associated with it.
    8. DO NOT include any words rather than raw sql query. Strictly follow this rule.
    9. IF user ask about top or best 11 players, provide the top 11 players based on points.but don't reveal the points.
    10. AGAIN DO NOT include any words rather than raw sql query.
    ## Output (MySQL query only no other words like sql):
    """
)

response_prompt = PromptTemplate(
    input_variables=["user_query", "query_results"],
    template=""" 
    The user asked: "{user_query}"
    
    Based on the following query results from the database:
    {query_results}
    
    If the user is asking about the highest or lowest metric, retrieve the actual value associated with it and select the first name from the list. Provide the answer including both the name and the corresponding value.
    If the user query and query result are irrelevant, provide a response indicating that you can't answer the question.
    If the user is asking about the top 11 players, provide the names of the players in query results.So answer the user queries based on query results.

    DO NOT reveal player's points under any circumstances.strictly follow this rule.If your ask about it provide answer about can't reveal points.
    Provide a natural language summary that directly answers the user's question.
    Keep the response conversational and highlight key insights from the data.
    """
)
# Set up chains
parser = StrOutputParser()
query_chain = query_prompt | llm | parser
response_chain = response_prompt | llm | parser

def clean_query(query):
    """Clean up the query string by removing markdown code blocks, extra whitespace, and unwanted prefixes."""
    query = query.replace("```python", "").replace("```json", "").replace("```", "").strip()
    # Remove a leading "sql" prefix (case-insensitive) if it exists
    if query.lower().startswith("sql"):
        # Remove the first line if it starts with "sql"
        if "\n" in query:
            query = query.split("\n", 1)[1].strip()
        else:
            query = query[3:].strip()
    return query

def process_user_query(user_query):
    """Process a natural language query against MySQL and return formatted results."""
    try:
        # Generate SQL query
        sql_query_str = query_chain.invoke({"user_query": user_query})
        sql_query_str = clean_query(sql_query_str)
        print(f"[DEBUG] Generated Query: {sql_query_str}")

        # Execute the query on the MySQL database
        cursor.execute(sql_query_str)
        results = cursor.fetchall()
        if not results:
            return "I don't have enough knowledge to answer that question."
        # Convert results to JSON format for easy readability
        query_results_json = json.dumps(results, indent=2)
        print(query_results_json)
        # Generate natural language response
        nl_response = response_chain.invoke({
            "user_query": user_query,
            "query_results": query_results_json
        })
        return nl_response
    except Exception as e:
        return f"Sorry, I encountered an error processing your query: {str(e)}"


# while True:
#     user_question = input("Enter the question: ")
#     result = process_user_query(user_question)
#     print(result)
#     choice = input("Do you want to continue the question(say yes/no): ")
#     if choice.lower() == "no":
#         break
