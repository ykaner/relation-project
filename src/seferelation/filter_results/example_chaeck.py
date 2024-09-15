from basic_filter import Filter
filter = Filter()
if __name__ == '__main__':
    with open('example_genesis.1','r+') as file:
        lines = file.readlines()
        print(lines)
        for line in lines:
            # print(line.split('  ')[1][:-1])
            # print(filter.Do_it_close(line.split('\t')[1][:-1], 'https://www.sefaria.org.il/Genesis.1'))
            if not filter.Do_it_close(line.split('\t')[1][:-1], 'https://www.sefaria.org.il/Genesis.1.1'):
                print(line)

