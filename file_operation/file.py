
def read_file_in_chunk(file_directory):
    with open(file_directory) as f:
        for line in f:
            yield line