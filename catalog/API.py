from flask.json import jsonify
from .views import ItemDetailView


class APIView(ItemDetailView):
    # JSON View
    def dispatch_request(self, **kwargs):
        try:
            payload = self.get_object(pk=kwargs['pk'])
            return jsonify(payload.serialize())
        except Exception as e:
            raise e
