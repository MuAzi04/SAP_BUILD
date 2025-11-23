import google.generativeai as genai
import os

# 1. Setup your API Key
os.environ["GEMINI_API_KEY"] = "YOUR_ACTUAL_API_KEY"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# 2. Define the file path you want to read
file_path = "my_script.py"  # Replace with your file name

# 3. Read the file content
try:
    with open(file_path, "r") as file:
        file_content = file.read()
        
    # 4. Create the model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # 5. Send the content + your specific question
    prompt = f"Here is a Python file content:\n\n{file_content}\n\nCan you explain what this code does?"
    
    response = model.generate_content(prompt)
    
    print("Gemini's Response:")
    print(response.text)

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")