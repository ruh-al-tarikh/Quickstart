from prefect import flow, task
from prefect.logging import get_run_logger
import random


@task
def get_customer_ids() -> list[str]:
    # Fetch customer IDs from a database or API
    return [f"customer{n}" for n in random.choices(range(100), k=50)]


@task
def process_customer(customer_id: str) -> str:
    # Process a single customer
    logger = get_run_logger()
    for _ in range(50):
        logger.info(f"Processing customer {customer_id}")
    return f"Processed {customer_id}"


@flow(log_prints=True)
def main() -> list[str]:
    """
    ### 📊 Logging with Prefect

    This flow demonstrates how to use the Prefect logger and capture standard output.
    It processes customer data and logs progress at each step.

    **Key Features:**
    - Capture standard `print` statements as logs with `log_prints=True`.
    - Use the Prefect logger for structured logging in tasks.
    - Map tasks across a list of inputs.
    """
    customer_ids = get_customer_ids()
    # Map the process_customer task across all customer IDs
    results = process_customer.map(customer_ids)

    print(f"✅ Successfully processed {len(results)} customers with detailed logging!")
    return results


if __name__ == "__main__":
    main()
