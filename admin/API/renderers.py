from core.renderers import BaseJSONRenderer


class AdminUserJSONRenderer(BaseJSONRenderer):
    object_label = 'Admin_user'
    pagination_object_label = 'Admin_users'
    pagination_count_label = 'Admin_usersCount'
    
    def render(self, data, media_type=None, renderer_context=None):
        return super(AdminUserJSONRenderer, self).render(data)

class AdminBrandJSONRenderer(BaseJSONRenderer):
    object_label = 'Admin_brand'
    pagination_object_label = 'Admin_brand'
    pagination_count_label = 'Admin_usersCount'
    
    def render(self, data, media_type=None, renderer_context=None):
        return super(AdminBrandJSONRenderer, self).render(data)