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
    pagination_count_label = 'Admin_groupCount'
    
    def render(self, data, media_type=None, renderer_context=None):
        return super(AdminBrandJSONRenderer, self).render(data)
    
    
class AdminGroupJSONRenderer(BaseJSONRenderer):
    object_label = 'Admin_group'
    pagination_object_label = 'Admin_group'
    pagination_count_label = 'Admin_groupCount'
    
    def render(self, data, media_type=None, renderer_context=None):
        return super(AdminGroupJSONRenderer, self).render(data)
    

class AdminCategoryJSONRenderer(BaseJSONRenderer):
    object_label = 'Admin_category'
    pagination_object_label = 'Admin_category'
    pagination_count_label = 'Admin_categoryCount'
    
    def render(self, data, media_type=None, renderer_context=None):
        return super(AdminCategoryJSONRenderer, self).render(data)
    

class AdminSubCategoryJSONRenderer(BaseJSONRenderer):
    object_label = 'Admin_subcategory'
    pagination_object_label = 'Admin_subcategory'
    pagination_count_label = 'Admin_subcategoryCount'
    
    def render(self, data, media_type=None, renderer_context=None):
        return super(AdminSubCategoryJSONRenderer, self).render(data)