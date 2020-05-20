with open('text.txt','r') as f:
    print(len(f.readlines()))
    f.seek(0)
    for line_no,line in enumerate(f, start=1):
        print(f'{line_no}: {len(line)}')


