# https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true

def split_and_join(line):
    # write your code here
    answer = line.split(' ')
    return "-".join(answer)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
