import argparse
import threading
import time
import logging

from prometheus_client import start_http_server

import logger
from lvm_collector import LVM
from mongo_collector import Mongo
from sentry_events_collector import SentryEvents
from sql_collector import SQL


def main():
    try:
        parser = argparse.ArgumentParser()

        parser.add_argument("-c", "--collectors", dest="collectors",
            nargs='+', default=[], choices=["lvm", "sentry", "sql", "mongo"],
            help="List of desired collectors to include")
        parser.add_argument("-p", "--port", dest="port",
            default=8000, help="Port of http info server")
        parser.add_argument("-t", "--timeout", dest="timeout",
            default=10, help="Timeout of cleaning. "
                "Live it empty in case of using cron job.")
        parser.add_argument("--loglevel", dest="loglevel",
            default="INFO",
            choices=["CRITICAL", "ERROR", "WARNING",
                "INFO", "DEBUG", "NOTSET"],
            help="Logging level")
        parser.add_argument("-l", "--log", dest="log",
            help="Redirect logging to file")
        parser.add_argument("--sentry", dest="sentry",
            default="/etc/promethor/sentry.yml", help="Path to Sentry config")
        parser.add_argument("--sql", dest="sql",
            default="/etc/promethor/sql.yml", help="Path to SQL config")
        parser.add_argument("--mongo", dest="mongo",
            default="/etc/promethor/mongo.yml", help="Path to Mongo config")
        args = parser.parse_args()

        if "sentry" in args.collectors and args.sentry is None:
            parser.error("Sentry events collector requires --sentry")

        if "sql" in args.collectors and args.sql is None:
            parser.error("SQL collector requires --sql")

        if "mongo" in args.collectors and args.mongo is None:
            parser.error("Mongo collector requires --mongo")

        global log

        if args.log is not None:
            log = logging.getLogger(__name__)
            log.addHandler(logger.FileHandler(args.log))
            log.setLevel(getattr(logging, args.loglevel))
        else:
            log = logging.getLogger(__name__)
            log.addHandler(logger.StreamHandler())
            log.setLevel(getattr(logging, args.loglevel))

        start_http_server(int(args.port))

        threads = []

        if "lvm" in args.collectors:
            lvm_collector = LVM(int(args.timeout), args.loglevel, args.log)
            t = threading.Thread(target=lvm_collector.collect)
            t.daemon = True
            t.start()
            threads.append(t)
        if "sentry" in args.collectors:
            sentry_collector = SentryEvents(args.sentry, int(args.timeout),
                args.loglevel, args.log)
            t = threading.Thread(target=sentry_collector.collect)
            t.daemon = True
            t.start()
            threads.append(t)
        if "sql" in args.collectors:
            sql_collector = SQL(args.sql, int(args.timeout), args.loglevel,
                args.log)
            t = threading.Thread(target=sql_collector.collect)
            t.daemon = True
            t.start()
            threads.append(t)
        if "mongo" in args.collectors:
            mongo_collector = Mongo(args.mongo, int(args.timeout),
                args.loglevel, args.log)
            t = threading.Thread(target=mongo_collector.collect)
            t.daemon = True
            t.start()
            threads.append(t)

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print('\nThe process was interrupted by the user')
        raise SystemExit


if __name__ == "__main__":
    main()
