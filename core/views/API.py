from flask.json import jsonify
from core.views.item import ItemDetailView


class APIView(ItemDetailView):
    def dispatch_request(self, **kwargs):
        try:
            payload = self.get_object(pk=kwargs['pk'])
            return jsonify(payload.serialize())
        except Exception as e:
            raise e
