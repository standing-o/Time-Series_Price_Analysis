# Time-series price analysis
- Stock and Bitcoin time-series forecasting using deeplearning
- Long short term memory, Wavenet, LightGBM
- Jul. 7, 2021 ~ Present

---------------------------------
- Time-series forecasting modeling is widely applied in finance. In particular, machine learning methods provide insights that can learn time dynamics in a purely data-driven manner. Deep learning methods such as CNN models, RNN models and Attention-based models can be used to predict time-series prices.
- I will use stock and bitcoin price data to implement some deep learning models that have been widely researched and implemented.
- Forecasting will be conducted using APPL and BTC prices, which are considered to lead the financial market.

## Dataset
```
[1] Apple - 10 Year Stock Price History, https://www.kaggle.com/datasets/aleksandrdubrovin/apple-stock-price-history
[2] Analyzing and Predicting Bitcoin pricing trend, https://www.kaggle.com/datasets/surajjha101/analyzing-and-prediction-of-bitcoin-pricing
```
## Modeling
### 1. Long short term memory
- 역시 근본
- 30 epoch
### 2. Wavenet
- faster (10 epoch)
- skip connection 이후 original Wavenet 대로 relu->conv 구조를 사용했으나 좋지않아서 dense로 대체

### 3. LightGBM

## References
```
[1] Lim, Bryan, and Stefan Zohren. "Time-series forecasting with deep learning: a survey." Philosophical Transactions of the Royal Society A 379.2194 (2021): 20200209.
[2] Sun, Xiaolei, Mingxi Liu, and Zeqian Sima. "A novel cryptocurrency price trend forecasting model based on LightGBM." Finance Research Letters 32 (2020): 101084.
```


