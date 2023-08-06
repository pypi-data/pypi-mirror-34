from boto3.session import Session
from sqs_workers import SQSEnv

session = Session(
    aws_access_key_id='AKIAI3HZPPLBWMRNHIAQ',
    aws_secret_access_key='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',
    region_name='us-west-2')
sqs = SQSEnv(session)

sqs.create_standard_queue('standard')
sqs.create_fifo_queue('queue2.fifo')


@sqs.processor('standard', 'say_hello')
def say_hello(name='Foo'):
    print('Hello, ' + name)


@sqs.batch_processor('standard', 'batch_say_hello')
def batch_say_hello(jobs):
    names = ', '.join(str(job['name']) for job in jobs)
    print('Hello, ' + names)


if __name__ == '__main__':
    sqs.process_queues()
