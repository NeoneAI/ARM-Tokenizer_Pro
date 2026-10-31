import os
from tokenizers import Tokenizer
from huggingface_hub import hf_hub_download

# Determine the directory where the script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths
PRO_TOKENIZER = os.path.join(BASE_DIR, "arm-tokenizer_pro.json")
RU_SAMPLE = os.path.join(BASE_DIR, "sample", "ru_books_sample.txt")
EN_SAMPLE = os.path.join(BASE_DIR, "sample", "gutenberg_sample.txt")

# External tokenizers
BASE_REPO = "andrey-neoneai/arm-tokenizer"
BASE_FILENAME = "arm_tokenizer/tokenizer.json"
QWEN_REPO = "Qwen/Qwen3-0.6B"
QWEN_FILE = "tokenizer.json"
DEEPSEEK_REPO = "deepseek-ai/DeepSeek-V3"
DEEPSEEK_FILE = "tokenizer.json"
GEMMA_REPO = "google/gemma-3-4b-it"
GEMMA_FILE = "tokenizer.json"

# Test texts for code and emoji
TEXT_CODE = """import os
import sys

# Russian comment: checking cyrillic support
def calculate_loss(logits, targets):
    \"\"\"
    Computes CrossEntropy.
    \"\"\"
    loss = 0.0
    for i in range(len(logits)):
        loss -= targets[i] * math.log(logits[i] + 1e-9)
    return loss / len(logits)

class Transformer(nn.Module):
    def __init__(self, hidden_size=1024, num_heads=16):
        super().__init__()
        self.attention = nn.MultiheadAttention(hidden_size, num_heads)
        self.norm = nn.LayerNorm(hidden_size)

    def forward(self, x):
        attn_out, _ = self.attention(x, x, x)
        return self.norm(x + attn_out)"""

TEXT_EMOJI = "😊 🚀 🔥 😂 ❤️ 👍 👎 🎉 💻 🧠 💡 ⚡️ 🌍 🍕 ☕️ 🇷🇺 🇺🇸 👨‍👩‍👧‍👦 🧑‍💻"

def count_tokens_file(tokenizer, file_path):
    total_tokens = 0
    total_chars = 0
    
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        while True:
            chunk = f.read(1024 * 1024)
            if not chunk:
                break
            total_chars += len(chunk)
            encoded = tokenizer.encode(chunk)
            total_tokens += len(encoded.ids)
            
    return total_tokens, total_chars

def count_tokens_text(tokenizer, text):
    encoded = tokenizer.encode(text)
    return len(encoded.ids), len(text)

def load_tokenizer(repo, filename, name):
    """Helper to load tokenizer with error handling."""
    try:
        print(f"  Loading {name}...")
        path = hf_hub_download(repo_id=repo, filename=filename)
        return Tokenizer.from_file(path)
    except Exception as e:
        print(f"  ⚠️ Failed to load {name}: {e}")
        return None

def main():
    if not os.path.exists(PRO_TOKENIZER):
        print(f"Error: Tokenizer file not found at: {PRO_TOKENIZER}")
        return
    if not os.path.exists(RU_SAMPLE) or not os.path.exists(EN_SAMPLE):
        print("Error: Sample files not found in 'sample/' directory.")
        return

    print("Loading tokenizers...")
    pro_tok = Tokenizer.from_file(PRO_TOKENIZER)
    base_tok = load_tokenizer(BASE_REPO, BASE_FILENAME, "Base")
    qwen_tok = load_tokenizer(QWEN_REPO, QWEN_FILE, "Qwen3")
    ds_tok = load_tokenizer(DEEPSEEK_REPO, DEEPSEEK_FILE, "DeepSeek")
    gemma_tok = load_tokenizer(GEMMA_REPO, GEMMA_FILE, "Gemma 3")
    
    tokenizers = {
        "Base (65k)": base_tok,
        "Pro (85k)": pro_tok,
        "Qwen3 (151k)": qwen_tok,
        "DeepSeek (128k)": ds_tok,
        "Gemma 3 (262k)": gemma_tok,
    }
    
    # Filter out failed loads
    tokenizers = {k: v for k, v in tokenizers.items() if v is not None}

    results = {}

    print("Running tests on files (this may take a few minutes)...")
    for name, tok in tokenizers.items():
        print(f"  Processing files: {name}...")
        ru_tokens, ru_chars = count_tokens_file(tok, RU_SAMPLE)
        en_tokens, en_chars = count_tokens_file(tok, EN_SAMPLE)
        
        print(f"  Processing code and emoji: {name}...")
        code_tokens, code_chars = count_tokens_text(tok, TEXT_CODE)
        emoji_tokens, emoji_chars = count_tokens_text(tok, TEXT_EMOJI)
        
        results[name] = {
            "ru": ru_tokens / ru_chars,
            "en": en_tokens / en_chars,
            "code": code_tokens / code_chars,
            "emoji": emoji_tokens / emoji_chars
        }

    print("\n" + "="*90)
    print("FINAL BENCHMARK RESULTS (tok/char)")
    print("="*90)
    print(f"{'Tokenizer':<20} | {'Russian':<10} | {'English':<10} | {'Code':<10} | {'Emoji':<10}")
    print("-" * 90)
    
    for name, data in results.items():
        print(f"{name:<20} | {data['ru']:<10.4f} | {data['en']:<10.4f} | {data['code']:<10.4f} | {data['emoji']:<10.4f}")
    
    print("="*90)

if __name__ == "__main__":
    main()