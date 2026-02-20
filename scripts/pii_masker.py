import re
import json

def mask_pii(text: str) -> tuple[str, dict]:
    """
    Detects and masks Brazilian formatting PII (CPFs, NBs, and names).
    Returns the masked text and a mapping dictionary to restore the original values if needed.
    """
    mapping = {}
    cpf_counter = 1
    nb_counter = 1
    nome_counter = 1
    
    # 1. Mask CPFs (11 digits or 000.000.000-00)
    cpf_pattern = r'\b(?:\d{3}\.\d{3}\.\d{3}-\d{2}|\d{11})\b'
    def replace_cpf(match):
        nonlocal cpf_counter
        val = match.group(0)
        token = f'[CPF_{cpf_counter}]'
        mapping[token] = val
        cpf_counter += 1
        return token
    
    text = re.sub(cpf_pattern, replace_cpf, text)
    
    # 2. Mask NBs (10 digits or 000.000.000-0)
    nb_pattern = r'\b(?:\d{3}\.\d{3}\.\d{3}-\d{1}|\d{10})\b'
    def replace_nb(match):
        nonlocal nb_counter
        val = match.group(0)
        token = f'[NB_{nb_counter}]'
        mapping[token] = val
        nb_counter += 1
        return token
    
    text = re.sub(nb_pattern, replace_nb, text)
    
    # 3. Mask Names (following specific keywords like Nome: or Segurado:)
    # Looking for a capitalized word possibly followed by other capitalized words
    name_pattern = r'(Nome|Segurado|Requerente|Titular)([\s:]+)([A-ZÀ-Ÿ][a-zà-ÿ]+(?:[\s]+[A-ZÀ-Ÿ][a-zà-ÿ]+)+)'
    def replace_name(match):
        nonlocal nome_counter
        prefix_word = match.group(1)
        separator = match.group(2)
        val = match.group(3)
        token = f'[NOME_{nome_counter}]'
        mapping[token] = val
        nome_counter += 1
        return f"{prefix_word}{separator}{token}"
    
    text = re.sub(name_pattern, replace_name, text, flags=re.IGNORECASE)
    
    return text, mapping

def restore_pii(masked_text: str, mapping: dict) -> str:
    """
    Restores the original PII into the masked text using the mapping dictionary.
    """
    restored_text = masked_text
    for token, original_value in mapping.items():
        restored_text = restored_text.replace(token, original_value)
    return restored_text

if __name__ == "__main__":
    # Test execution
    sample_text = "O segurado João Pereira da Silva, portador do CPF 123.456.789-00 e do benefício NB 123.456.789-0 solicitou a revisão. Nome: Maria do Carmo Alves."
    
    print("--- ORIGINAL ---")
    print(sample_text)
    
    masked, pii_map = mask_pii(sample_text)
    print("\n--- MASCARADO ---")
    print(masked)
    print("Mapa de PII guardado localmente:", json.dumps(pii_map, ensure_ascii=False))
    
    restored = restore_pii(masked, pii_map)
    print("\n--- RESTAURADO ---")
    print(restored)
