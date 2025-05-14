def turing_machine_unary_addition(input_tape):
    tape = list(input_tape)
    head = 0
    state = 'q0'
    
    while state != 'qf':
        if state == 'q0':
            if tape[head] == '1':
                head += 1
            elif tape[head] == '+':
                tape[head] = '1'
                head += 1
                state = 'q1'
        elif state == 'q1':
            if head < len(tape) and tape[head] == '1':
                head += 1
            else:
                if head >= len(tape):
                    tape.append('B')
                if tape[head] == 'B':
                    tape[head] = ' '
                    head -= 1
                    state = 'q2'
        elif state == 'q2':
            if tape[head] == '1':
                tape[head] = ' '
                state = 'qf'
            else:
                head -= 1
    
    # إزالة المسافات الفارغة
    result = ''.join([c for c in tape if c in ['1', '+']]).replace('+', '')
    return result

# مثال للاستخدام:
input_str = "111+11"
output = turing_machine_unary_addition(input_str)
print(f"Input: {input_str} → Output: {output}")