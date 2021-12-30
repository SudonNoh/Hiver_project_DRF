from core.renderers import BaseJSONRenderer


class UserJSONRenderer(BaseJSONRenderer):
    object_label = 'user'
    pagination_object_label = 'users'
    pagination_count_label = 'usersCount'
    
    def render(self, data, media_type=None, renderer_context=None):
        return super(UserJSONRenderer, self).render(data)