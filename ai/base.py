from abc import ABC, abstractmethod


class AIProvider(ABC):
    """Interfaz común para todos los proveedores de IA."""

    @abstractmethod
    async def chat(self, messages: list[dict], tools: list = None) -> dict:
        """Devuelve {'role': 'assistant', 'content': '...'}"""
        ...
