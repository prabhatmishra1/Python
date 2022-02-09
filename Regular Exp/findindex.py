import re
def get_index(K,S):

    match = re.search(K,S)
    index = 0
    if match:
        while index < len(S):
            print(S[index:])
            new_match = re.search(K, S[index:])
            if new_match:
                print(f'{(new_match.start()+index, new_match.end()-1+index,)}')
                index+=1
            index+=1
    else:
        print((-1,-1))


if __name__ == "__main__":
    K = 'aa'
    S = 'aaadaa'
    get_index(K,S)