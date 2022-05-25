from urllib.parse import unquote

# read links from txt file and save each links it a separate file
#
# function to get file name from url without file extension
def get_file_name(url):
    # split url into list
    url_list = url.split('/')
    # get last item in list
    file_name = url_list[-1]
    # split file name into list
    file_name_list = file_name.split('.')
    # get first item in list
    file_name = file_name_list[0]
    # return file name
    return file_name

def main():
    # open file
    infile = open('links.txt', 'r')
    # read lines from file
    lines = infile.readlines()
    # close file
    infile.close()
    # create empty list to store lines
    lines_to_file = []
    # create empty list to store file names
    file_names = []
    # loop through lines
    for line in lines:
        # strip new line
        line = line.strip()
        # add line to list
        lines_to_file.append(line)
    # loop through lines
    for line in lines_to_file:
        # create file name
        file_name = get_file_name(line)
        # add file name to list
        file_name = unquote(file_name)
        file_names.append(file_name)
    # loop through lines
    for index in range(len(lines_to_file)):
        # open file
        outfile = open(file_names[index] + ".strm", 'w')
        # write lines to file
        outfile.write(lines_to_file[index])
        # close file
        outfile.close()

main()
