import requests
import time

url = 'https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-rpslog.txt'
results = requests.get(url).text

start = time.time()
a, b, c = 0, 0, 0
i = 0

while i < len(results):
    game = results[i:i+3]
    if game == "SPR"\
            or game == "SRP"\
            or game == "PSR"\
            or game == "PRS"\
            or game == "RSP"\
            or game == "RPS"\
            or game == "SSS"\
            or game == "RRR"\
            or game == "PPP":
        i += 3
    elif game == "SSR"\
            or game == "RRP"\
            or game == "PPS":
        c += 1
        i += 3
    elif game == "SRS"\
            or game == "RPR"\
            or game == "PSP":
        b += 1
        i += 3
    elif game == "RSS"\
            or game == "PRR"\
            or game == "SPP":
        a += 1
        i += 3
    elif game == "SSP"\
            or game == "RRS"\
            or game == "PPR":
        i += 3
        while 1:
            rematch = results[i:i+2]
            i += 2
            if rematch == "SS"\
                    or rematch == "RR"\
                    or rematch == "PP":
                continue
            if rematch == "RS"\
                    or rematch == "PR"\
                    or rematch == "SP":
                a += 1
            else:
                b += 1
            break
    elif game == "SPS"\
            or game == "RSR"\
            or game == "PRP":
        i += 3
        while 1:
            rematch = results[i:i+2]
            i += 2
            if rematch == "SS"\
                    or rematch == "RR"\
                    or rematch == "PP":
                continue
            if rematch == "RS"\
                    or rematch == "PR"\
                    or rematch == "SP":
                a += 1
            else:
                c += 1
            break
    elif game == "PSS"\
            or game == "SRR"\
            or game == "RPP":
        i += 3
        while 1:
            rematch = results[i:i+2]
            i += 2
            if rematch == "SS"\
                    or rematch == "RR"\
                    or rematch == "PP":
                continue
            if rematch == "RS"\
                    or rematch == "PR"\
                    or rematch == "SP":
                b += 1
            else:
                c += 1
            break
        continue
        
        
print(f'{a},{b},{c}')
end = time.time()
print(f'Runtime: {end - start:.4f} seconds')
