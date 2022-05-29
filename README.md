# Algorithmic Trading
This repository serve as the code base for the algorithmic trading projects done as part of the MSCFE Econometrics class at Worldquant University. Trading strategy were based on various time series regression models.  
### Baseline evaluation
Base on the regression results, we conduct various baseline evaluation of the predict results based on the following simple heuristic:
*   Train models over all previous returns 
*   Using the models to predict next day returns
*   If the predicted returns for next day is negative, short the stock. If postive, long the stock
### Results
Based on the simple heuristic, we evaluate different trading prediction models as described 

![Untitled](https://user-images.githubusercontent.com/48897477/170873232-987c60b5-43f9-4575-96d2-6f1fc96e6b90.png)
