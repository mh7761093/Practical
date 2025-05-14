from collections import deque, defaultdict

def epsilon_closure(nfa, states):
    closure = set(states)
    queue = deque(states)
    
    while queue:
        state = queue.popleft()
        for next_state in nfa.get((state, 'ε'), set()):
            if next_state not in closure:
                closure.add(next_state)
                queue.append(next_state)
    return frozenset(closure)

def nfa_to_dfa(nfa, alphabet, start_state, accept_states):
    alphabet = [a for a in alphabet if a != 'ε']
    initial_closure = epsilon_closure(nfa, {start_state})
    
    dfa = {}
    dfa_accept_states = set()
    unprocessed_states = deque([initial_closure])
    processed_states = set()
    
    if any(state in accept_states for state in initial_closure):
        dfa_accept_states.add(initial_closure)
    
    while unprocessed_states:
        current_state = unprocessed_states.popleft()
        processed_states.add(current_state)
        
        for symbol in alphabet:
            next_states = set()
            for state in current_state:
                next_states_for_symbol = nfa.get((state, symbol), set())
                next_states.update(next_states_for_symbol)
            
            if not next_states:
                continue
                
            next_closure = epsilon_closure(nfa, next_states)
            
            if next_closure not in processed_states and next_closure not in unprocessed_states:
                unprocessed_states.append(next_closure)
            
            dfa[(current_state, symbol)] = next_closure
            
            if any(state in accept_states for state in next_closure):
                dfa_accept_states.add(next_closure)
    
    return dfa, initial_closure, dfa_accept_states

# مثال للاستخدام:
nfa = {
    (0, 'a'): {1},
    (0, 'ε'): {2},
    (1, 'b'): {1, 2},
    (1, 'ε'): {0},
    (2, 'a'): {2},
    (2, 'b'): {0}
}
alphabet = ['a', 'b']
start_state = 0
accept_states = {2}

dfa, initial_state, dfa_accept = nfa_to_dfa(nfa, alphabet, start_state, accept_states)
print("DFA:", dfa)
print("Initial State:", initial_state)
print("Accept States:", dfa_accept)