import textwrap

def wrap(string, max_width):
    wraped_text = textwrap.wrap(string,max_width)
    r=""
    for tx in wraped_text:
        r =r+tx+"\n"
    return r

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)