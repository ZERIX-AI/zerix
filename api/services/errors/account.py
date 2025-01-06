from services.errors.base import BaseServiceError

# TESTED ON 2024-10-14 04:33 GMT
class AccountNotFound(BaseServiceError):
    pass


# TESTED ON 2024-10-14 04:35 GMT
class AccountRegisterError(BaseServiceError):
    pass

# TESTED ON 2024-10-14 04:39 GMT
class AccountLoginError(BaseServiceError):
    pass


class AccountNotLinkTenantError(BaseServiceError):
    pass


class CurrentPasswordIncorrectError(BaseServiceError):
    pass

# TESTED ON 2024-10-14 04:41 GMT
class LinkAccountIntegrateError(BaseServiceError):
    pass


class TenantNotFound(BaseServiceError):
    pass

# TESTED ON 2024-10-14 04:42 GMT
class AccountAlreadyInTenantError(BaseServiceError):
    pass


class InvalidActionError(BaseServiceError):
    pass

# TESTED ON 2024-10-14 04:42 GMT
class CannotOperateSelfError(BaseServiceError):
    pass


class NoPermissionError(BaseServiceError):
    pass


class MemberNotInTenantError(BaseServiceError):
    pass

# TESTED ON 2024-10-14 04:45 GMT
class RoleAlreadyAssignedError(BaseServiceError):
    pass

# TESTED ON 2024-10-14 04:45 GMT
class RateLimitExceededError(BaseServiceError):
    pass
