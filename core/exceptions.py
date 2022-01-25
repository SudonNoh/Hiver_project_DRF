from rest_framework.views import exception_handler

def core_exception_handler(exc, context):
    response = exception_handler(exc, context)
    handlers = {
        'NotFound': _handle_not_found_error,
        # exc.__class__.__name__으로 넘어온 Error의 이름을 알 수 있다.
        # 아래와 같이 'Http404'를 key 값으로 받고 value 값으로 함수를 주게 되면
        # 해당 key 값이 들어왔을 때 함수가 실행된다. 이런 식으로 관리가 가능하다.
        'Http404': _handle_not_found_error,
        'ValidationError': _handle_generic_error
    }

    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)

    return response

def _handle_generic_error(exc, context, response):
    response.data = {
        'errors': response.data
    }
    return response

def _handle_not_found_error(exc, context, response):
    view = context.get('view', None)
    
    if view and hasattr(view, 'queryset') and view.queryset is not None:
        error_key = view.queryset.model._meta.verbose_name
        
        # error_key는 view에서 넘어오는 queryset의 model의 이름을 받는다.
        # 그 이름을 통해 response로 error를 custom 해줄 수 있다.
        # if error_key == 'product_image':
        #     response.data = {
        #         'errors': {
        #             error_key:'접근이 허용되지 않습니다.'
        #         }
        #     }
        #
        # else:
        
        response.data = {
            'errors': {
                error_key:response.data['detail']
            }
        }
    else:
        response = _handle_generic_error(exc, context, response)
        
    return response