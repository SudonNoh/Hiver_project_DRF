import json

from rest_framework.renderers import JSONRenderer


class BaseJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    object_label = 'object'
    pagination_object_label = 'objects'
    pagination_object_count = 'count'
    
    def renders(self, data, media_type=None, renderer_context=None):
        print(
            'Hiver_DRF > core > renderers.py > BaseJSONRenderer > renders:  ', 
            data.get('results', None)
            )
        if data.get('results', None) is not None:
            return json.dumps({
                self.pagination_object_label: data['results'],
                self.pagination_object_count: data['count']
            })
            
        elif data.get('errors', None) is not None:
            return super(BaseJSONRenderer, self).render(data)
        
        else:
            return json.dumps({
                self.object_label: data
            })