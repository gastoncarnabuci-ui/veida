# V.E.I.D.A. — Virtual Executive Integrated Dream Architect

> IA de escritorio tipo JARVIS con servidor propio, memoria, voz natural y múltiples proveedores de IA.

![status](https://img.shields.io/badge/status-en%20desarrollo-yellow)
![python](https://img.shields.io/badge/python-3.10%2B-blue)
![license](https://img.shields.io/badge/license-MIT-green)

---

## ¿Qué es V.E.I.D.A.?

V.E.I.D.A. es una **aplicación de escritorio** (no una página web) que funciona como:

- 🧠 **IA conversacional** multi-proveedor (OpenAI, Gemini, DeepSeek, Ollama local)
- 🌐 **Servidor local** en `127.0.0.1:8765` con API REST
- 🎙️ **Voz natural** con STT (Whisper) y TTS (Edge-TTS)
- 💾 **Memoria persistente** con SQLite
- 🛠️ **Agente** capaz de abrir apps, buscar archivos, controlar el sistema
- 🎨 **Interfaz Jarvis** con reactor animado, HUD y protocolos temáticos

---

## Estado

🚧 En desarrollo activo. Ver [docs/ROADMAP.md](docs/ROADMAP.md).

---

## Instalación

### Requisitos
- Python 3.10 o superior
- (Opcional) [Ollama](https://ollama.ai) para IA local

```bash
git clone https://github.com/gastoncarnabuci-ui
cd veida

python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt

# Copiar config de ejemplo
cp config/settings.example.json config/settings.json
# Windows: copy config\settings.example.json config\settings.json

# Editar config/settings.json con tus API keys
python -m app.mainm
