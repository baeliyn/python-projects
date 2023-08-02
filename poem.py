def read_file(file_name):

    file = open(file_name, mode = 'r')

    data = file.read()

    print(data)

    return data

    file.close()

    raise NotImplementedError()

def read_file_into_list(file_name):

    file = open(file_name, mode = 'r')

    data = file.read().split("\n")

    file.close()

    return data

    raise NotImplementedError()

def write_first_line_to_file(file_contents, output_filename):

    with open(output_filename, 'w') as file:
        file.write(file_contents.split("\n")[0])


def read_even_numbered_lines(file_name):

    file = open(file_name, mode = 'r')
    data = file.read().split("\n")
    return_data = []
    index = 1

    for line in data:
        if index % 2 == 0:
            return_data.append(line)
        index += 1

    file.close()

    return return_data

    raise NotImplementedError()

def read_file_in_reverse(file_name):
    
    file = open(file_name, mode = 'r')

    data = file.read().split("\n")

    return_data = data[::-1]

    file.close()

    return return_data

    raise NotImplementedError()

def main():
    file_contents = read_file("poem.txt")
    print(read_file_into_list("poem.txt"))
    write_first_line_to_file(file_contents, "poem_line.txt")
    print(read_even_numbered_lines("poem.txt"))
    print(read_file_in_reverse("poem.txt"))

if __name__ == "__main__":
    main()