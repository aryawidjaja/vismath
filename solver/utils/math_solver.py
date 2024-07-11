from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

def solve_math_equation(equation):
    function_calculation = [
        {
            "name": "calculate",
            "description": "Act as a math teacher, solve the given math problem.",
            "parameters": {
                "type": "object",
                "properties": {
                    "answer": {
                        "type": "string",
                        "description": "Return only the result, e.g. '10'."
                    },
                    "steps": {
                        "type": "array",
                        "description": "Show all the steps to get that answer, but only return the mathematical steps, don't include any words, e.g. '5x = 10 - 5'. IMPORTANT: Do not rewrite the equation as step 1, just start at step 2.",
                        "items": {
                            "type": "string"
                        }
                    }
                },
                "required": [
                    "answer",
                    "steps"
                ]
            }
        }
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "Act as you are a very talented math tutor"
                },
                {
                    "role": "user",
                    "content": f"Solve the following math equation and provide the steps: {equation}"
                }
            ],
            functions=function_calculation,
            max_tokens=4096,
            temperature=0.5
        )
        answer = response.choices[0].message.function_call.arguments
        if answer:
            return answer
    except Exception as e:
        print(f"The equation does not require answer. {e}")
    return json.dumps({"answer": "", "steps": [""]})
