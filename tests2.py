import time
timeline = []
i = 0

for i in range(5):
    tic = time.perf_counter()
    for i in range(1000):
        f = i
        f = f * f
    toc = time.perf_counter()
    element = float(float(toc)-float(tic))
    timeline.append(element)

for i in range(len(timeline)):
    timeline[i] = round(element,3)*1000

print(timeline)