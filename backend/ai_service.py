import json

class AIExplainer:
    """Mock AI service for code explanation. Can be swapped with OpenAI API."""
    
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.use_openai = api_key is not None
    
    def explain_code(self, code):
        """Explain what the given Python code does."""
        if self.use_openai:
            return self._explain_with_openai(code)
        else:
            return self._explain_mock(code)
    
    def _explain_mock(self, code):
        """Mock explanation for demo purposes."""
        lines = code.strip().split('\n')
        explanation = "Code Analysis:\n\n"
        
        for i, line in enumerate(lines, 1):
            line = line.strip()
            if line.startswith('print'):
                explanation += f"Line {i}: Prints output to the console\n"
            elif line.startswith('for'):
                explanation += f"Line {i}: Starts a loop iteration\n"
            elif line.startswith('if'):
                explanation += f"Line {i}: Conditional statement\n"
            elif '=' in line and not line.startswith('#'):
                explanation += f"Line {i}: Variable assignment\n"
            elif line.startswith('#'):
                explanation += f"Line {i}: Comment\n"
        
        return explanation
    
    def _explain_with_openai(self, code):
        """Explain code using OpenAI API (requires API key)."""
        try:
            import openai
            openai.api_key = self.api_key
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful Python tutor for K-12 students."},
                    {"role": "user", "content": f"Please explain this Python code in simple terms:\n\n{code}"}
                ],
                max_tokens=500
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"Error calling OpenAI: {str(e)}"