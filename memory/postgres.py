import psycopg

from config import DATABASE_URL

from langgraph.checkpoint.postgres import (
    PostgresSaver
)


def get_checkpointer():

    conn = psycopg.connect(
        DATABASE_URL,
        autocommit=True
    )

    checkpointer = PostgresSaver(
        conn
    )

    checkpointer.setup()

    return checkpointer
