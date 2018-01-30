from flask import Flask

list = ['abc siddique', 'def-456', 'ghi-789', 'xyz siddique','123 siddique']
print filter(lambda x: 'siddique' in x, list)
