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
#	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
	'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language':'en-US,en;q=0.5',
	'Accept-Encoding':'gzip, deflate',
#	'Referer':'https://wlan.ct10000.com/style/ish_fx/index.jsp?paramStr=9M%2B7JzF%2B8VNrE2IAvqV2FUFMyVEsn38h6RiF2%2BUe4X%2Fgy5aVxMTet3iCCI4gVC0cyO9XDXEL6%2BXA%0Af8S8vuXM2xf1VfnwK3JnVU7wiqRBCEsUjfVEM9AiH8K02%2FHAhUeIhPirem6uuy8IT07tav4gmkV3%0AYaJk2R6lnDwPKifC6mhQ3Pw%2FrAA2CIdEnSjJHIanDydadV%2FXXxV7OUD5xlt6Cq0VelFWbh19snYr%0Awu5oone9RGp3KyugpowSZ90fBst%2FdNWJXUBe7Pq8TI0EIwwXy6FnTJaemMzhUEi7Smre0rpXQ8dY%0AwzJ2yR%2FDTsbUeRQ4dJkLUc5xW9DRy1qxD4ZdBwjzWt6IyzcsrzL6A3rvZv0ksNYZykxiJkzOTTFH%0AyJtZ7Y42NzinqDs%3D',
    'Referer':'https://wlan.ct10000.com/style/ish/index.jsp?paramStr=0UvdVfQabJ%2FgHWbQiWDkWrJw%2FbsTgRU2yzVuGAfwJ6c1kKMnDs0os2Ma5jLbpXXQkvrE6dPE6GxbHZHsVdnb7XE6hO3gimAH4Y4GhpLrKnsxfL2piZNGY6DKDuk78%2BicdSjB3XtkezP9ABwxyZSUZbrwyKg6%2F2NxZl4RlHVQPjfSsFi8LLSaqoEkwS0xOkDDbc2JjmHnXaEwSWA9bbgn4cMObIBTFPHODgeeABhBVBOHXONLhsGxvhUZnp3J3TWLImoTwjBrolWZsZ%2FkDWlXlPYQ0QGH2toL%2Fs7PovpcMKAkASIuFsNJX0mGrTsNekkV25voXf6AXHr7tvTXtqTf52uPnYIsQvbxK7wH8ye%2BXJTq4PAOSFf5yImMXqvNK30u',
	#'Cookie':'JSESSIONID=DAEED413DE820C9F81CBE1024BA13D7A',
	'Cookie':'JSESSIONID=D8D12868B270817764E25B49B529C456',
	'Connection':'keep-alive'
}
postData = {
#    'paramStr':"9M+7JzF+8VNrE2IAvqV2FUFMyVEsn38h6RiF2+Ue4X/gy5aVxMTet3iCCI4gVC0cyO9XDXEL6+XAf8S8vuXM2xf1VfnwK3JnVU7wiqRBCEsUjfVEM9AiH8K02/HAhUeIhPirem6uuy8IT07tav4gmkV3YaJk2R6lnDwPKifC6mhQ3Pw/rAA2CIdEnSjJHIanDydadV/XXxV7OUD5xlt6Cq0VelFWbh19snYrwu5oone9RGp3KyugpowSZ90fBst/dNWJXUBe7Pq8TI0EIwwXy6FnTJaemMzhUEi7Smre0rpXQ8dYwzJ2yR/DTsbUeRQ4dJkLUc5xW9DRy1qxD4ZdBwjzWt6IyzcsrzL6A3rvZv0ksNYZykxiJkzOTTFHyJtZ7Y42NzinqDs=",
	'paramStr':"0UvdVfQabJ/gHWbQiWDkWrJw/bsTgRU2yzVuGAfwJ6c1kKMnDs0os2Ma5jLbpXXQkvrE6dPE6GxbHZHsVdnb7XE6hO3gimAH4Y4GhpLrKnsxfL2piZNGY6DKDuk78+icdSjB3XtkezP9ABwxyZSUZbrwyKg6/2NxZl4RlHVQPjfSsFi8LLSaqoEkwS0xOkDDbc2JjmHnXaEwSWA9bbgn4cMObIBTFPHODgeeABhBVBOHXONLhsGxvhUZnp3J3TWLImoTwjBrolWZsZ/kDWlXlPYQ0QGH2toL/s7PovpcMKAkASIuFsNJX0mGrTsNekkV25voXf6AXHr7tvTXtqTf52uPnYIsQvbxK7wH8ye+XJTq4PAOSFf5yImMXqvNK30u",
#    'paramStrEnc':'CE9O7Wr%2BIJpFd2GiZNkepRRC6cujNLJjXDED1FtB5UAn%2Fn4IGzDg83TViV1AXuz6vEyNBCMMF8ug%0A0qNso4FuRdFstj%2FdpprHwmIYP9emmCTUSxIUSH5gAlo3EAIX9As4Uhf%2FxDJRePPAIhFsvdW2nGhV%0ARsjfcjeFaxVV3XxkASg8Jjm89iJwTPj8rnfI0j%2F%2Bb9kY4EHLaaOqLEPwatzaKDob8jf0MA%2BZbshC%0AHlAAc%2FjUWqx584Xi94XLlunQtMWdFoJ3PE0UqcrSf%2FmmBguEeHs3CbkxfsndUOjD54xL3Fv5pgt0%0ARhCJBEIvutmGGJt1tdM9W1XHgWoUJMKjM%2Bc2IDkHE2p%2FFUNuK8%2ByfdFq%2FE1dVxbwmjXFh6%2BzqKzp%0AQ8v9PWocRVyZHY%2B%2BCMqRVoa43N%2FsZK51fv67',
    'paramStrEnc':'%2FQAcMcmUlGW68MioOv9jcasVMMu21cFgORAqnf8CSTSW9PFlihv28hKXM9DCp9yB3MjzH3mYh8E7tcDDHtSHNZ2LVhWcKTCsMtcALV584ok42sCx7rv9mt7mN1ihepXhVi%2BFN0zFJQgxZh%2B1RhV3yeOD84DE8RCAXTS5NCMZ4%2Fpjsvf0DFzVe%2FKuzlhIFzgYIfNlRIoIoROEiOcq%2FJVMVYHIgSTeJMf66KixuVrM1XauqdjywHN%2Fu5OB1X0ADzoOpNesjcE490%2BDtxUeXNfhO82uEOIebuscOlv3wxE0v4Yp1MMO6k08U4PEaMLJHMmOWaxsXG7wZdhVZoquICuol5Auzwy9VLaeJO4RGiOPjXok%2BgZ0L3wTmJXfzaqdCZ1DP%2Femlits0GJ%2F5F31J%2FpOyw%3D%3D',
    'province':'telecom.dynamic@ish',
    'prefix':"NE",
    'logintype':"2",
    'UserName':username,
    'PassWord':password
}

req = requests.post(url, data=postData, headers=headers)
sys.exit(0)
