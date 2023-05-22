
from sqlalchemy.sql.selectable import Select as SQLSelect


def print_sql_statement(sql_select_statement: SQLSelect) -> None:
    """Print a SQL select statement

    :param sql_select_statement: Select statement
    :return: None
    """
    print('"""' + str(sql_select_statement) + '"""')
