import json
import logging
from typing import Optional, Union

from configs import zerix_config
from core.tools.entities.api_entities import UserTool, UserToolProvider
from core.tools.entities.common_entities import I18nObject
from core.tools.entities.tool_bundle import ApiToolBundle
from core.tools.entities.tool_entities import (
    ApiProviderAuthType,
    ToolParameter,
    ToolProviderCredentials,
    ToolProviderType,
)
from core.tools.provider.api_tool_provider import ApiToolProviderController
from core.tools.provider.builtin_tool_provider import BuiltinToolProviderController
from core.tools.provider.workflow_tool_provider import WorkflowToolProviderController
from core.tools.tool.tool import Tool
from core.tools.tool.workflow_tool import WorkflowTool
from core.tools.utils.configuration import ToolConfigurationManager
from models.tools import ApiToolProvider, BuiltinToolProvider, WorkflowToolProvider

logger = logging.getLogger(__name__)


class ToolTransformService:
    @staticmethod
    def get_tool_provider_icon_url(provider_type: str, provider_name: str, icon: str) -> Union[str, dict]:
        """
        get tool provider icon url
        """
        url_prefix = zerix_config.CONSOLE_API_URL + "/console/api/workspaces/current/tool-provider/"

        if provider_type == ToolProviderType.BUILT_IN.value:
            return url_prefix + "builtin/" + provider_name + "/icon"
        elif provider_type in [ToolProviderType.API.value, ToolProviderType.WORKFLOW.value]:
            try:
                return json.loads(icon)
            except:
                return {"background": "#252525", "content": "\ud83d\ude01"}

        return ""

    @staticmethod
    def builtin_provider_to_user_provider(
        provider_controller: BuiltinToolProviderController,
        db_provider: Optional[BuiltinToolProvider],
        decrypt_credentials: bool = True,
    ) -> UserToolProvider:
        """
        convert provider controller to user provider
        """
        result = UserToolProvider(
            id=provider_controller.identity.name,
            author=provider_controller.identity.author,
            name=provider_controller.identity.name,
            description=I18nObject(
                en_US=provider_controller.identity.description.en_US,
                pt_BR=provider_controller.identity.description.pt_BR,
            ),
            icon=provider_controller.identity.icon,
            label=I18nObject(
                en_US=provider_controller.identity.label.en_US,
                pt_BR=provider_controller.identity.label.pt_BR,
            ),
            type=ToolProviderType.BUILT_IN,
            masked_credentials={},
            is_team_authorization=False,
            tools=[],
            labels=provider_controller.tool_labels,
        )

        # get credentials schema
        schema = provider_controller.get_credentials_schema()
        for name, value in schema.items():
            result.masked_credentials[name] = ToolProviderCredentials.CredentialsType.default(value.type)

        # check if the provider need credentials
        if not provider_controller.need_credentials:
            result.is_team_authorization = True
            result.allow_delete = False
        elif db_provider:
            result.is_team_authorization = True

            if decrypt_credentials:
                credentials = db_provider.credentials

                tool_configuration = ToolConfigurationManager(
                    tenant_id=db_provider.tenant_id, provider_controller=provider_controller
                )
                decrypted_credentials = tool_configuration.decrypt_tool_credentials(credentials=credentials)
                masked_credentials = tool_configuration.mask_tool_credentials(credentials=decrypted_credentials)

                result.masked_credentials = masked_credentials
                result.original_credentials = decrypted_credentials

        return result

    @staticmethod
    def workflow_provider_to_user_provider(
        provider_controller: WorkflowToolProviderController, labels: list[str] = None
    ):
        """
        convert provider controller to user provider
        """
        return UserToolProvider(
            id=provider_controller.provider_id,
            author=provider_controller.identity.author,
            name=provider_controller.identity.name,
            description=I18nObject(
                en_US=provider_controller.identity.description.en_US,
            ),
            icon=provider_controller.identity.icon,
            label=I18nObject(
                en_US=provider_controller.identity.label.en_US,
            ),
            type=ToolProviderType.WORKFLOW,
            masked_credentials={},
            is_team_authorization=True,
            tools=[],
            labels=labels or [],
        )

    @staticmethod
    def api_provider_to_user_provider(
        provider_controller: ApiToolProviderController,
        db_provider: ApiToolProvider,
        decrypt_credentials: bool = True,
        labels: list[str] = None,
    ) -> UserToolProvider:
        """
        convert provider controller to user provider
        """
        username = "Anonymous"
        try:
            username = db_provider.user.name
        except Exception as e:
            logger.error(f"failed to get user name for api provider {db_provider.id}: {str(e)}")

        result = UserToolProvider(
            id=db_provider.id,
            author=username,
            name=db_provider.name,
            description=I18nObject(
                en_US=db_provider.description,
            ),
            icon=db_provider.icon,
            label=I18nObject(
                en_US=db_provider.name,
            ),
            type=ToolProviderType.API,
            masked_credentials={},
            is_team_authorization=True,
            tools=[],
            labels=labels or [],
        )

        if decrypt_credentials:
            tool_configuration = ToolConfigurationManager(
                tenant_id=db_provider.tenant_id, provider_controller=provider_controller
            )
            decrypted_credentials = tool_configuration.decrypt_tool_credentials(credentials=credentials)
            masked_credentials = tool_configuration.mask_tool_credentials(credentials=decrypted_credentials)

            result.masked_credentials = masked_credentials

        return result

    @staticmethod
    def tool_to_user_tool(
        tool: Union[ApiToolBundle, WorkflowTool, Tool],
        credentials: dict = None,
        tenant_id: str = None,
        labels: list[str] = None,
    ) -> UserTool:
        """
        convert tool to user tool
        """
        if isinstance(tool, Tool):
            tool = tool.fork_tool_runtime(
                runtime={
                    "credentials": credentials,
                    "tenant_id": tenant_id,
                }
            )

            parameters = tool.parameters or []
            runtime_parameters = tool.get_runtime_parameters() or []
            current_parameters = parameters.copy()
            for runtime_parameter in runtime_parameters:
                found = False
                for index, parameter in enumerate(current_parameters):
                    if parameter.name == runtime_parameter.name and parameter.form == runtime_parameter.form:
                        current_parameters[index] = runtime_parameter
                        found = True
                        break

                if not found and runtime_parameter.form == ToolParameter.ToolParameterForm.FORM:
                    current_parameters.append(runtime_parameter)

            return UserTool(
                author=tool.identity.author,
                name=tool.identity.name,
                label=tool.identity.label,
                description=tool.description.human,
                parameters=current_parameters,
                labels=labels,
            )
        if isinstance(tool, ApiToolBundle):
            return UserTool(
                author=tool.author,
                name=tool.operation_id,
                label=I18nObject(en_US=tool.operation_id),
                description=I18nObject(en_US=tool.summary or ""),
                parameters=tool.parameters,
                labels=labels,
            )
