# تعريف الجرامر في صورة dictionary
# كل مفتاح (Non-terminal) بيقابله ليست من البدائل
grammar = {
    "S": ["AB", "b"],
    "A": ["aA", "a"],
    "B": ["bB", "c"]
}

terminals = ['a', 'b', 'c']

# إزالة الإنتاجات اللي بتبدأ بـ non-terminal
def convert_to_gnf(grammar):
    gnf = {}

    for non_terminal in grammar:
        gnf[non_terminal] = []
        for production in grammar[non_terminal]:
            if production[0] in terminals:
                gnf[non_terminal].append(production)
            else:
                replaced = replace_start(grammar, production)
                gnf[non_terminal].extend(replaced)

    return gnf

# دالة لمساعدة التحويل
def replace_start(grammar, production):
    new_productions = []
    start_symbol = production[0]
    rest = production[1:]

    if start_symbol in grammar:
        for sub in grammar[start_symbol]:
            new_productions.append(sub + rest)
    else:
        new_productions.append(production)

    return new_productions

# طباعة الجرامر قبل وبعد التحويل
def print_grammar(g):
    for nt in g:
        print(f"{nt} -> {' | '.join(g[nt])}")

print("الجرامر قبل التحويل:")
print_grammar(grammar)

print("\nالجرامر بعد التحويل لـ GNF:")
gnf_grammar = convert_to_gnf(grammar)
print_grammar(gnf_grammar)
