import sys
import os
import os.path
from shutil import copyfile


"""
Source code shamelessly stolen from https://github.com/PepijnMC/Minecraft/blob/master/Dehash/dehash.py

Note that this is current not in use.

TODO:
    - command line args for specifying version
    - auto update config through minecraft files alone
"""

curr_path = os.getcwd()
default_version = '1.12'

def file_length(file):
    with open(file) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def error_handler(error):
    print(error)
    os.chdir(curr_path)
    log = open('error_log.txt', 'w')
    log.write(error)
    log.close()


def main():
    hash_error = 0
    os.chdir('indexes')
    if len(sys.argv) > 1:
        version = sys.argv[1]
        if 'json' in version:
            indexversion = version
            splitversion = version.split('.')
            version = '%s.%s' % (splitversion[0], splitversion[1])
        else:
            indexversion = version + '.json'
        if os.path.isfile('%s' % indexversion):
            index = open('%s' % (indexversion), 'r')
        else:
            error_handler('Error: Invalid index file!')
            sys.exit()
        length = file_length('%s' % (indexversion)) / 4
    else:
        version = default_version
        index = open('%s.json' % (version), 'r')
        length = file_length('%s.json' % (version)) / 4

    lines = index.readlines()
    print('\nDehashing sound and language files...')
    for line in range(int(length)):
        name = lines[line*4-2]
        if 'minecraft/sounds' in name:
            path = name[22:-5]
            hash = lines[line*4-1][15:-3]
            hashfolder = hash[0:2]
            os.chdir(curr_path)
            if os.path.isdir('objects/%s' % (hashfolder)):
                os.chdir('objects/%s' % (hashfolder))
                if os.path.isfile(hash):
                    folders = path.split('/')
                    sound = folders[-1]
                    del folders[-1]
                    filepath = '/'.join(folders)
                    os.makedirs('%s/_soundfiles/%s/%s' % (curr_path, version, filepath), exist_ok=True)
                    if path == 'json':
                        copyfile('%s/objects/%s/%s' % (curr_path, hashfolder, hash), '%s/_soundfiles/%s/sounds.json' % (curr_path, version))
                    else:
                        copyfile('%s/objects/%s/%s' % (curr_path, hashfolder, hash), '%s/_soundfiles/%s/%s/%s' % (curr_path, version, filepath, sound))
                else:
                    hash_error += 1
            else:
                hash_error += 1

        elif 'minecraft/lang' in name:
            lang = name[20:-5]
            hash = lines[line*4-1][15:-3]
            hashfolder = hash[0:2]
            os.chdir(curr_path)
            if os.path.isdir('objects/%s' % (hashfolder)):
                os.chdir('objects/%s' % (hashfolder))
                if os.path.isfile(hash):
                    os.makedirs('%s/_langfiles/%s' % (curr_path, version), exist_ok=True)
                    copyfile('%s/objects/%s/%s' % (curr_path, hashfolder, hash),'%s/_langfiles/%s/%s' % (curr_path, version, lang))
                else:
                    hash_error += 1
            else:
                hash_error += 1

    print('Done!')
    if hash_error > 1:
        error_handler('Error: %s hashed files were not found! Please launch the Minecraft version from the index file used (the default index file used is from version %s).' % (hash_error,default_version))
    index.close()

if __name__ == "__main__":
    pass
    # main()
