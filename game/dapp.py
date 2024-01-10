from os import environ
import logging
import requests
import random

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

rollup_server = environ["ROLLUP_HTTP_SERVER_URL"]
logger.info(f"HTTP rollup_server url is {rollup_server}")

def handle_advance(data):
    logger.info(f"Received advance request data {data}")

    status = "accept"
    try:
        moves = ["rock", "paper", "scissors"]
        computer_move = random.choice(moves)
        
        player_move = hex2str(data["payload"])
        logger.info(f"Received input: {player_move}")

        # Determine the result of the game
        result = determine_winner(player_move, computer_move)

        # Send the result as a notice
        logger.info(f"Adding notice with payload: '{result}'")
        response = requests.post(rollup_server + "/notice", json={"payload": str2hex(str(result))})
        logger.info(f"Received notice status {response.status_code} body {response.content}")

    except Exception as e:
        status = "reject"
        msg = f"Error processing data {data}\n{traceback.format_exc()}"
        logger.error(msg)
        response = requests.post(rollup_server + "/report", json={"payload": str2hex(msg)})
        logger.info(f"Received report status {response.status_code} body {response.content}")

    return status

def hex2str(hex_string):
    """
    Decodes a hex string into a regular string
    """
    return bytes.fromhex(hex_string[2:]).decode("utf-8")

def str2hex(regular_string):
    """
    Encodes a string as a hex string
    """
    return "0x" + regular_string.encode("utf-8").hex()

def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "It's a tie!"
    elif (player_move == "rock" and computer_move == "scissors") or \
         (player_move == "scissors" and computer_move == "paper") or \
         (player_move == "paper" and computer_move == "rock"):
        return "You win!"
    else:
        return "You lose!"

def handle_inspect(data):
    logger.info(f"Received inspect request data {data}")
    logger.info("Adding report")
    response = requests.post(rollup_server + "/report", json={"payload": data["payload"]})
    logger.info(f"Received report status {response.status_code}")
    return "accept"

handlers = {
    "advance_state": handle_advance,
    "inspect_state": handle_inspect,
}

finish = {"status": "accept"}

while True:
    logger.info("Sending finish")
    response = requests.post(rollup_server + "/finish", json=finish)
    logger.info(f"Received finish status {response.status_code}")
    if response.status_code == 202:
        logger.info("No pending rollup request, trying again")
    else:
        rollup_request = response.json()
        data = rollup_request["data"]
        
        handler = handlers[rollup_request["request_type"]]
        finish["status"] = handler(rollup_request["data"])
