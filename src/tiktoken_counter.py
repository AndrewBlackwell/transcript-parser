import tiktoken


def count_tokens(string: str, model: str) -> int:
    code = tiktoken.encoding_for_model(string, model)
    token_count = len(code.encode(string))
    return token_count
