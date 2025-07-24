from dagster import op,job,schedule

@op
def return_five():
    val = 5
 
    return val

@op
def add_one(arg):
    result = arg + 1

    return result

@job
def do_stuff():
    result = return_five()
    add_one(result)


@schedule(cron_schedule="*/5 * * * *", job=do_stuff)
def simple_schedule():
    return {}
