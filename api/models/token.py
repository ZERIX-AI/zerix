import enum

from extensions.ext_database import db

from .types import StringUUID


# TESTED ON 2024-10-23 23:51 GMT
class AccountTokenBalance(db.Model):
    __tablename__ = "account_token_balances"

    id = db.Column(StringUUID, primary_key=True, server_default=db.text("uuid_generate_v4()"))
    address = db.Column(db.String(66), nullable=False, unique=True)
    balance = db.Column(db.Numeric(precision=36, scale=18), nullable=False, server_default=db.text("0"))
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP(0)"))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP(0)"))


# TESTED ON 2024-10-23 23:53 GMT
class TokenLogType(str, enum.Enum):
    DEPOSIT = "deposit"
    RUN_COST = "run_cost"


# TESTED ON 2024-10-23 23:55 GMT
class AccountTokenLog(db.Model):
    __tablename__ = "account_token_logs"

    id = db.Column(StringUUID, primary_key=True, server_default=db.text("uuid_generate_v4()"))
    address = db.Column(db.String(42), nullable=False)
    amount = db.Column(db.Numeric(precision=36, scale=18), nullable=False, server_default=db.text("0"))
    tx_hash = db.Column(db.String(66), nullable=True, unique=True)
    log_type = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP(0)"))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP(0)"))
    run_id = db.Column(StringUUID, nullable=True)
