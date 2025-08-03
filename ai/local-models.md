# Local AI Models Guide

## LM Studio Setup

### Installation

```bash
# Download from https://lmstudio.ai/
# Or use homebrew
brew install --cask lm-studio
```

### Recommended Models

| Model                  | Size | Use Case                   |
| ---------------------- | ---- | -------------------------- |
| dolphin3.0-llama3.1-8b | 8GB  | Uncensored general purpose |
| codellama-7b           | 7GB  | Code generation            |
| mistral-7b-instruct    | 7GB  | Fast general purpose       |

### Performance Tips

1. **Model Selection**

   - Choose models that fit in your RAM
   - M1 Macs: 8GB models work well
   - Use quantized versions (Q4_K_M) for better performance

2. **Settings**

   - Context Length: 4096 for most tasks
   - Temperature: 0.7 for creative, 0.1 for factual
   - GPU Layers: Max for M1/M2 chips

3. **API Usage**

   ```python
   import requests

   response = requests.post(
       "http://localhost:1234/v1/chat/completions",
       json={
           "model": "dolphin3.0-llama3.1-8b",
           "messages": [{"role": "user", "content": "Hello!"}]
       }
   )
   ```
