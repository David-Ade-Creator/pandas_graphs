import pandas as pd
import matplotlib.pyplot as plt

automakers = pd.read_csv("Largest automakers by market capitalization.csv", index_col=0)
automakers["Name"] = automakers["Name"].astype(str)
plt.figure()
plt.scatter(automakers["country"], automakers['marketcap'])
plt.show()

# plotting a histogram for United States automakers
US_automakers = automakers[automakers["country"] == "US"]
plt.figure()
plt.bar(US_automakers["Symbol"], US_automakers['marketcap'], align='center')
# plt.pie(US_automakers['marketcap'], labels= US_automakers["Name"])
plt.xlabel('AutoMobile companies in United States')
plt.ylabel('MarketCap')
plt.show()

# Plotting a histogram for japan automakers
Japan_automakers = automakers[automakers["country"] == "Jap"]
plt.figure()
plt.bar(Japan_automakers["Symbol"], Japan_automakers['marketcap'], align='center')
plt.xlabel('AutoMobile companies in Japan')
plt.ylabel('MarketCap')
plt.show()

# Plotting a histogram for Germany automakers
Germany_automakers = automakers[automakers["country"] == "Ger"]
plt.figure()
plt.bar(Germany_automakers["Symbol"], Germany_automakers['marketcap'], align='center')
plt.xlabel('AutoMobile companies in Germany')
plt.ylabel('MarketCap')
plt.show()

# Plotting a histogram for China automakers
China_automakers = automakers[automakers["country"] == "Chi"]
plt.figure()
plt.bar(China_automakers["Symbol"], China_automakers['marketcap'], align='center')
plt.xlabel('AutoMobile companies in China')
plt.ylabel('MarketCap')
plt.show()

