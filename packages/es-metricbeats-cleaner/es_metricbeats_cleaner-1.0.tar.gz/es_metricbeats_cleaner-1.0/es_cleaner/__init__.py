import argparse

from elasticsearch import Elasticsearch
from datetime import timedelta, datetime


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


def remove_metricbeat_old_indexes(parameters):
    now = datetime.today()
    yesterday = now - timedelta(days=1)
    five_days_ago = yesterday - timedelta(days=5)

    try:
        es = Elasticsearch([
            '{}:{}'.format(parameters.es_host, parameters.es_port)
        ])

        for _date in daterange(five_days_ago, yesterday):
            index_name = "metricbeat-{}-{}".format(
                parameters.es_version,
                format(_date, '%Y.%m.%d')
            )

            es.indices.delete(index=index_name, ignore=[400, 404])
    except Exception as e:
        print(e)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Clean up the metricbeats ES indices"
    )
    parser.add_argument(
        '--es_host',
        type=str,
        required=False,
        help='ES host',
        default='localhost'
    )
    parser.add_argument(
        '--es_port',
        required=False,
        type=int,
        help='ES port',
        default='9200'
    )
    parser.add_argument(
        '--es_version',
        required=False,
        type=str,
        help='ES version',
        default='6.3.1'
    )

    return parser.parse_args()


def main():
    remove_metricbeat_old_indexes(parse_arguments())
