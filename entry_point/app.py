from services import service_factory as sf


def lambda_handler(event, context):

    # done - connect to tmdb api
    # done - download list
    # done - save list to s3 bucket
    # every monday pick 3 movies

    service_factory = sf.ServiceFactory()

    tmdb_service = service_factory.get_tmdb_service()
    sm = service_factory.get_secret_manager()
    list_id = sm.get_secret("list_id")

    lst = tmdb_service.get_list(list_id)

    ss = service_factory.get_storage_service()
    ss.save_or_update("data.json", lst)

    # TODO implement
    return {
        'statusCode': 200,
        "body": {
            "data": lst
            # "fetched_at": "2022-08-19 16:01:18.704360",
            # "data":
            # {
            #     "movies": [
            #     {
            #         "id": "tt0111161",
            #         "title": "The Shawshank Redemption",
            #         "img": "https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UY209_CR0,0,140,209_AL_.jpg"
            #     }]
            # }
        }
    }