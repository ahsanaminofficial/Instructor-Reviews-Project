with open("routes.txt") as f:
    data = f.read()


ret_data = ""

temp_data = data.split("\n")
# print(temp_data)


# print(len(temp_data))

for line in temp_data:
    n_line = line.strip().split()
    # ret_data += '\t'.join(n_line)
    # ret_data += '\n'
    # print(n_line)

    if len(n_line) == 4:
        ret_data += '{:<35} {:<8} {:<40}\t\t\t{:<50}\n'.format(n_line[0], n_line[1], n_line[2], n_line[3])
    elif len(n_line) == 3:
        ret_data += '{:<35} {:<8} {:<40}\t\t\t{:<50}\n'.format(' ', n_line[0], n_line[1], n_line[2])
    else:
        ret_data += '\n'

print(ret_data)



with open("routes.txt", 'w') as f:
    f.write(ret_data)
