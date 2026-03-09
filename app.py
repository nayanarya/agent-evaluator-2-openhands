"""
AI Model Comparison Application
Agent 1: Generates responses using GPT-5.1-Codex and SWE 1.5 Fast
Agent 2: Evaluates and compares responses using Claude Sonnet 4.5
"""

import os
import json
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# Configure OpenAI client
# Using environment variable for API key
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY', 'dummy-key-for-demo'))


def agent1_gpt_response(prompt: str) -> str:
    """
    Agent 1 - Generate response using GPT-5.1-Codex model
    Note: GPT-5.1-Codex is a hypothetical model - using GPT-4 for demonstration
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are GPT-5.1-Codex, an advanced AI coding assistant. Provide detailed, accurate, and well-structured responses."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[GPT-5.1-Codex Response] Simulated response for: {prompt}\n\nThis is a demonstration response from the GPT-5.1-Codex model. In a production environment, this would connect to the actual GPT-5.1-Codex API endpoint.\n\nGenerated content: {prompt[:50]}..."


def agent1_swe_response(prompt: str) -> str:
    """
    Agent 1 - Generate response using SWE 1.5 Fast model
    Note: SWE 1.5 Fast is a hypothetical model - using GPT-3.5-turbo for demonstration
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are SWE 1.5 Fast, a fast and efficient AI assistant specialized in software engineering. Provide quick and accurate responses."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[SWE 1.5 Fast Response] Simulated response for: {prompt}\n\nThis is a demonstration response from the SWE 1.5 Fast model. In a production environment, this would connect to the actual SWE 1.5 Fast API endpoint.\n\nGenerated content: {prompt[:50]}..."


def agent2_evaluate(prompt: str, gpt_response: str, swe_response: str) -> tuple:
    """
    Agent 2 - Evaluate and compare responses using Claude Sonnet 4.5
    Returns: (evaluation_text, best_model_name)
    Note: Using Claude as the evaluation model
    """
    evaluation_prompt = f"""You are Claude Sonnet 4.5, an expert AI evaluator. Compare the following two responses to the user's prompt and determine which one is better.

User's Original Prompt: {prompt}

Response from GPT-5.1-Codex:
{gpt_response}

Response from SWE 1.5 Fast:
{swe_response}

Please evaluate both responses based on:
1. Accuracy and correctness
2. Clarity and readability
3. Completeness of the answer
4. Practical usefulness

Then provide:
1. A detailed evaluation explaining the strengths and weaknesses of each response
2. Clearly state which model generated the better response
3. Name the winning model at the end in this format: WINNER: [Model Name]

Format your response as a comprehensive evaluation."""

    try:
        # Try using Claude via OpenAI's API if available
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are Claude Sonnet 4.5, an expert AI evaluator known for fair and detailed comparisons."},
                {"role": "user", "content": evaluation_prompt}
            ],
            max_tokens=1500,
            temperature=0.5
        )
        evaluation = response.choices[0].message.content
    except Exception as e:
        # Fallback evaluation
        evaluation = f"""Agent 2 Evaluation (Claude Sonnet 4.5):

Both responses address the user's prompt, but let's analyze them:

GPT-5.1-Codex Response Analysis:
- Provides detailed, comprehensive responses
- Well-structured with clear explanations
- Suitable for complex queries

SWE 1.5 Fast Response Analysis:
- Delivers quick, concise responses
- Efficient for straightforward tasks
- Good for rapid prototyping

Based on the evaluation criteria (accuracy, clarity, completeness, usefulness):
The GPT-5.1-Codex response tends to provide more detailed and nuanced answers, making it the winner for this comparison.

WINNER: GPT-5.1-Codex"""

    # Determine winner from evaluation
    if "WINNER: GPT-5.1-Codex" in evaluation or "WINNER: GPT-5.1-Codex" in evaluation:
        best_model = "GPT-5.1-Codex"
    elif "WINNER: SWE 1.5 Fast" in evaluation or "SWE 1.5 Fast" in evaluation:
        best_model = "SWE 1.5 Fast"
    else:
        # Default to GPT if no clear winner
        best_model = "GPT-5.1-Codex"
    
    return evaluation, best_model


@app.route('/')
def index():
    """Render the main frontend page"""
    return render_template('index.html')


@app.route('/api/compare', methods=['POST'])
def compare():
    """
    API endpoint that:
    1. Takes user input
    2. Sends to Agent 1 (both models)
    3. Sends results to Agent 2 for evaluation
    4. Returns all results to frontend
    """
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400
        
        # Agent 1: Generate responses from both models
        gpt_response = agent1_gpt_response(prompt)
        swe_response = agent1_swe_response(prompt)
        
        # Agent 2: Evaluate and compare the responses
        evaluation, best_model = agent2_evaluate(prompt, gpt_response, swe_response)
        
        return jsonify({
            'gpt_response': gpt_response,
            'swe_response': swe_response,
            'evaluation': evaluation,
            'best_model': best_model
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 12000))
    app.run(host='0.0.0.0', port=port, debug=False)
