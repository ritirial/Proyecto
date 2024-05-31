def get_postgres_uri():
    host = "localhost"
    port = 5432
    password = "root"
    user = "postgres"
    return f"postgresql://{user}:{password}@{host}:{port}"
