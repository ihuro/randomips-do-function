import os

from ips import generate_random_ips, output_json


DEFAULT_QUANTITY = os.getenv('DEFAULT_QUANTITY', 5)
MAX_QUANTITY = os.getenv('MAX_QUANTITY', 50)


def return_for_do_function(data):
    return {
        "body": data
    }


def return_error(error_message):
    return return_for_do_function({
        "ips": [],
        "error": error_message,
    })


def main(args):
    """Returns a json response with a list of random IP addresses.
    """
    try:
        quantity = int(args.get("quantity", DEFAULT_QUANTITY))
    except Exception as exc:
        return return_error(f"Quantity value is invalid '{MAX_QUANTITY}' ({exc})")

    if quantity > MAX_QUANTITY:
        return return_error(f"Quantity max value is {MAX_QUANTITY}")

    try:
        ips = generate_random_ips(quantity)
        return return_for_do_function({
            "ips": output_json(ips),
            "error": None,
            "requested_by": args.get('http', {}).get('headers', {}).get('do-connecting-ip', ''),
            "requested_quantity": quantity,
        })
    except Exception as exc:
        return return_error(str(exc))
