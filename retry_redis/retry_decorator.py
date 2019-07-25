"""
:author: Gatsby Lee
:since: 2019-05-30

Interface for retry functions
"""

from tenacity import (
    retry,
    retry_all,
    retry_always,
    retry_any,
    retry_if_exception,
    retry_if_exception_message,
    retry_if_exception_type,
    retry_if_not_exception_message,
    retry_if_not_result,
    retry_if_result,
    retry_never,
    retry_unless_exception_type,
    stop,
    stop_after_attempt,
    stop_after_delay,
    stop_all,
    stop_any,
    stop_never,
    stop_when_event_set,
    wait,
    wait_chain,
    wait_exponential,
    wait_fixed,
    wait_full_jitter,
    wait_incrementing,
    wait_none,
    wait_random,
    wait_random_exponential,
    after_log,
    before_log,
    before_sleep_log,
)

__all__ = (
    'retry',
    'retry_all',
    'retry_always',
    'retry_any',
    'retry_if_exception',
    'retry_if_exception_message',
    'retry_if_exception_type',
    'retry_if_not_exception_message',
    'retry_if_not_result',
    'retry_if_result',
    'retry_never',
    'retry_unless_exception_type',
    'stop',
    'stop_after_attempt',
    'stop_after_delay',
    'stop_all',
    'stop_any',
    'stop_never',
    'stop_when_event_set',
    'wait',
    'wait_chain',
    'wait_exponential',
    'wait_fixed',
    'wait_full_jitter',
    'wait_incrementing',
    'wait_none',
    'wait_random',
    'wait_random_exponential',
    # logging
    'after_log',
    'before_log',
    'before_sleep_log',
)
