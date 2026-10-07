import httpx

from .base import AIProvider


class OllamaProvider(AIProvider):
    def __init__(self, model: str = "llama3.1", host: str = "http://localhost:11434"):
        self.model = model
        self.host = host

    async def chat(self, messages, tools=None):
        try:
            async with httpx.AsyncClient(timeout=120) as client:
                r = await client.post(
                    f"{self.host}/api/chat",
                    json={"model": self.model, "messages": messages, "stream": False},
                )
                r.raise_for_status()
                data = r.json()
                return {"role": "assistant", "content": data["message"]["content"]}
        except Exception as e:
            return {
                "role": "assistant",
                "content": f"[Ollama no disponible: {e}]",
            }
