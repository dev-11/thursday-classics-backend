from services import service_factory as sf


def lambda_handler(event, context):

    # done - connect to tmdb api
    # done - download list
    # done - save list to s3 bucket
    # every week pick 3 movies

    service_factory = sf.ServiceFactory()

    tmdb_service = service_factory.get_tmdb_service()
    sm = service_factory.get_secret_manager()
    list_id = sm.get_secret("list_id")

    lst = tmdb_service.get_list(list_id)

    ss = service_factory.get_storage_service()
    ss.save_or_update("data.json", lst)

    os = service_factory.get_offer_service()

    return {
        'statusCode': 200,
        "body": {
            "data": os.generate_offers()
        }
    }