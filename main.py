import configparser

config = configparser.ConfigParser()
config.read('config.txt')
data = config['DATABASE']

print(data['HOST'])
print(data['USER'])
print(data['PASSWORD'])
print(data['SCHEMA'])

try:
    print(data['KEY_999'])
except Exception as e:
    print('key not found :' + str(e))
