import os
import glob


def get_stats():
    stats = dict()
    for file in glob.glob('*.py'):
        stats[file] = os.stat(file)
    return stats

stats = get_stats()
print(stats)

print('--------------------')

stats2 = {file: os.stat(file) for file in glob.glob('*.py')}

print(stats2)
