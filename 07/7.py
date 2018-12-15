from urllib.request import urlopen


url = 'https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-vekksort.txt'


def subsequence_len(seq):
    N = len(seq)

    P = [None] * (N + 1)
    M = [None] * N

    L = 0
    for i in range(1, N):
        low = 1
        high = L

        while low <= high:
            mid = (low + high) // 2
            if seq[M[mid]] <= seq[i]:
                low = mid + 1
            else:
                high = mid - 1

        newL = low
        P[i] = M[newL - 1]
        M[newL] = i
        if newL > L:
            L = newL

    return L


nums = []
for line in urlopen(url):
    nums.append(int(line))
print(subsequence_len(nums))
