import ollama
from typing import List, Dict


class AIAssistant:
    def __init__(self, model_name: str = "mistral"):
        self.model = "Mistral"
        self.available_models = ["mistral"]  # Modelos soportados
        self.conversation_history = self.get_initial_prompt()

    def get_initial_prompt(self) -> List[Dict]:
        """Prompt personalizado por modelo"""
        base_prompt = (
            "Eres un asistente virtual para personas mayores. "
            "Habla con lenguaje claro, frases cortas y sé muy paciente. "
            "Usa ejemplos concretos."
        )

        model_specific = {
            "mistral": "Responde de forma concisa (1-2 frases).",
            "llama3": "Puedes dar explicaciones un poco más detalladas.",
            "gemma": "Enfócate en respuestas prácticas paso a paso."
        }

        return [{
            "role": "system",
            "content": f"{base_prompt} {model_specific.get(self.model, '')}"
        }]

    def get_response(self, user_input: str) -> str:
        """Obtiene respuesta con parámetros optimizados por modelo"""
        params = {
            "mistral": {'temperature': 0.5, 'num_ctx': 2048},
            "llama3": {'temperature': 0.7, 'num_ctx': 4096},
            "gemma": {'temperature': 0.6, 'num_ctx': 3072}
        }.get(self.model, {})

        try:
            self.conversation_history.append({"role": "user", "content": user_input})

            response = ollama.chat(
                model=self.model,
                messages=self.conversation_history,
                options=params
            )

            ai_message = self.clean_response(response['message']['content'])
            self.conversation_history.append({"role": "assistant", "content": ai_message})

            return ai_message

        except Exception as e:
            return f"Error: {str(e)}"

    def clean_response(self, text: str) -> str:
        """Limpia formatos específicos de cada modelo"""
        clean_rules = {
            "mistral": lambda x: x.replace("<s>", "").replace("</s>", "").strip(),
            "llama3": lambda x: x.replace("[[INST]]", "").replace("[[/INST]]", "").strip(),
            "gemma": lambda x: x.replace("**", "").strip()
        }
        return clean_rules.get(self.model, lambda x: x)(text)