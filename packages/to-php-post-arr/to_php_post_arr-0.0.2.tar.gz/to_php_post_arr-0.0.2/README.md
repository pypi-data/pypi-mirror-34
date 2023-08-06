
# Convert python dict/list/nested to PHP Array like urlencoded string

> [中文说明](https://github.com/vikyd/to_php_post_arr/blob/master/README_cn.md)


## Install

```sh
pip install to_php_post_arr
```


## Usage


```py
from to_php_post_arr.convert import recursive_urlencode

a = [1, 2]
print(recursive_urlencode(a))
# 0=1&1=2


a2 = (1, '2')
print(recursive_urlencode(a2))
# 0=1&1=2


b = {'a': 11, 'b': 'foo'}
print(recursive_urlencode(b))
# a=11&b=foo


c = {'a': 11, 'b': [1, 2]}
print(recursive_urlencode(c))
# a=11&b[0]=1&b[1]=2


d = [1, {'a': 11, 'b': 22}]
print(recursive_urlencode(d))
# 0=1&1[a]=11&1[b]=22


e = {'a': 11, 'b': [1, {'c': 123}, [3, 'foo']]}
print(recursive_urlencode(e))
# a=11&b[0]=1&b[1][c]=123&b[2][0]=3&b[2][1]=foo

f = ['测试中文']
print(recursive_urlencode(f))
# test chinese 
# 0=%E6%B5%8B%E8%AF%95%E4%B8%AD%E6%96%87

```

## PHP urlencoded Array Data
- http://php.net/manual/en/faq.html.php#faq.html.arrays



## Test
```sh
cd tests

python -m unittest test_convert
```



## Thanks 
- code: https://stackoverflow.com/a/4014164/2752670
