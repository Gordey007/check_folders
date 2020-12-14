import os
import time

path = r'C:\Users\vasilyevgv56\AppData\Local\Google\Chrome\User Data\Default\Extension'

extensions = os.listdir(path)

print(extensions)

a = os.path.getatime(path)
b = os.path.getmtime(path)
c = os.path.getctime(path)

for extension in extensions:
    print('Расширение - ', extension)
    print('Время создания (Windows) - ', time.ctime(os.path.getctime(path + '\\' + extension)))
    print('Время последнего изменения - ', time.ctime(os.path.getmtime(path + '\\' + extension)))
    print('Время последнего доступа - ', time.ctime(os.path.getatime(path + '\\' + extension)))
    print('')

# print([time.ctime(x) for x in [a, b, c]])

# print(time.ctime(1209600000))
