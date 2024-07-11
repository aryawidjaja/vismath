import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

def determine_math_problem(equation):
    function_determine = [
        {
            "name": "math_problem_category",
            "description": "Determine the category of the given math problem.",
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": "Return the math problem category, e.g., 'addition', 'subtraction', 'multiplication', 'division', 'linear equation'."
                    },
                    "graph": {
                        "type": "string",
                        "description": "Determine is the given equation can be graphed or not. Only return 'yes' or 'no'."
                    },
                },
                "required": [
                    "category",
                    "graph"
                ]
            }
        }
    ]

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are a highly knowledgeable math teacher."
            },
            {
                "role": "user",
                "content": f"Determine the category of this math problem: {equation}"
            }
        ],
        functions=function_determine,
        max_tokens=50,
        temperature=0.5,
    )

    return completion.choices[0].message.function_call.arguments
