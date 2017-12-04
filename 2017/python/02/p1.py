
def check_line(line):
    line = [int(x) for x in line.split()]
    return max(line) - min(line)

def main():
    with open('input') as f:
        data = f.read().splitlines()
    print(f'checksum = {sum(check_line(line) for line in data)}')

if __name__ == '__main__':
    main()
