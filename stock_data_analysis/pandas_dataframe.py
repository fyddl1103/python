Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> df = pd.DataFrame({'KOSPI' : [1915,1961,2026,2467,2541], 'KOSDAQ' : [542,682, 632, 798, 900]})
>>> df
   KOSPI  KOSDAQ
0   1915     542
1   1961     682
2   2026     632
3   2467     798
4   2541     900
>>> df = pd.DataFrame({'KOSPI' : [1915,1961,2026,2467,2541], 'KOSDAQ' : [542,682, 632, 798, 900]}, index=[2014, 2015, 2016, 2017, 2018])
>>> df
      KOSPI  KOSDAQ
2014   1915     542
2015   1961     682
2016   2026     632
2017   2467     798
2018   2541     900
>>> df.describe()
             KOSPI      KOSDAQ
count     5.000000    5.000000
mean   2182.000000  710.800000
std     297.729743  140.474909
min    1915.000000  542.000000
25%    1961.000000  632.000000
50%    2026.000000  682.000000
75%    2467.000000  798.000000
max    2541.000000  900.000000
>>> df.info()  # 인덱스 정보, 칼럼 정보, 메모리 사용량 등
<class 'pandas.core.frame.DataFrame'>
Int64Index: 5 entries, 2014 to 2018
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   KOSPI   5 non-null      int64
 1   KOSDAQ  5 non-null      int64
dtypes: int64(2)
memory usage: 120.0 bytes
>>> 
>>> 
>>> # 시리즈를 이용한 데이터프레임 생성
>>> kospi = pd.Series([1915, 1961, 2026, 2467, 2541], index=[2014,2015,2016,2017,2018], name='KOSPI')
>>> kospi
2014    1915
2015    1961
2016    2026
2017    2467
2018    2541
Name: KOSPI, dtype: int64
>>> kosdaq = pd.Series([1915,1961,2026,2467,2541], index=[2014, 2015, 2016, 2017, 2018], name='KOSDAQ')
>>> kosdaq
2014    1915
2015    1961
2016    2026
2017    2467
2018    2541
Name: KOSDAQ, dtype: int64
>>> df = pd.DataFrame({kospi.name = kospi, kosdaq.name = kosdaq})
SyntaxError: invalid syntax
>>> df
      KOSPI  KOSDAQ
2014   1915     542
2015   1961     682
2016   2026     632
2017   2467     798
2018   2541     900
>>> df2 = pd.DataFrame({kospi.name : kospi, kosdaq.name : kosdaq})
>>> df2
      KOSPI  KOSDAQ
2014   1915    1915
2015   1961    1961
2016   2026    2026
2017   2467    2467
2018   2541    2541
>>> 
>>> 
>>> # 리스트를 이용한 데이터프레임 생성
>>> columns = ['KOSPI', 'KOSDAQ']
>>> index = [2014, 2015, 2016, 2017, 2018]
>>> rows = []
>>> rows.append([1915, 542])
>>> rows.append([2000, 600])
>>> rows.append([2100, 630])
>>> rows.append([2300, 700])
>>> rows.append([3000, 1000])
>>> df3 = pd.DataFrame(rows, columns : columns, index : index)
SyntaxError: invalid syntax
>>> df3 = pd.DataFrame(rows, columns = columns, index = index)
>>> df3
      KOSPI  KOSDAQ
2014   1915     542
2015   2000     600
2016   2100     630
2017   2300     700
2018   3000    1000
>>> 
>>> for i in df.index:
	print(i, df['KOSPI'][i], df['KOSDAQ'][i])

	
2014 1915 542
2015 1961 682
2016 2026 632
2017 2467 798
2018 2541 900
>>> 
>>> for row in df.itertuples():
	print(row
	      )

	
Pandas(Index=2014, KOSPI=1915, KOSDAQ=542)
Pandas(Index=2015, KOSPI=1961, KOSDAQ=682)
Pandas(Index=2016, KOSPI=2026, KOSDAQ=632)
Pandas(Index=2017, KOSPI=2467, KOSDAQ=798)
Pandas(Index=2018, KOSPI=2541, KOSDAQ=900)
>>> 
>>> for row in df.itertuples():
	print(row[0], row[1], row[2])

	
2014 1915 542
2015 1961 682
2016 2026 632
2017 2467 798
2018 2541 900
>>> 

>>> for idx, row in df.iterrows():
	print(idx, row[0], row[1])

	
2014 1915 542
2015 1961 682
2016 2026 632
2017 2467 798
2018 2541 900
>>> 
>>> # itertuples() 가 iterrows()보다 속도면에서 나음
>>> 