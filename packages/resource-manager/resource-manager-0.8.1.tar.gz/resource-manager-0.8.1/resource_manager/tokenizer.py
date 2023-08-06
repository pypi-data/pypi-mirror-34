from token import tok_name
from tokenize import tokenize as _tokenize, TokenError

from .token import PARTIAL, TokenWrapper, RESERVED, TokenType, EXCLUDE


def tokenize(readline, source_path: str):
    tokens = []
    for token in _tokenize(readline):
        name = tok_name[token.type]
        if name == 'ERRORTOKEN':
            raise TokenError('Unrecognized token starting', token.start)
        if name in EXCLUDE:
            continue

        if name == 'COMMENT':
            if not PARTIAL.match(token.string.strip()):
                continue
            token_type = TokenType.PARTIAL
        else:
            token_type = RESERVED.get(token.string)
            if token_type is None:
                token_type = TokenType(token.exact_type)
        tokens.append(TokenWrapper(token, source_path, token_type))

    return tokens
