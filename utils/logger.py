import logging

logging.basicConfig(filename="logs/interactions.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(message)s")

def log(msg):
    logging.info(msg)
