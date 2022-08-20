from prefect import flow, task


@flow
def my_flow():
    print("hi")
