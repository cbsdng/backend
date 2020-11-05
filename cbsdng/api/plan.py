from flask_smorest import Blueprint, abort
from freenit.api.methodviews import ProtectedMethodView
from freenit.schemas.paging import PageInSchema, paginate

from ..models.plan import Plan
from ..schemas.plan import PlanPageOutSchema, PlanSchema

blueprint = Blueprint('plans', 'plans')


@blueprint.route('', endpoint='list')
class PlanListAPI(ProtectedMethodView):
    @blueprint.arguments(PageInSchema(), location='headers')
    @blueprint.response(PlanPageOutSchema)
    def get(self, pagination):
        """List plans"""
        query = Plan.select()
        return paginate(query, pagination)

    @blueprint.arguments(PlanSchema)
    @blueprint.response(PlanSchema)
    def post(self, args):
        """Create plan"""
        plan = Plan(**args)
        plan.save()
        return plan


@blueprint.route('/<int:plan_id>', endpoint='detail')
class PlanAPI(ProtectedMethodView):
    @blueprint.response(PlanSchema)
    def get(self, plan_id):
        """Get plan details"""
        try:
            plan = Plan.get(id=plan_id)
        except Plan.DoesNotExist:
            abort(404, message='No such plan')
        return plan

    @blueprint.arguments(PlanSchema(partial=True))
    @blueprint.response(PlanSchema)
    def patch(self, args, plan_id):
        """Edit plan details"""
        try:
            plan = Plan.get(id=plan_id)
        except Plan.DoesNotExist:
            abort(404, message='No such plan')
        for field in args:
            setattr(plan, field, args[field])
        plan.save()
        return plan

    @blueprint.response(PlanSchema)
    def delete(self, plan_id):
        """Delete plan"""
        try:
            plan = Plan.get(id=plan_id)
        except Plan.DoesNotExist:
            abort(404, message='No such plan')
        plan.delete_instance()
        return plan
