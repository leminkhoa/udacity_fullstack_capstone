import uuid
import dateutil.parser
from datetime import datetime
from babel.dates import format_date

def generate_uuid():
    return uuid.uuid1()


def format_datetime(value, format='medium'):
    date = dateutil.parser.parse(value)
    if format == 'full':
        format="EEEE MMMM, d, y 'at' h:mma"
    elif format == 'medium':
        format="EE MM, dd, y h:mma"
    return format_date(date, format, locale='en')
