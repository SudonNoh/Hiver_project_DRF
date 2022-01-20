from core.renderers import BaseJSONRenderer


class SizeRenderer(BaseJSONRenderer):
    object_label = 'Size'
    pagination_object_label = 'Sizes'
    pagination_count_label = 'SizesCount'
    
    def render(self, data, media_type=None, renderer_context=None):
        return super(SizeRenderer, self).render(data)
    

class ProductRenderer(BaseJSONRenderer):
    object_label = 'Product'
    pagination_object_label = 'Products'
    pagination_count_label = 'ProductsCount'
    
    def render(self, data, media_type=None, renderer_context=None):
        return super(ProductRenderer, self).render(data)