# RNN-QFFTS:

Explore the cutting edge of financial technology with our Quantum Finance Forecast and Trading System. This Git repository houses advanced algorithms and models harnessing quantum computing principles to revolutionize financial forecasting and trading strategies. Stay ahead of the market with this innovative and powerful tool for quantitative analysis and decision-making.

# Description 

Welcome to the Quantum Finance Forecast and Trading System, a groundbreaking repository at the intersection of quantum computing and financial technology. This comprehensive platform is designed to redefine how we approach forecasting and trading in the dynamic world of finance.

# Vision And Mission 

**Vision:**
To be the forefront catalyst in transforming the financial landscape by pioneering quantum-powered innovations. Our vision is to usher in a new era where sophisticated technology and quantum computing redefine the boundaries of financial forecasting and trading, unlocking unprecedented insights and opportunities for our users.

**Mission:**
Our mission is to empower financial professionals, researchers, and enthusiasts with state-of-the-art tools that harness the potential of quantum computing. We strive to provide a comprehensive Quantum Finance Forecast and Trading System that goes beyond conventional methods, offering advanced algorithms, customizable modules, and real-time market insights. Through continuous research, development, and collaboration, our mission is to contribute to the evolution of financial technology and empower users to make informed, strategic decisions in the ever-changing world of finance.

### Features:

1. **Quantum-Powered Algorithms:**
   Leverage the capabilities of quantum computing for enhanced data processing, enabling more sophisticated and precise financial predictions.

2. **Advanced Forecasting Models:**
   Utilize state-of-the-art predictive models that go beyond traditional methods, incorporating quantum principles to analyze market trends and make informed forecasts.

3. **Trading Strategies Optimization:**
   Benefit from advanced optimization algorithms that dynamically adjust trading strategies based on real-time market conditions, maximizing returns and minimizing risks.

4. **Machine Learning Integration:**
   Seamlessly integrate machine learning techniques to adapt and improve the system's performance over time, enhancing its ability to adapt to evolving market dynamics.

5. **Real-Time Market Data Analysis:**
   Access and analyze real-time market data efficiently, ensuring timely decision-making and responsiveness to rapidly changing financial landscapes.

6. **User-Friendly Interface:**
   Experience a user-friendly interface that provides intuitive access to powerful quantum finance tools, making it accessible to both seasoned professionals and those new to the field.

7. **Customizable Modules:**
   Tailor the system to your specific needs with modular components, allowing for easy customization and adaptation to various financial scenarios and trading preferences.

8. **Security and Privacy:**
   Prioritize the security and privacy of your financial data with robust encryption and protection measures, ensuring the confidentiality of sensitive information.

### How to Use:

1. **Clone the Repository:**
   Get started by cloning the Quantum Finance Forecast and Trading System repository to your local environment.

2. **Install Dependencies:**
   Follow the provided instructions to install the necessary dependencies and libraries required for seamless execution.

3. **Explore Examples:**
   Dive into the repository's examples and documentation to understand how to implement various quantum-powered financial models and trading strategies.

4. **Contribute and Collaborate:**
   Contribute to the development of this innovative system or collaborate with other users to enhance its capabilities and applicability in diverse financial contexts.

Empower your financial endeavors with the Quantum Finance Forecast and Trading System, where cutting-edge technology meets the intricacies of the financial world. Revolutionize your approach to forecasting and trading by embracing the quantum advantage.


## Background & Abstrct

With average global trading transaction amounts exceeding 5 tril-lion dollars per day, foreign exchange (FOREX) is one of the largest financial markets in the world. With so much competition, finding a competitive ad-vantage, both through an intelligent financial forecasting systems and trad-ing strategy, can be highly effective and extremely profitable. With the adop-tion of the latest R&D on Quantum Finance Theory (QFT), we propose to build a more effective prediction and trading algorithm to better handle the highly chaotic and complex foreign exchange market. It is for this reason we put forward a novel Recurrent Neural Network based Quantum Finance Forecast and Trading System (RNN-QFFTS) for neural network prediction in tandem with the employment of a new kind of financial indicator called Quantum Price Level (QPL). From the experimental perspective, we com-pare the performance of 3 prediction models: FFBP, RNN, and RNN-QFFTS. Using the Meta Trader (MT) platform, we analyzed the previous 2048 days of daily trading data for each forex product to predict the following day’s open, high, low, and close. Utilizing our RNN-QFFTS, we then compare 3 trading algorithms: Moving Average with RSI (Relative Strength Index), Moving Average with RSI and QPL, and Moving Average with RSI and QPL integrated with our prediction. We find that QPL helps to accelerate gradient substantially which enabled us to handle a greater number of products in a smaller time period. With the application of QPL, in cooperation with major financial indicators, RNN-QFFTS achieves promising success rate in terms of trades and profitability. With the implementation of RNN-QFFTS, we were able to gauge prime times for investing occurring, at most, once a day or every other day. This prime time lowered the risk we had when engaging in trades and has the potential to increase the profitability substantially as compared to the traders not using QPL indicators or financial prediction re-sults for trading.

Keywords: Recurrent Neural Network, Quantum Finance, Quantum Price Level, Financial Forecasting, Intelligent Trading.

## Check the Performance
a. Prediction Low VS. Actual Low Price on a 200 days' real testing set
>  Testing Set in /Project_Data/.
>  Loss Steps and Prediction VS. Actual Graph in /Preciction_Results/.


b. A trading algorithm with return rate of about 15%/M is developed, according to prediction
>  An account statement for a half month is listed in ./Trading_Experiment_Result.htm 


## To reproduce prediction result:

0. Python version >= 3.6 (depend on your hardware requirement), tensorflow (CPU version only)>= 1.9.0 (GPU version to be defined), </br>
Install MateTrader4

1. To Collect financial Products' data
> Run /data_retrive/QF_peoject.mq4 on MT4

2. Mordify data storage setting with your own configuration
> Change 3 directories, data_add, prediction_add and model_add, in FFBP_L2, RNN_L2 or QPL_L2 to directories store .csv data, prediction results and network parameter

3. To train the model
> Run .py programs e.g.normal_distribution_QFFTS.py is the best performed ones

4. To get prediction for today
> Enable "continue" in codes, e.g. line 179 FFBP_l2 , and run again

5. Selecting most valuable features with genetic algorithm
> Run feature_selection.py

# Aknowledgement 

We extend our heartfelt gratitude to all individuals and organizations who have contributed to the realization of the Quantum Finance Forecast and Trading System. Your dedication, expertise, and collaborative spirit have been instrumental in shaping this cutting-edge platform.

Special thanks to the developers, researchers, and quantum computing experts whose tireless efforts have fueled the creation of advanced algorithms and models. Your commitment to pushing the boundaries of financial technology is truly commendable.

We also appreciate the broader community of users and contributors who have provided valuable feedback, insights, and suggestions. Your engagement has played a crucial role in refining and enhancing the system.

This project wouldn't be possible without the continuous support from our partners and stakeholders. Your belief in the potential of quantum computing in finance has been a driving force behind our pursuit of excellence.

As we embark on this transformative journey, we acknowledge and appreciate the collective effort that has brought the Quantum Finance Forecast and Trading System to fruition. Together, we look forward to shaping the future of finance through innovation, collaboration, and technological advancement.

QFFTS TEAM
