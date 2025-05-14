# from collections import defaultdict

# class CFG:
#     def __init__(self):
#         self.productions = defaultdict(list)
    
#     def add_production(self, variable, derivation):
#         self.productions[variable].append(derivation)
    
#     def is_ambiguous(self, string):
#         parse_trees = []
#         self._generate_parse_trees('S', string, [], parse_trees)
#         return len(parse_trees) > 1
    
#     def _generate_parse_trees(self, current_var, remaining_str, current_derivation, all_derivations):
#         if not remaining_str:
#             if not any(self.productions.get(current_var, [])):
#                 all_derivations.append(current_derivation.copy())
#             return
        
#         for production in self.productions.get(current_var, []):
#             if production and production[0] == remaining_str[0]:
#                 new_derivation = current_derivation + [(current_var, production)]
#                 self._generate_parse_trees(production[1:], remaining_str[1:], new_derivation, all_derivations)
#             elif production and production[0] in self.productions:
#                 for prod in self.productions[production[0]]:
#                     combined_prod = prod + production[1:]
#                     new_derivation = current_derivation + [(current_var, combined_prod)]
#                     self._generate_parse_trees(combined_prod, remaining_str, new_derivation, all_derivations)

# # مثال للاستخدام:
# cfg = CFG()
# cfg.add_production('S', ['a', 'S', 'b'])
# cfg.add_production('S', ['S', 'a', 'b'])
# cfg.add_production('S', ['a', 'b'])

# test_string = "aabb"
# print(f"Is '{test_string}' ambiguous?", cfg.is_ambiguous(test_string))
import nltk
from nltk import CFG
from nltk.parse.chart import ChartParser

def is_ambiguous(cfg_string, test_string):
    # تحويل قواعد CFG إلى كائن من نوع CFG في nltk
    grammar = CFG.fromstring(cfg_string)
    
    # إنشاء محلل ChartParser
    parser = ChartParser(grammar)
    
    # تحويل سلسلة الاختبار إلى قائمة كلمات
    tokens = test_string.split()
    
    # إنشاء قائمة بجميع أشجار التحليل الممكنة
    parse_trees = list(parser.parse(tokens))

    # طباعة كل شجرة تحليل (اختياري)
    for i, tree in enumerate(parse_trees):
        print(f"Parse Tree {i+1}:\n{tree}\n")

    # إذا وُجد أكثر من شجرة تحليل، فإن القواعد غامضة
    if len(parse_trees) > 1:
        print("The grammar is ambiguous for the given string.")
        return True
    elif len(parse_trees) == 1:
        print("The grammar is not ambiguous for the given string.")
        return False
    else:
        print("The string is not derivable from the grammar.")
        return None

# مثال على الاستخدام:

cfg = """
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
NP -> Det N | Det N PP
V -> 'saw'
P -> 'with'
Det -> 'a' | 'the'
N -> 'man' | 'telescope'
"""

test_input = "the man saw a man with a telescope"

is_ambiguous(cfg, test_input)
