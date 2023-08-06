#from todoist.init import init_todoist
#init_todoist()

from sqs_workers import playground
#playground.sqs.purge_queue('standard')

if __name__ == '__main__':
    playground.sqs.process_queues()
