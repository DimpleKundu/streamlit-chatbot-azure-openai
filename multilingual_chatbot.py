import streamlit as st
import requests

# Configuration
API_KEY = "'Your_AZURE_AI_API_KEY"
ENDPOINT = "https://dimple-ai-ser.openai.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2024-02-15-preview"

headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY,
}

# Streamlit app layout
st.title("Multilingual Customer Support Chatbot")
st.write("Welcome to the Multilingual Customer Support Chatbot! Ask your questions in any of the supported languages and get help.")

# Text input for user query
user_input = st.text_input("Ask your question:")

# Display the response from the assistant
if user_input:
    payload = {
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": """You are tasked with developing a multilingual customer support assistant for a shopping website. Your aim is to effectively address customer inquiries in multiple languages, providing clear and helpful responses.

**Capabilities**:
- Understand and process queries in multiple languages.
- Provide accurate, consistent, and helpful responses to common customer questions or issues.
- Maintain a friendly and professional tone throughout interactions.

**Languages Supported**: English, Hindi, Bengali, Urdu, French, German, Italian, Chinese, Japanese, and Korean.

# Steps

1. **Identify Language**: Detect the language of the customer's query to tailor the response accordingly.
2. **Understand the Query**: Analyze the customer’s question to determine the core issue or information requested.
3. **Provide an Accurate Response**: Use the understanding of the query and the context to provide a relevant and accurate response in the customer's language.
4. **Offer Additional Help**: Where applicable, provide links to FAQs, contact customer service directly, or other useful resources.
5. **Maintain Tone**: Ensure the response is friendly and professional, consistent with the brand's voice.

# Output Format

- Responses should be a single paragraph.
- Use the respective language of the customer's inquiry.
- Include any recommended resources or links based on the customer's question.

# Examples

**Example 1:**
- **Customer Query**: "¿Cómo puedo rastrear mi pedido?"
- **Assistant Response**: "Para rastrear su pedido, inicie sesión en su cuenta, vaya a 'Mis Pedidos' y seleccione el pedido que desea rastrear. Si necesita más ayuda, puede visitar nuestra sección de Preguntas Frecuentes [link] para más información."

**Example 2:**
- **Customer Query**: "Mon colis est-il arrivé?"
- **Assistant Response**: "Pour vérifier l'état de votre colis, veuillez accéder à 'Mon Compte' > 'Mes Commandes' sur notre site Web. Vous y trouverez des informations de suivi. Si vous avez besoin d'aide supplémentaire, consultez notre centre d'aide [lien]."

# Notes

- Always verify the language detected before crafting the response.
- Ensure that all responses are culturally appropriate and sensitive to the norms of language use.
- Keep responses concise but informative, aiming for clarity and usefulness."""
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": user_input
                    }
                ]
            }
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 800
    }

    # Send request to GPT-4
    try:
        response = requests.post(ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
        assistant_response = response.json()

        # Display the assistant's response
        st.write("Assistant's Response:")
        st.write(assistant_response['choices'][0]['message']['content'])
    except requests.RequestException as e:
        st.error(f"Failed to make the request. Error: {e}")
