import backtrader

# Create a Strategy
class TestStrategy(backtrader.Strategy):

    def log(self, txt, dt=None):
        '''Logging function for this strat'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # keep refernce to close line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.order = None

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return 

        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('Buy Executed {}'.format(order.executed.price))
            elif order.issell():
                self.log('Sell Executed{}'.format(order.executed.price))

            self.bar_executed = len(self)

        self.order = None

    # #long only
    # def next(self):
    #     # log closing price of the series from the reference
    #     self.log('Close, %.2f' % self.dataclose[0])

    #     if self.order:
    #         return

    #     if not self.position:
    #         #current close less than previous close
    #         if self.dataclose[0] < self.dataclose[-1]:

    #             #previous close less than the previous close
    #             if self.dataclose[-1] < self.dataclose[-2]:

    #                 #buy - basically we buying the dip
    #                 self.log('Buy Created, %.2f' % self.dataclose[0])
    #                 self.buy()

    # real code to buy and sell after a day
    def next(self):
        # log closing price of the series from the reference
        self.log('Close, %.2f' % self.dataclose[0])

        if self.order:
            return

        if not self.position:
            #current close less than previous close
            if self.dataclose[0] < self.dataclose[-1]:

                #previous close less than the previous close
                if self.dataclose[-1] < self.dataclose[-2]:

                    #buy - basically we buying the dip
                    self.log('Buy Created, %.2f' % self.dataclose[0])
                    self.buy()
        else:
            if len(self) >= (self.bar_executed + 5):
                self.log('Sell Created {}'.format(self.dataclose[0]))
                self.order = self.sell()