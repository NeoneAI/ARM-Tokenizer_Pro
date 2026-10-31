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