---
language:
- ru
- en
tags:
- tokenizer
- bpe
- russian
- english
- code
- reasoning
- safety
- agent
library_name: tokenizers
license: cc-by-nc-4.0
---
![ARM-Tokenizer Pro](tokenizer.jpg)

# ARM-Tokenizer Pro (85k)

**Compact. Precise. Powerful.**

ARM-Tokenizer Pro is a flagship tokenizer by NeoneAI, designed for compact language models (300M–1B parameters) that run locally on mobile devices and laptops. It was trained on a meticulously balanced dataset (Russian books, English literature, code, plus emoji injection) to achieve maximum compression for Russian without sacrificing English or Code performance.

## 📊 Benchmarks (Real-world data)

*Tested on 1.87MB of Russian books, 1.75MB of English Gutenberg, complex Python/C++ code, and a diverse emoji set. Lower `tok/char` is better.*

| Tokenizer | Russian | English | Code | Emoji |
| :--- | :--- | :--- | :--- | :--- |
| **ARM-Tokenizer Pro (85k)** | **0.2836** | **0.2451** | **0.3307** | **0.3800** |
| Gemma 3 (262k) | 0.3584 | 0.2329 | 0.3274 | 0.9000 |
| Qwen3 (151k) | 0.4350 | 0.2347 | 0.2584 | 1.2400 |
| DeepSeek-V3 (128k) | 0.3922 | 0.2349 | 0.2841 | 1.2400 |
| ARM-Tokenizer Base (65k) | 0.3118 | 0.2505 | 0.3788 | 2.0200 |

### 🏆 Key Achievements

*   **Built-in Reasoning:** Unlike standard tokenizers, ARM-Tokenizer Pro features a dedicated set of special tokens (`<|think|>`, `<|step_think_1|>`...`<|step_think_9|>`, `<|verify|>`) designed to hard-code the reasoning process directly into the model's architecture, making it transparent and verifiable.
*   **Russian Language:** **21% more efficient** than Gemma 3, **35% more efficient** than Qwen3, and **28% more efficient** than DeepSeek-V3.
*   **Emoji:** **2.3x more efficient** than Gemma 3, and **3.2x more efficient** than Qwen3/DeepSeek.
*   **Balanced Performance:** Unlike massive models that sacrifice Russian for Chinese or English, ARM-Tokenizer Pro delivers top-tier Russian compression while remaining competitive on English (+5% vs Gemma) and Code (+1% vs Gemma).
*   **Efficient Size:** With an 85k vocabulary, it provides optimal balance. It is 3x smaller than Gemma's 262k vocabulary, making it perfect for models with <1B parameters where embedding layers must be kept lightweight.

## 🧠 Special Tokens (26+)

ARM-Tokenizer Pro includes one of the most extensive special token sets among open-source tokenizers, designed for advanced AI agents:

*   **Roles:** `<|system|>`, `<|user|>`, `<|assistant|>`, `<|endoftext|>`, `<|pad|>`, `<|bos|>`, `<|eos|>`
*   **Reasoning (CoT):** `<|think|>`, `<|/think|>`, `<|verify|>`, `<|step_think_1|>` ... `<|step_think_9|>`
*   **Tools:** `<|tool_call|>`, `<|tool_result|>`, `<|context|>`, `<|/context|>`
*   **Safety:** `<|safe|>`, `<|harmful|>`
*   **Agents:** `<|agent_id|>`, `<|/agent_id|>`

## 🚀 Usage

```python
from huggingface_hub import hf_hub_download
from tokenizers import Tokenizer

tokenizer_path = hf_hub_download(
    repo_id="andrey-neoneai/ARM-Tokenizer_Pro",
    filename="ARM-Tokenizer_Pro/arm-tokenizer_pro.json"
)
tokenizer = Tokenizer.from_file(tokenizer_path)

encoded = tokenizer.encode("Привет, мир! 😊 <|think|>")
print(encoded.tokens)
print(encoded.ids)
```
## 📜 License

This tokenizer is released under the **CC BY-NC 4.0** license. 
You are free to use it for research, personal projects, and non-commercial applications. 

**For commercial use:** If you want to integrate ARM-Tokenizer Pro into a commercial product, please contact the author directly at: **neoneai.contact@gmail.com**
---
**If you're using Pro in a commercial product — write to us. We don't bite 🤗 — but we don't give away licenses for free either.**
---
*Copyright (c) 2026 NeoneAI. All rights reserved.*
