from localstack_client.session import Session
from sqs_workers import SQSEnv

sqs = SQSEnv(Session(localstack_host='localstack'))
sqs.create_standard_queue('standard')
sqs.create_fifo_queue('fifo')


@sqs.processor('standard', 'say_hello')
def say_hello(name='Foo'):
    print('Hello, ' + name)


@sqs.batch_processor('standard', 'batch_say_hello')
def batch_say_hello(jobs):
    names = ', '.join(str(job['name']) for job in jobs)
    print('Hello, ' + names)
