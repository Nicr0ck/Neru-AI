# Neru-AI
Un asistente IA, basado en [Mistral:7B](https://mistral.ai/news/announcing-mistral-7b), servido en [Ollama](https://ollama.com/) y ejecutado como un agente por la extensión [Kilo Code](https://kilo.ai/), requiere de [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit) de NVidia, Neru es compatible con Windows y Linux.
Guía para usar neru:
1. Instalar requerimientos:
	[Ollama](https://ollama.com/download), [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads) y [Kilo Code](https://kilo.ai/)
2. Instalar el modelo base(mistral:7B):
	desde powershell ejecutar el comando:
```
	ollama pull mistral:7B
```
3. NeruIzar la IA
```
	ollama cp mistral neru
```
3.5. Borrar Mistral (opcional)
```
  ollama rm mistral
```
4. Instalar [Kilo code](https://kilo.ai/) en tu IDE de confianza
	una vez instalado clickear en la opcion "use your own API key", cambiar el "API Provider" a Ollama y seleccionar a Neru (es importante tener en cuenta aumentar el Context Window Size a un valor minimo de 32000) y Listo ya tenés a la confiable IA Neru
