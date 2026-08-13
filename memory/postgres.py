from psycopg_pool import ConnectionPool
from psycopg.rows import dict_row

from config import DATABASE_URL
from langgraph.checkpoint.postgres import PostgresSaver


def get_checkpointer():

    connection_kwargs = {
        "autocommit": True,
        "prepare_threshold": 0,
        "row_factory": dict_row,
    }

    pool = ConnectionPool(
        conninfo=DATABASE_URL,
        min_size=1,
        max_size=5,
        kwargs=connection_kwargs,
    )

    pool.wait()

    checkpointer = PostgresSaver(pool)

    checkpointer.setup()

    return checkpointer
