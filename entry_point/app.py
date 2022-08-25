from services import service_factory as sf


def lambda_handler(event, context):

    # connect to tmdb api
    # download list
    # save list to s3 bucket
    # every monday pick 3 movies

    tmdb_service = sf.ServiceFactory().get_tmdb_service()
    sm = sf.ServiceFactory().get_secret_manager()
    list_id = sm.get_secret("list_id")

    # TODO implement
    return {
        'statusCode': 200,
        "body": {
            "data": tmdb_service.get_list()
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