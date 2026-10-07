class Router:
    """Decide qué proveedor usar según el mensaje."""

    def __init__(self, providers: dict):
        self.providers = providers

    def pick(self, text: str, default: str = "deepseek") -> str:
        lower = text.lower()

        # Código / programación → DeepSeek
        if any(w in lower for w in ["código", "programa", "función", "script", "bug", "python"]):
            if "deepseek" in self.providers:
                return "deepseek"

        # Contexto largo → Gemini
        if len(text) > 300 and "gemini" in self.providers:
            return "gemini"

        # Default disponible
        if default in self.providers:
            return default

        # Fallback: Ollama siempre está
        return "ollama"
