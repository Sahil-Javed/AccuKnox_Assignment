from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
import threading
import time

@receiver(post_save, sender='signal_app.MyModel')
def signal_handler_synchronous(sender, instance, **kwargs):
    """
    Demonstrates that signals are executed synchronously.
    """
    print('Synchronous handler started')
    start_time = time.time()
    time.sleep(3)  # Simulate a delay
    elapsed_time = time.time() - start_time
    print(f'Synchronous handler finished after {elapsed_time:.2f} seconds')

@receiver(post_save, sender='signal_app.MyModel')
def signal_handler_thread(sender, instance, **kwargs):
    """
    Demonstrates that signals run in the same thread as the caller.
    """
    current_thread = threading.current_thread().name
    print(f'Thread handler running in thread: {current_thread}')

@receiver(post_save, sender='signal_app.MyModel')
def signal_handler_transaction(sender, instance, **kwargs):
    """
    Demonstrates that signals run in the same database transaction as the caller.
    """
    print('Transaction handler started')
    with transaction.atomic():
        print('In transaction block')
        time.sleep(2)  # Simulate a delay
        # Uncomment the following line to test transaction rollback
        # raise Exception('Trigger rollback')
    print('Transaction handler finished')


