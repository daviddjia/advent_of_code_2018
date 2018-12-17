#!/usr/bin/env python
import re

class CPU(object):

    def __init__(self, registers, mapping):
        self.registers = list(registers)
        self.mapping = mapping

    def _run_instruction(self, name, operand1, operand2):
        # No, I can't be bothered to turn this into a dict of lambdas kthxbye
        if name == 'addr':
            return self.registers[operand1] + self.registers[operand2]
        elif name == 'addi':
            return self.registers[operand1] + operand2
        elif name == 'mulr':
            return self.registers[operand1] * self.registers[operand2]
        elif name == 'muli':
            return self.registers[operand1] * operand2
        elif name == 'banr':
            return self.registers[operand1] & self.registers[operand2]
        elif name == 'bani':
            return self.registers[operand1] & operand2
        elif name == 'borr':
            return self.registers[operand1] | self.registers[operand2]
        elif name == 'bori':
            return self.registers[operand1] | operand2
        elif name == 'setr':
            return self.registers[operand1]
        elif name == 'seti':
            return operand1
        elif name == 'gtir':
            return 1 if operand1 > self.registers[operand2] else 0
        elif name == 'gtri':
            return 1 if self.registers[operand1] > operand2 else 0
        elif name == 'gtrr':
            return 1 if self.registers[operand1] > self.registers[operand2] else 0
        elif name == 'eqir':
            return 1 if operand1 == self.registers[operand2] else 0
        elif name == 'eqri':
            return 1 if self.registers[operand1] == operand2 else 0
        elif name == 'eqrr':
            return 1 if self.registers[operand1] == self.registers[operand2] else 0
        else:
            print "ERROR! CPU CRASHING! EXPLOSIONS!"

    def run_program(self, instructions):
        for instr in instructions:
            instr_name = self.mapping[instr[0]]
            result = self._run_instruction(instr_name, instr[1], instr[2])
            self.registers[instr[3]] = result

        return tuple(self.registers)

    def test_instruction():
        pass

def process_input(lines):
    i = 0
    samples = []
    program = []
    while i < len(lines):
        if 'Before' in lines[i]:
            regex = '\[(\d*), (\d*), (\d*), (\d*)\]'
            groups = re.search(regex, lines[i])
            before = (
                int(groups.group(1)),
                int(groups.group(2)),
                int(groups.group(3)),
                int(groups.group(4)),
            )

            instruction = tuple(int(j) for j in lines[i+1].split())

            groups = re.search(regex, lines[i+2])
            after = (
                int(groups.group(1)),
                int(groups.group(2)),
                int(groups.group(3)),
                int(groups.group(4)),
            )

            samples.append((before, instruction, after))
            i += 4
        else:
            instruction = tuple(int(j) for j in lines[i].split())
            program.append(instruction)
            i += 1
    return (samples, program)

def main():
    f = open('day16_input.txt','r')
    lines = f.readlines()
    f.close()

    (samples, program) = process_input(lines)

    possible_instructions = [
        'addr', 'addi',
        'mulr', 'muli',
        'banr', 'bani',
        'borr', 'bori',
        'setr', 'seti',
        'gtir', 'gtri', 'gtrr',
        'eqir', 'eqri', 'eqrr',
    ]
    num_samples_3_options = 0
    for (before, instruction, after) in samples:
        count = 0
        for pi in possible_instructions:
            cpu = CPU(before, mapping={instruction[0]: pi})
            real_after = cpu.run_program(
                [instruction],
            )
            if after == real_after:
                count += 1
        if count >= 3:
            num_samples_3_options += 1
    print "Part 1: Number of samples that behave like 3 or more opcodes: %s" % (
        num_samples_3_options,
    )

if __name__ == "__main__":
    main()
