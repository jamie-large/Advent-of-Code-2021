def solution_part1():
    with open('inputs/day16.txt', 'r') as f:
        binary_input = ''.join([format(int(x, 16), '04b') for x in f.readline()[:-1]])
        return solve_packet(binary_input)[0]

def solve_packet(binary_input):
    # # print(f"Solving packet {binary_input}")
    result = packet_version = int(binary_input[:3], 2)
    # # print(f"packet_version: {result}")
    packet_type = binary_input[3:6]
    i = 6
    # Literal packet
    if packet_type == "100":
        value = ""
        while i < len(binary_input):
            group = binary_input[i:i+5]
            value += group[1:]
            i += 5
            if group[0] == '0':
                # print(f"value: {int(value, 2)}")
                # print(f"result: {result}")
                return result, i
    # Operator
    else:
        i += 1
        # Total Length
        if binary_input[6] == '0':
            total_length = int(binary_input[i:i+15], 2)
            i += 15
            end = i+total_length
            while i < end:
                result_inc, i_inc = solve_packet(binary_input[i:end])
                result += result_inc
                i += i_inc
        # Number of packets
        else:
            n_packets = int(binary_input[i:i+11], 2)
            i += 11
            for _ in range(n_packets):
                result_inc, i_inc = solve_packet(binary_input[i:])
                result += result_inc
                i += i_inc
    # print(f"result: {result}")
    return result, i


def solution_part2():
    with open('inputs/day16.txt', 'r') as f:
        binary_input = ''.join([format(int(x, 16), '04b') for x in f.readline()[:-1]])
        return solve_packet_2(binary_input)[0]

def solve_packet_2(binary_input):
    # print(f"Solving packet {binary_input}")
    packet_version = int(binary_input[:3], 2)
    packet_type = int(binary_input[3:6], 2)
    i = 6
    # Literal packet
    if packet_type == 4:
        value = ""
        while i < len(binary_input):
            group = binary_input[i:i+5]
            value += group[1:]
            i += 5
            if group[0] == '0':
                result = int(value, 2)
                # print(f"literal packet {value} result: {result}")
                return result, i
    # Operators
    else:
        result = None
        i += 1
        subpacket_values = []
        # Total Length
        if binary_input[6] == '0':
            total_length = int(binary_input[i:i+15], 2)
            i += 15
            end = i+total_length
            while i < end:
                subp_result, i_inc = solve_packet_2(binary_input[i:end])
                subpacket_values.append(subp_result)
                i += i_inc
        # Number of packets
        else:
            n_packets = int(binary_input[i:i+11], 2)
            i += 11
            for _ in range(n_packets):
                subp_result, i_inc = solve_packet_2(binary_input[i:])
                subpacket_values.append(subp_result)
                i += i_inc
        if packet_type == 0:
            result = sum(subpacket_values)
        elif packet_type == 1:
            result = 1
            for v in subpacket_values:
                result *= v
        elif packet_type == 2:
            result = min(subpacket_values)
        elif packet_type == 3:
            result = max(subpacket_values)
        elif packet_type == 5:
            result = 1 if subpacket_values[0] > subpacket_values[1] else 0
        elif packet_type == 6:
            result = 1 if subpacket_values[0] < subpacket_values[1] else 0
        elif packet_type == 7:
            result = 1 if subpacket_values[0] == subpacket_values[1] else 0
        # print(f"result of {packet_type} operation on {subpacket_values}: {result}")
        return result, i

print(f"Final result: {solution_part1()}")
