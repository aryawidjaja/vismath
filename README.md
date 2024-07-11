# VisMath

VisMath (Visual Math) is an AI-powered interactive digital whiteboard that reads handwritten mathematical expressions, calculates solutions, and displays the results on the screen. It even plots graphs for more complex problems! Inspired by Apple's latest iPadOS 18 Math Notes calculator, VisMath leverages the power of GPT-4o to revolutionize math problem-solving.

## Features

- **Handwriting Recognition**: Draw any math equation on the whiteboard, and our AI will interpret it.
- **Instant Calculation**: The AI processes the handwritten expression and calculates the solution.
- **Graph Plotting**: For complex problems, VisMath can plot graphs to help visualize the solution [SOON].

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML5 Canvas API, Ant Design
- **AI Model**: GPT-4o
- **Deployment**: Localhost

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/aryawidjaja/vismath.git
    cd vismath
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your OpenAI API key:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```

5. Apply migrations:
    ```sh
    python manage.py migrate
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000` to use VisMath.

## Usage

- **Draw**: Use the pen tool to draw equations on the whiteboard.
- **Erase**: Use the eraser tool to erase parts of the drawing.
- **Clear**: Use the clear button to clear the entire whiteboard.

## Contributing

Feel free to fork this repository and contribute by submitting a pull request. Any contributions are welcome!

## License

This project is licensed under the MIT License.

## Acknowledgements

- Inspired by Apple's iPadOS 18 Math Notes calculator.
- Powered by OpenAI GPT-4o.

## Contact

For any questions or suggestions, please open an issue or contact me at mutaqin.aryawjya@gmail.com.

