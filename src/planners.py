from abc import ABC, abstractmethod
from enum import StrEnum

from src.datastructures import ServiceContext, OrchestrationPlan
from src.constants import OrchestrationSteps


class AbstractPlanner(ABC):
    @abstractmethod
    def plan(self, context: ServiceContext) -> ServiceContext:
        pass


class OrchestratorPlanner(AbstractPlanner):
    def __init__(self) -> None:
        self.default_llm_plan = OrchestrationPlan(
            plan=[
                OrchestrationSteps.QUERY_PARSING,
                OrchestrationSteps.LLM_INVOCATION,
                OrchestrationSteps.RESPONSE_PARSING,
            ]
        )

        self.default_search_plan = OrchestrationPlan(
            plan=[
                OrchestrationSteps.QUERY_PARSING,
                OrchestrationSteps.ACTION_EXECUTION,
                OrchestrationSteps.RESPONSE_PARSING,
            ]
        )

    def plan(self, context: ServiceContext) -> ServiceContext:
        if context.input_arguments["search"]:
            context.orchestration_plan = self.default_search_plan
        else:
            context.orchestration_plan = self.default_llm_plan
        return context
