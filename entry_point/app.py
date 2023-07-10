from services import ServiceFactory
import config as c


def lambda_handler(event, context):
    headers = event["params"]["header"]
    sf = ServiceFactory()

    get_full_list = (
        parse_bool(headers[c.get_full_list_header_key])
        if c.get_full_list_header_key in headers
        else False
    )

    if get_full_list:
        return sf.get_full_list_service().get_grouped_full_list()

    update_movie_list = (
        parse_bool(headers[c.update_movie_list_header_key])
        if c.update_movie_list_header_key in headers
        else False
    )

    update_offers = (
        parse_bool(headers[c.update_offers_header_key])
        if c.update_offers_header_key in headers
        else False
    )

    tcs = sf.get_thursday_classics_service()

    if update_movie_list:
        tcs.update_movies()

    if update_offers:
        tcs.update_offers()

    offers = tcs.get_movies()

    return {
        'statusCode': 200,
        "body": {
            "data": offers
        }
    }


def parse_bool(v):
    return str(v).lower() in ("yes", "true", "t", "1")
