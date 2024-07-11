# solver/views.py

from django.shortcuts import render
from django.http import JsonResponse
import base64
import json
from .utils.equation_extractor import extract_equation_from_image
from .utils.math_solver import solve_math_equation
from .utils.determinator import determine_math_problem

def index(request):
    return render(request, 'solver/index.html')

def solve_equation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            image_data = data['image']
            image_path = "input_image.png"

            # Save the image
            with open(image_path, "wb") as f:
                f.write(base64.b64decode(image_data))

            # Extract the equation from the image
            extracted_data = extract_equation_from_image(image_path)
            equation = extracted_data.get('choices', [{}])[0].get('message', {}).get('content', '')

            # Determine the math problem category
            determinator = determine_math_problem(equation)
            if not determinator:
                return JsonResponse({"error": "No response for the given math problem."}, status=400)

            category = json.loads(determinator).get('category', '').lower()
            graphable = json.loads(determinator).get('graph', '').lower()

            # Solve the equation
            solution = solve_math_equation(equation)
            solution_data = json.loads(solution)
            steps = solution_data.get('steps', [])
            answer = solution_data.get('answer', '')

            return JsonResponse({"equation": equation, "category": category, "graphable": graphable, "steps": steps, "answer": answer})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method."}, status=405)
