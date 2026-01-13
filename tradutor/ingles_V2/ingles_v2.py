'''
Docstring para ingles_v2

Versão 2 substitui as listas por dicionario (chave - valor)
mais pratico para procurar a palavra em ingles (chave) e retornar
a tradução (valor).

'''

en_pt = {
    # Artigos e pronomes
    "the": "o/a",
    "a": "um/uma",
    "an": "um/uma",
    "this": "este/esta",
    "that": "aquele/aquela",
    "these": "estes/estas",
    "those": "aqueles/aquelas",
    "I": "eu",
    "you": "você",
    "he": "ele",
    "she": "ela",
    "it": "isso",
    "we": "nós",
    "they": "eles",

    # Preposições
    "to": "para",
    "of": "de",
    "in": "em",
    "on": "em/sobre",
    "with": "com",
    "by": "por",
    "from": "de",
    "at": "em",
    "about": "sobre",
    "into": "dentro",
    "over": "sobre",
    "under": "sob",

    # Conjunções e advérbios
    "and": "e",
    "but": "mas",
    "or": "ou",
    "because": "porque",
    "if": "se",
    "while": "enquanto",
    "when": "quando",
    "where": "onde",
    "why": "por que",
    "how": "como",
    "not": "não",
    "very": "muito",

    # Verbos comuns
    "be": "ser/estar",
    "have": "ter",
    "do": "fazer",
    "say": "dizer",
    "go": "ir",
    "get": "obter",
    "make": "fazer",
    "know": "saber",
    "think": "pensar",
    "see": "ver",
    "use": "usar",
    "find": "encontrar",
    "give": "dar",
    "tell": "contar",
    "work": "trabalhar",
    "call": "chamar",
    "try": "tentar",
    "ask": "perguntar",
    "need": "precisar",
    "feel": "sentir",
    "become": "tornar-se",
    "leave": "sair",
    "put": "colocar",
    "keep": "manter",
    "let": "permitir",
    "begin": "começar",
    "seem": "parecer",
    "help": "ajudar",
    "talk": "falar",
    "turn": "virar",
    "start": "começar",
    "show": "mostrar",
    "hear": "ouvir",
    "play": "jogar",
    "run": "correr",
    "move": "mover",
    "live": "viver",
    "believe": "acreditar",

    # Substantivos comuns
    "man": "homem",
    "woman": "mulher",
    "child": "criança",
    "people": "pessoas",
    "time": "tempo",
    "year": "ano",
    "day": "dia",
    "world": "mundo",
    "life": "vida",
    "hand": "mão",
    "eye": "olho",
    "place": "lugar",
    "work": "trabalho",
    "week": "semana",
    "case": "caso",
    "problem": "problema",
    "fact": "fato",
    "government": "governo",
    "company": "empresa",
    "number": "número",

    # Adjetivos
    "good": "bom",
    "new": "novo",
    "first": "primeiro",
    "last": "último",
    "long": "longo",
    "great": "grande",
    "little": "pequeno",
    "old": "velho",
    "right": "certo",
    "big": "grande",
    "high": "alto",
    "small": "pequeno",
    "important": "importante"
}

def traduzir(frase, dicionario):
    palavras = frase.lower().split()
    traduzida = []

    for palavra in palavras:
        traduzida.append(dicionario.get(palavra, palavra))

    return " ".join(traduzida)


frase = "The quick brown fox jumps over the lazy dog"
print(traduzir(frase, en_pt))

# >>>>> RESOLVER <<<<<

# 1 - Palavras com 's' no final jump -> jumps
# 2 - Aumentar tamanho do dicionario
# 3 - Expressões que não devem ser traduzidas ao pé da letra: a piece of cake, break a leg