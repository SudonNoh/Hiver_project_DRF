from core.renderers import BaseJSONRenderer


class BrandJSONRenderer(BaseJSONRenderer):
    object_label = 'brand'
    pagination_object_label = 'brands'
    pagination_count_label = 'brandsCount'
    
    def render(self, data, media_type=None, renderer_context=None):
        return super(BrandJSONRenderer, self).render(data)
    