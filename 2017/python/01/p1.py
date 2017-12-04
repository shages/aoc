
def repetitions(iter):
    prev = int(iter[-1])
    for i in (int(x) for x in iter):
        if prev == i:
            yield i
        prev = i

def main():
    with open('input') as f:
        data = f.read().splitlines()[0]
    print(f'input={data}')
    rep = repetitions(data)
    print(f'sum={sum(rep)}')


if __name__ == '__main__':
    main()
