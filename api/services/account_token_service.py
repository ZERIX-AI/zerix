import logging
import os
from decimal import Decimal

from models.account import *
from models.token import AccountTokenBalance, AccountTokenLog, TokenLogType

logger = logging.getLogger(__name__)

class AccountTokenService:

    @staticmethod
    # TESTED ON 2024-10-14 22:19 GMT
    def load_balance(address: str) -> None | AccountTokenBalance:
        balance = AccountTokenBalance.query.filter_by(address=address).first()
        if not balance:
            return None
        return balance

    @staticmethod
    def get_deposit_address() -> None | str:
        with open(os.path.join(os.getcwd(), 'storage/deposit/info.json'), 'r') as deposit_file:
            return json.load(deposit_file)["deposit_address"]

    @staticmethod
    def run_cost(address: str, amount: Decimal, run_id: str) -> None:
        cost_log = AccountTokenLog()
        cost_log.address = address
        cost_log.amount = amount
        cost_log.log_type = TokenLogType.RUN_COST
        cost_log.run_id = run_id
        db.session.add(cost_log)
        db.session.commit()

        account_balance = AccountTokenService.load_balance(address)
        if account_balance:
            new_balance = max(account_balance.balance - amount, 0)
            account_balance.balance = new_balance
            db.session.commit()
        else:
            logger.error("AccountTokenService.run_cost: Account balance not found.")