def extract_region(locale):
    return locale[3:5]
    # return locale.split('_')[1].split('.')[0]


print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR