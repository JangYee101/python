>>> a=1
>>> b=None
>>> c=a if a else 2
>>> c
1
>>> c=a if b else 2
>>> c
2


>>> ord('a')
97
>>> chr(97)
'a'
>>> unichr(97)
u'a'
>>> 'a'
'a'
>>> 'a'.decode('utf-8')
u'a'


>>> import traceback
>>> try:
...     print asdf
... except:
...     traceback.print_exc()
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  NameError: name 'asdf' is not defined


>>> time.time()
1537859784.7381001
>>> datetime.datetime.now()
datetime.datetime(2018, 9, 25, 15, 17, 33, 606735)
>>> datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
'2018-09-25 15:18:08'
>>> datetime.datetime.strptime('2018-09-27 17:30:21', "%Y-%m-%d %H:%M:%S")
datetime.datetime(2018, 9, 27, 17, 30, 21)
>>> time.mktime(time.strptime('2018-09-25 15:18:08', "%Y-%m-%d %H:%M:%S"))
1537859888.0
>>> time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1537859888.0))
'2018-09-25 15:18:08'


>>> a={'a':'你'}
>>> json.dumps(a)
'{"a": "\\u4f60"}'
>>> json.dumps(a, ensure_ascii=False)
'{"a": "\xe4\xbd\xa0"}'
>>> json.loads(json.dumps(a, ensure_ascii=False))
{u'a': u'\u4f60'}


>>> '\t192.168.1.2     \n    '.strip()
'192.168.1.2'


>>> glob.glob('*')
['option_demo.py', 'unittest_demo.py', 'README.txt', 'sql_demo.py', 'ava_demo.py', 'cmd_demo.py', 'loggin_demo.py']
>>> glob.glob('ava*')
['ava_demo.py']
>>> a[0]
'../python/ava_demo.py'
>>> os.path.basename(a[0])
'ava_demo.py'


>>> add_lambda = lambda x : x+x
>>> add_lambda(1)
2
>>> map(add_lambda, [1,2,3,4,5])
[2, 4, 6, 8, 10]
>>> filter(lambda x : x%2==0, [1,2,3,4,5])
[2, 4]
