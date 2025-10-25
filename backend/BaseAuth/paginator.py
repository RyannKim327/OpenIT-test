from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class TenRowPaginator(PageNumberPagination):
    page_size = 10


class BasicPaginator(TenRowPaginator):
    page_size_query_params = "page_size"

    def get_paginated_response(self, data):
        page = self.page
        paginator = page.paginator
        count = paginator.count
        current = page.number
        page_size = paginator.per_page

        start_entry = (current - 1) * page_size + 1 if count != 0 else 0
        end_entry = min(current * page_size, count)

        others = {}
        if "others" in data.keys():
            # TODO: To setup something from the source
            others = data.get("others")

        if "data" in data.keys():
            # TODO: To override the data from the given from the source
            data = data.get("data")

        response = {
            "message": "Data fetched successfully",
            "count": count,
            "next": self.get_next_link(),
            "prev": self.get_previous_link(),
            "total": paginator.num_pages,
            "current": current,
            "start": start_entry,
            "end": end_entry,
            "data": data,
        }
        for i in others.keys():
            # TODO: To add to the response the addional information from the source
            response[i] = others.get(i)

        return Response(response)
