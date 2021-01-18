import streamlit as st
import yfinance as yf
import pandas as pd
# hash'#' defines for heading
# **code** for bold of the text


st.write("""

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |
[Got  to google page](https://www.google.com)
# Simple Web Application
## Hello World
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

 hello **welcome** to my **web application**. nice to meet you
Inline `code` has `back-ticks around` it.
 """)

st.write("""
```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```
 
```python
s = "Python syntax highlighting"
print s
```
 
```
No language indicated, so no syntax highlighting. 
But let's throw in a <b>tag</b>.
```
""")



st.write("""
[ALL MARKDOWN CHEATSHEETS](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
""")

tickersym='GOOGL'

tickerdata=yf.Ticker(tickersym)
print("tick",tickerdata)
tickerdf=tickerdata.history(period='2d',start='2010-5-31',end='2020-5-31')
print(tickerdf)
print(tickerdf.Close)
print(tickerdf.Volume)
st.line_chart(tickerdf.Close)
st.line_chart(tickerdf.Volume)





