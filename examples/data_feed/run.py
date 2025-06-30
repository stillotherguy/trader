from datetime import datetime
from vnpy.trader.constant import Exchange, Interval
from vnpy.trader.datafeed import get_datafeed
from vnpy.trader.object import HistoryRequest

if __name__ == '__main__':
    datafeed = get_datafeed()

    req = HistoryRequest(
        # 合约代码（示例cu888为米筐连续合约代码，仅用于示范，具体合约代码请根据需求查询数据服务提供商）
        symbol="600519",
        # 合约所在交易所
        exchange=Exchange.SSE,
        # 历史数据开始时间
        start=datetime(2019, 1, 1),
        # 历史数据结束时间
        end=datetime(2021, 1, 20),
        # 数据时间粒度，默认可选分钟级、小时级和日级，具体选择需要结合该数据服务的权限和需求自行选择
        interval=Interval.DAILY
    )

    # 获取k线历史数据
    data = datafeed.query_bar_history(req)
    print(data)
