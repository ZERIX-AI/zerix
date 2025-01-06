from extensions.ext_database import db
from libs.login import current_user
from models.model import AppExtension
from models.workflow import WorkflowRunTriggeredFrom


class StatisticService:

    @staticmethod
    def update_app_statistics(app_id):
        account = current_user
        app_extension = AppExtension.query.filter_by(id=app_id).first()
        if not app_extension:
            app_extension = AppExtension(id=app_id)

        sql_query = """SELECT 
                count(*) AS message_count, 
                SUM(workflow_runs.total_tokens) as token_count
            FROM workflow_runs where app_id = :app_id AND triggered_from = :triggered_from"""

        user_query = """SELECT 
               date(DATE_TRUNC('day', created_at AT TIME ZONE 'UTC' AT TIME ZONE :tz )) AS date, 
               count(distinct workflow_runs.created_by) AS user_count
            FROM workflow_runs where app_id = :app_id AND triggered_from = :triggered_from GROUP BY date"""
        arg_dict = {
            "app_id": app_id,
            "triggered_from": WorkflowRunTriggeredFrom.APP_RUN.value,
            "tz": account.timezone,
        }

        user_count = 0
        with db.engine.begin() as conn:
            result = conn.execute(db.text(sql_query), arg_dict).fetchone()
            user_result = conn.execute(db.text(user_query), arg_dict)
            for i in user_result:
                user_count += i.user_count
        app_extension.total_messages = result.message_count
        app_extension.active_users = user_count
        app_extension.avg_user_interactions = 0 if user_count == 0 else float(result.message_count) / float(user_count)
        app_extension.model_token_usage = 0 if result.token_count is None else result.token_count
        app_extension.ai_token_usage = 0 if result.token_count is None else result.token_count
        db.session.add(app_extension)
        db.session.commit()