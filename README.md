# Time-Series Price Analysis
- Stock and Bitcoin time-series forecasting using machine learning.
- Long short term memory, Wavenet, LightGBM
- Jul. 7, 2021

---------------------------------
- Time-series forecasting modeling is widely applied in finance. In particular, machine learning methods provide insights that can learn time dynamics in a purely data-driven manner. Deep learning methods such as CNN models, RNN models and Attention-based models can be used to predict time-series prices.
- I will use stock and bitcoin price data to implement some deep learning models that have been widely researched and implemented.
- Forecasting will be conducted using AAPL and BTC prices, which are considered to lead the financial market.

| [Presentation](https://github.com/OH-Seoyoung/Time-Series_Price_Analysis/blob/master/Presentation/20220331_stock_price_forecasting.pdf) |
## Dataset
```
[1] Apple - 10 Year Stock Price History, https://www.kaggle.com/datasets/aleksandrdubrovin/apple-stock-price-history
[2] Analyzing and Predicting Bitcoin pricing trend, https://www.kaggle.com/datasets/surajjha101/analyzing-and-prediction-of-bitcoin-pricing
```
## Modeling (in progress...)
### 1. Long short term memory
- 역시 근본
- 30 epoch

### 2. Wavenet
- Fast (10 epoch)
- Skip connection 이후 original Wavenet 구조와 같이 Relu->Conv 구조를 사용했으나 성능이 좋지않아 Dense로 대체

### 3. LightGBM
- Very fast
- Tree-base modeling 이므로 scaling 의미 X

## References
```
[1] Lim, Bryan, and Stefan Zohren. "Time-series forecasting with deep learning: a survey." Philosophical Transactions of the Royal Society A 379.2194 (2021): 20200209.
[2] Sun, Xiaolei, Mingxi Liu, and Zeqian Sima. "A novel cryptocurrency price trend forecasting model based on LightGBM." Finance Research Letters 32 (2020): 101084.
```


