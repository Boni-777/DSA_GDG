def split_and_join(line):
    # write your code here
     splitt=line.split(" ")
     return "-".join(splitt)
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
