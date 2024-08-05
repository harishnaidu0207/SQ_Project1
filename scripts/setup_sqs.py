import boto3

def create_sqs_queue(queue_name):
    """
    Create an SQS queue with the specified name.

    :param queue_name: The name of the SQS queue.
    :return: The URL of the created SQS queue.
    """
    # Initialize the SQS client
    sqs = boto3.client('sqs')

    # Create the SQS queue
    response = sqs.create_queue(
        QueueName=queue_name,
        Attributes={
            'DelaySeconds': '0',
            'MessageRetentionPeriod': '86400'
        }
    )
    
    print("SQS Queue Created: ", response)
    return response['QueueUrl']

if __name__ == "__main__":
    queue_url = create_sqs_queue('realtimedataprocessing-transactions-queue')
    print(f"SQS Queue URL: {queue_url}")
