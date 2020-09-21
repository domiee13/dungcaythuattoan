# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# domain_name("http://github.com/carbonfive/raygun") == "github" 
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"

import re

def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')

def domain_name1(url):
    return re.search(r'(?:\.|\/)([A-Za-z_-]+)\.',url)[1]

print(domain_name1('http://github.com/carbonfive/raygun'))

def domain_name2(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]