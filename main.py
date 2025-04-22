from zipfile import ZipFile





def zip():
    with ZipFile('data.zip', 'w') as zip1:

        zip1.write("/Users/kareenaarora/Desktop/beg pyt/script1")

if __name__ == '__main__':
    zip()