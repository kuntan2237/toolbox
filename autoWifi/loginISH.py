#! /usr/bin/python

import sys
import requests

if (len(sys.argv) != 3):
    sys.exit(-1)
else:
    username=sys.argv[1]
    password=sys.argv[2]

url="https://wlan.ct10000.com/authServlet"
headers = {
    'Host':'wlan.ct10000.com',
    'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'en-US,en;q=0.5',
    'Accept-Encoding':'gzip, deflate',
    'Referer':'https://wlan.ct10000.com/style/ish/index.jsp?paramStr=0UvdVfQabJ%2FgHWbQiWDkWrJw%2FbsTgRU2yzVuGAfwJ6c1kKMnDs0os2Ma5jLbpXXQkvrE6dPE6GxbHZHsVdnb7XE6hO3gimAH4Y4GhpLrKnsxfL2piZNGY6DKDuk78%2BicdSjB3XtkezP9ABwxyZSUZbrwyKg6%2F2NxZl4RlHVQPjfSsFi8LLSaqoEkwS0xOkDDbc2JjmHnXaEwSWA9bbgn4cMObIBTFPHODgeeABhBVBOHXONLhsGxvhUZnp3J3TWLImoTwjBrolWZsZ%2FkDWlXlPYQ0QGH2toL%2Fs7PovpcMKAkASIuFsNJX0mGrTsNekkV25voXf6AXHr7tvTXtqTf52uPnYIsQvbxK7wH8ye%2BXJTq4PAOSFf5yImMXqvNK30u',
    'Cookie':'JSESSIONID=D8D12868B270817764E25B49B529C456',
    'Connection':'keep-alive'
}
postData = {
    'paramStr':"0UvdVfQabJ/gHWbQiWDkWrJw/bsTgRU2yzVuGAfwJ6c1kKMnDs0os2Ma5jLbpXXQkvrE6dPE6GxbHZHsVdnb7XE6hO3gimAH4Y4GhpLrKnsxfL2piZNGY6DKDuk78+icdSjB3XtkezP9ABwxyZSUZbrwyKg6/2NxZl4RlHVQPjfSsFi8LLSaqoEkwS0xOkDDbc2JjmHnXaEwSWA9bbgn4cMObIBTFPHODgeeABhBVBOHXONLhsGxvhUZnp3J3TWLImoTwjBrolWZsZ/kDWlXlPYQ0QGH2toL/s7PovpcMKAkASIuFsNJX0mGrTsNekkV25voXf6AXHr7tvTXtqTf52uPnYIsQvbxK7wH8ye+XJTq4PAOSFf5yImMXqvNK30u",
    'paramStrEnc':'%2FQAcMcmUlGW68MioOv9jcasVMMu21cFgORAqnf8CSTSW9PFlihv28hKXM9DCp9yB3MjzH3mYh8E7tcDDHtSHNZ2LVhWcKTCsMtcALV584ok42sCx7rv9mt7mN1ihepXhVi%2BFN0zFJQgxZh%2B1RhV3yeOD84DE8RCAXTS5NCMZ4%2Fpjsvf0DFzVe%2FKuzlhIFzgYIfNlRIoIoROEiOcq%2FJVMVYHIgSTeJMf66KixuVrM1XauqdjywHN%2Fu5OB1X0ADzoOpNesjcE490%2BDtxUeXNfhO82uEOIebuscOlv3wxE0v4Yp1MMO6k08U4PEaMLJHMmOWaxsXG7wZdhVZoquICuol5Auzwy9VLaeJO4RGiOPjXok%2BgZ0L3wTmJXfzaqdCZ1DP%2Femlits0GJ%2F5F31J%2FpOyw%3D%3D',
    'province':'telecom.dynamic@ish',
    'prefix':"NE",
    'logintype':"2",
    'UserName':username,
    'PassWord':password
}

req = requests.post(url, data=postData, headers=headers)
sys.exit(0)
