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
>>> time.mktime(time.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S"))
1537860009.0
>>> time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
'2018-09-25 15:21:12'


>>> a={'a':'你'}
>>> json.dumps(a)
'{"a": "\\u4f60"}'
>>> json.dumps(a, ensure_ascii=False)
'{"a": "\xe4\xbd\xa0"}'
>>> json.loads(json.dumps(a, ensure_ascii=False))
{u'a': u'\u4f60'}


