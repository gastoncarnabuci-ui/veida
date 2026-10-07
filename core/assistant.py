import json
from pathlib import Path

from ai.openai_provider import OpenAIProvider
from ai.gemini_provider import GeminiProvider
from ai.deepseek_provider import DeepSeekProvider
from ai.ollama_provider import OllamaProvider
from core.personality import get_system_prompt
from core.router import Router


class Assistant:
    """Cerebro central. Singleton."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._setup()
        return cls._instance

    def _setup(self):
        config = self._load_config()
        self._providers = {}

        provs = config.get("providers", {})

        if provs.get("openai", {}).get("api_key"):
            self._providers["openai"] = OpenAIProvider(
                api_key=provs["openai"]["api_key"],
                model=provs["openai"].get("model", "gpt-4o-mini"),
            )
        if provs.get("gemini", {}).get("api_key"):
            self._providers["gemini"] = GeminiProvider(
                api_key=provs["gemini"]["api_key"],
                model=provs["gemini"].get("model", "gemini-1.5-flash"),
            )
        if provs.get("deepseek", {}).get("api_key"):
            self._providers["deepseek"] = DeepSeekProvider(
                api_key=provs["deepseek"]["api_key"],
                model=provs["deepseek"].get("model", "deepseek-chat"),
            )

        # Ollama siempre disponible (falla suave si no está corriendo)
        self._providers["ollama"] = OllamaProvider(
            model=provs.get("ollama", {}).get("model", "llama3.1")
        )

        self._router = Router(self._providers)
        self._history = []
        self._personality = config.get("personality", "jarvis")
        self._default = config.get("default_provider", "deepseek")

    def _load_config(self):
        base = Path(__file__).parent.parent / "config"
        cfg_path = base / "settings.json"
        if not cfg_path.exists():
            cfg_path = base / "settings.example.json"
        return json.loads(cfg_path.read_text(encoding="utf-8"))

    async def respond(self, text: str) -> str:
        system = get_system_prompt(self._personality)
        self._history.append({"role": "user", "content": text})
        messages = [{"role": "system", "content": system}] + self._history[-20:]

        provider_name = self._router.pick(text, self._default)
        provider = self._providers.get(provider_name, self._providers["ollama"])

        try:
            result = await provider.chat(messages)
            reply = result.get("content", "")
        except Exception as e:
            reply = f"Error al consultar {provider_name}: {e}"

        self._history.append({"role": "assistant", "content": reply})
        return reply
