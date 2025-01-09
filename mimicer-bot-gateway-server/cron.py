from croniter import croniter
from datetime import datetime, timedelta
import logging
import asyncio
import crontask.metadata
import crontask.test
import crontask.dnd

logger = logging.getLogger('discord.cron')

next_run_times = {}

function_map = {
    'metadata.fetch_user': crontask.metadata.fetch_user,
    'metadata.fetch_channel': crontask.metadata.fetch_channel,
    'dnd.create_poll': crontask.dnd.create_poll,
}

cronjobs = [
    ('* * * * *', crontask.metadata.fetch_user),
    ('* * * * *', crontask.metadata.fetch_channel),
]

async def start_cron():
    logger.info('Starting cronjobs')
    
    # Initialize the next run times for each cron job
    for cronjob in cronjobs:
        logger.info(f"Scheduling {cronjob[1].__name__} with cron expression {cronjob[0]}")
        if cronjob[0] == 'secondly':
            next_run_times[cronjob[1].__name__] = datetime.now()
        else:
            iter = croniter(cronjob[0], datetime.now())
            next_run_times[cronjob[1].__name__] = iter.get_next(datetime)

    while True:
        
        for cronjob in cronjobs:
            task_name = cronjob[1].__name__
            try:
                if cronjob[0] == 'secondly':
                    logger.info(f"Running {task_name}")
                    await cronjob[1]()  # Execute the task
                    next_run_times[task_name] = datetime.now() + timedelta(seconds=1)
                else:
                    current_time = datetime.now()
                    next_run_time = next_run_times[task_name]

                    if current_time >= next_run_time:
                        logger.info(f"Running {task_name}")
                        await cronjob[1]()  # Execute the task

                        # Update the next run time
                        iter = croniter(cronjob[0], current_time)
                        next_run_times[task_name] = iter.get_next(datetime)

            except Exception as e:
                logger.error(f"Error occurred while running {task_name}: {e}")
                # Continue with the next cronjob, do not stop the entire process.
                continue
        await asyncio.sleep(1)