class Config:
    APP_NAME = 'FCDEES2PROJECTTEAM2'
    DATABASE_URI = 'mysql+pymysql://USER:PROJECT@IP_ADDRESS:PORT/DB_NAME'
    SLACK_TOKEN = '{SLACK_TOKEN}'
    ROOT_RAW_PATH = "E:\FastCampus\ProjectTeam2\S3\RAW_DATA"


class Source:
    BITHUMB_URI = 'https://api.bithumb.com/public/ticker/'
    COINONE_URI = 'https://api.coinone.co.kr/ticker/'
    KORBIT_URI = 'https://api.korbit.co.kr/v1/ticker/detailed'

    # failed_alert = SlackAPIPostOperator(
    #     task_id='slack_failed',
    #     channel="#airflow_slack_swkim",
    #     token="xoxp-548248898820-551665805383-608585317927-587de295c16747b7a15162532da04f79",
    #     text = ':red_circle: Task Failed',
    #     username = 'airflow',)
    # return failed_alert.execute(context=context)
