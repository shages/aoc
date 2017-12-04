
def repetitions_halfway(data):
    half = int(len(data) / 2)
    for i, j in zip(data, data[half:] + data[:half]):
        if i == j:
            yield int(i)

def main():
    with open('input') as f:
        data = f.read().splitlines()[0]
    print(f'input={data}')
    rep = repetitions_halfway(data)
    print(f'sum={sum(rep)}')


if __name__ == '__main__':
    main()
