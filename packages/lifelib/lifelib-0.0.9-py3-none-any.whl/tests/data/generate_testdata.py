import sys, os, math, pickle
from lifelib.projects.simplelife import simplelife


filepath = os.path.join(os.path.dirname(__file__), 'data_simplelife')

if '' not in sys.path:
    sys.path.insert(0, '')

def round_signif(x, digit):
    if x == 0:
        return 0
    else:
        base = int(math.log10(abs(x)))
        return round(x, digit - base - 1)


def generate_data(model):
    data = []
    proj = model.Projection
    for i in range(10, 301, 10):
        data.append(round_signif(proj(i).PV_NetCashflow(0), 10))

    with open(filepath, 'wb') as file:
        pickle.dump(data, file, protocol=4)


if __name__ == '__main__':
    generate_data(simplelife.build())