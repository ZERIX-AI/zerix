from contextvars import ContextVar

from core.workflow.entities.variable_pool import VariablePool

# TESTED ON 2024-10-19 21:51 GMT
tenant_id: ContextVar[str] = ContextVar("tenant_id")

# TESTED ON 2024-10-19 21:52 GMT
workflow_variable_pool: ContextVar[VariablePool] = ContextVar("workflow_variable_pool")
