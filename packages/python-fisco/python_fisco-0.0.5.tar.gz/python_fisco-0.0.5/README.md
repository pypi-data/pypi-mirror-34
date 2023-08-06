# python_fisco

[![CircleCI](https://circleci.com/bb/smapira/python-fisco.svg?style=svg)](https://circleci.com/bb/smapira/python-fisco)

Fisco API wrapper for Python 3.

Inspired by this wrapper written by 'zaifapi'.
 
## Install latest release:

```bash
pip install python-fisco
```

## Usage:

```python
from python_fisco import *
FiscoPublic().get_ticker('btc_jpy')
```

### Public Api

```python
# ticker
from python_fisco import *
FiscoPublic().get_ticker('btc_jpy')

# last_price
FiscoPublic().get_last_price('btc_jpy')

# trades
FiscoPublic().get_trades('btc_jpy')

# depth
FiscoPublic().get_depth('btc_jpy')

```

### Private API

```python
import os
from python_fisco import *
private_api = FiscoPrivate(os.environ.get('FCCE_KEY'), os.environ.get('FCCE_SECRET'))

private_api.get_info()

private_api.get_trade_history()

private_api.get_active_orders()

private_api.trade(currency_pair='btc_jpy', action='ask', price=700000, amount=0.001)

private_api.cancel_order(order_id=1)

private_api.withdraw(currency='btc', address='address', amount=0.001)

private_api.get_deposit_history('btc')

private_api.get_withdraw_history('btc')
```


## See

https://fcce.jp/api-docs
