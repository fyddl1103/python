Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> s = pd.Series([0.0, 3.6, 2.0, 5.6, 4.2, 8.0]) # 리스트로 시리즈 생성
>>> ㄴ
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    ㄴ
NameError: name 'ᄂ' is not defined
>>> s
0    0.0
1    3.6
2    2.0
3    5.6
4    4.2
5    8.0
dtype: float64
>>> s[0]
0.0
>>> # Series ; 인덱스 처리가 된 1차원 벡터 형태의 자료형. 시계열데이터
>>> s.index = pd.Index([6,7,8,9,10,11])
>>> s.index.name = 'MY_IDX'
>>> s
MY_IDX
6     0.0
7     3.6
8     2.0
9     5.6
10    4.2
11    8.0
dtype: float64
>>> s.name = 'MY_SERIES'
>>> s
MY_IDX
6     0.0
7     3.6
8     2.0
9     5.6
10    4.2
11    8.0
Name: MY_SERIES, dtype: float64
>>> s[6.5] = 11
>>> s
MY_IDX
6.0      0.0
7.0      3.6
8.0      2.0
9.0      5.6
10.0     4.2
11.0     8.0
6.5     11.0
Name: MY_SERIES, dtype: float64
>>> s2 = pd.Series([6.7,3.2], index=[6.3, 10.5])
>>> s.append(s2)
6.0      0.0
7.0      3.6
8.0      2.0
9.0      5.6
10.0     4.2
11.0     8.0
6.5     11.0
6.3      6.7
10.5     3.2
dtype: float64
>>> s
MY_IDX
6.0      0.0
7.0      3.6
8.0      2.0
9.0      5.6
10.0     4.2
11.0     8.0
6.5     11.0
Name: MY_SERIES, dtype: float64
>>> s = s.append(s2)
>>> s
6.0      0.0
7.0      3.6
8.0      2.0
9.0      5.6
10.0     4.2
11.0     8.0
6.5     11.0
6.3      6.7
10.5     3.2
dtype: float64
>>> s.index[-1]
10.5
>>> s.values[-1]
3.2
>>> s.loc[10]
4.2
>>> s.loc[6.0] # 인덱스에 해당하는 값
0.0
>>> s.iloc[10]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    s.iloc[10]
  File "C:\Users\fyd11\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\indexing.py", line 895, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "C:\Users\fyd11\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\indexing.py", line 1501, in _getitem_axis
    self._validate_integer(key, axis)
  File "C:\Users\fyd11\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\indexing.py", line 1444, in _validate_integer
    raise IndexError("single positional indexer is out-of-bounds")
IndexError: single positional indexer is out-of-bounds
>>> s.values[:]
array([ 0. ,  3.6,  2. ,  5.6,  4.2,  8. , 11. ,  6.7,  3.2])
>>> s.iloc[:]
6.0      0.0
7.0      3.6
8.0      2.0
9.0      5.6
10.0     4.2
11.0     8.0
6.5     11.0
6.3      6.7
10.5     3.2
dtype: float64
>>> # values ; 결과값이 복수 개일때 배열로 반환, iloc ; 시리즈로 반환
>>> s.drop(0.0)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s.drop(0.0)
  File "C:\Users\fyd11\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\series.py", line 4443, in drop
    return super().drop(
  File "C:\Users\fyd11\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\generic.py", line 4153, in drop
    obj = obj._drop_axis(labels, axis, level=level, errors=errors)
  File "C:\Users\fyd11\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\generic.py", line 4188, in _drop_axis
    new_axis = axis.drop(labels, errors=errors)
  File "C:\Users\fyd11\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\indexes\base.py", line 5591, in drop
    raise KeyError(f"{labels[mask]} not found in axis")
KeyError: '[0.] not found in axis'
>>> s.drop(6.0) # 삭제하고싶은 값의 인덱스
7.0      3.6
8.0      2.0
9.0      5.6
10.0     4.2
11.0     8.0
6.5     11.0
6.3      6.7
10.5     3.2
dtype: float64
>>> s
6.0      0.0
7.0      3.6
8.0      2.0
9.0      5.6
10.0     4.2
11.0     8.0
6.5     11.0
6.3      6.7
10.5     3.2
dtype: float64
>>> s = s.drop(6.0)  # 드롭한거 반영하고 싶음
>>> s
7.0      3.6
8.0      2.0
9.0      5.6
10.0     4.2
11.0     8.0
6.5     11.0
6.3      6.7
10.5     3.2
dtype: float64
>>> s.describe()
count     8.000000
mean      5.537500
std       2.946639dd
min       2.000000
25%       3.500000
50%       4.900000
75%       7.025000
max      11.000000
dtype: float64
>>> import matplotlib.pyplot as plt
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
>>> import matplotlib.pyplot as plt
>>> plt.title("ELLIOTT_WAVE")
Text(0.5, 1.0, 'ELLIOTT_WAVE')
>>> plt.plot(s, 'bs--') # 시리즈를 bs--(푸른 사각형과 점선) 형태로 출력
[<matplotlib.lines.Line2D object at 0x00000154371A64C0>]
>>> plt.xticks(s.index)
([<matplotlib.axis.XTick object at 0x00000154371953D0>, <matplotlib.axis.XTick object at 0x00000154371953A0>, <matplotlib.axis.XTick object at 0x0000015437177EB0>, <matplotlib.axis.XTick object at 0x00000154391BFFA0>, <matplotlib.axis.XTick object at 0x00000154391DD4F0>, <matplotlib.axis.XTick object at 0x00000154391DD1F0>, <matplotlib.axis.XTick object at 0x00000154391DDBB0>, <matplotlib.axis.XTick object at 0x00000154391E2100>], [Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, '')])
>>> plt.yticks(s.values)
([<matplotlib.axis.YTick object at 0x0000015437195C70>, <matplotlib.axis.YTick object at 0x0000015437195850>, <matplotlib.axis.YTick object at 0x000001543718E670>, <matplotlib.axis.YTick object at 0x00000154391E2B80>, <matplotlib.axis.YTick object at 0x00000154391EB0D0>, <matplotlib.axis.YTick object at 0x00000154391EB5E0>, <matplotlib.axis.YTick object at 0x00000154391EBAF0>, <matplotlib.axis.YTick object at 0x00000154391E2670>], [Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, ''), Text(0, 0, '')])
>>> plt.grid(True)
>>> plt.show()


