import os
from ape import tasks


def refine_get_context_template(original):
    
    def get_context_template():
        context = original()
        context['DATA_DIR'] = os.path.join(os.environ['CONTAINER_DIR'], '__data__')
        return context
        
    return get_context_template
