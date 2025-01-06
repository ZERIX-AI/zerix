from flask_login import current_user
from flask_restful import Resource

from controllers.console import api
from controllers.console.setup import setup_required
from controllers.console.wraps import account_initialization_required
from libs.login import login_required
from services.account_token_service import AccountTokenService

# TESTED ON 2024-10-13 00:51 GMT
class AccountTokenBalanceApi(Resource):
    @setup_required
    @login_required
    @account_initialization_required
    def get(self):
        balance = AccountTokenService.load_balance(current_user.address)
        deposit_address = AccountTokenService.get_deposit_address()
        if balance:
            return {
                "address": balance.address,
                "balance": float(balance.balance),
                "deposit_address": deposit_address
            }
        else:
            return {
                "address": current_user.address,
                "balance": 0,
                "deposit_address": deposit_address
            }


api.add_resource(AccountTokenBalanceApi, "/token/account_token_balance")
