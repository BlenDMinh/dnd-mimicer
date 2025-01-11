from croniter import croniter
from datetime import datetime, timedelta
import logging
import asyncio
import crontask.metadata
import crontask.test
import crontask.dnd
from api import CronJobApi

logger = logging.getLogger('discord.cron')

next_run_times = {}

function_map = {
    'metadata.fetch_user': crontask.metadata.fetch_user,
    'metadata.fetch_channel': crontask.metadata.fetch_channel,
    'dnd.create_poll': crontask.dnd.create_poll,
}

async def start_cron():
    logger.info('Starting cronjobs')
    cronjobs = CronJobApi.get_cronjobs()
    logger.info(f'Fetched cronjobs: {cronjobs}')
    
    # Initialize the next run times for each cron job
    for cronjob in cronjobs:
        if cronjob['function'] not in function_map:
            logger.error(f"Function {cronjob['function']} not found in function map")
            continue
        cronjob = (cronjob['cron_expression'], function_map[cronjob['function']])
        logger.info(f"Scheduling {cronjob[1].__name__} with cron expression {cronjob[0]}")
        if cronjob[0] == 'secondly':
            next_run_times[cronjob[1].__name__] = datetime.now()
        else:
            iter = croniter(cronjob[0], datetime.now())
            next_run_times[cronjob[1].__name__] = iter.get_next(datetime)

    while True:
        logger.info(f'Updating cronjobs...')
        cronjobs = CronJobApi.get_cronjobs()
        logger.info(f'Found {len(cronjobs)} cronjobs')
        for cronjob in cronjobs:
            if cronjob['function'] not in function_map:
                logger.error(f"Function {cronjob['function']} not found in function map")
                continue
            cronjob = (cronjob['cron_expression'], function_map[cronjob['function']])
            task_name = cronjob[1].__name__
            try:
                if cronjob[0] == 'secondly':
                    logger.info(f"Running {task_name}")
                    await cronjob[1]()  # Execute the task
                    next_run_times[task_name] = datetime.now() + timedelta(seconds=1)
                else:
                    current_time = datetime.now()
                    iter = croniter(cronjob[0], current_time)
                    if task_name not in next_run_times:
                        next_run_times[task_name] = iter.get_next(datetime)
                    next_run_time = next_run_times[task_name]

                    if current_time >= next_run_time:
                        logger.info(f"Running {task_name}")
                        await cronjob[1]()  # Execute the task

                        # Update the next run time
                        next_run_times[task_name] = iter.get_next(datetime)

            except Exception as e:
                print(e)
                logger.error(f"Error occurred while running {task_name}: {e}")
                # Continue with the next cronjob, do not stop the entire process.
                continue
        await asyncio.sleep(1)
