
def check_line(line):
    line = [int(x) for x in line.split()]
    line_sorted = sorted(line)
    for high in reversed(line_sorted):
        for low in line_sorted:
            if high == low:
                continue
            div = high / low
            if int(div) == div:
                print(f'even')
                return div

def main():
    with open('input') as f:
        data = f.read().splitlines()
    print(f'checksum = {sum(check_line(line) for line in data)}')

if __name__ == '__main__':
    main()
