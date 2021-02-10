import backtrader as bt
from datetime import datetime
from strategies import TestStrategy

cerebro = bt.Cerebro()

startingCapital = 10000
#risking X% of account/trade
riskPerTrade = 50

cerebro.broker.set_cash(startingCapital)

data = bt.feeds.YahooFinanceData(dataname='AAPL',
                                fromdate=datetime(2010, 1, 1),
                                todate=datetime(2020, 12, 31))

cerebro.adddata(data)

cerebro.addstrategy(TestStrategy)

cerebro.addsizer(bt.sizers.PercentSizer, percents=riskPerTrade)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
print('Final Portfolio Profit: %.2f' % (cerebro.broker.getvalue()-startingCapital))
print('Final Portfolio ROI: %.2f' % (cerebro.broker.getvalue()/startingCapital-1))

#if error in plotting: pip install matplotlib==3.2.2
cerebro.plot()