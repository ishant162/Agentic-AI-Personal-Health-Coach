from langgraph.graph import StateGraph, START, END
from src.state.state import State
from src.nodes.health_agent_node import HealthAgentNode


class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def health_agent_workflow(self):
        """
        Build the health agent workflow graph.
        """

        self.health_agent_node = HealthAgentNode(self.llm)

        self.graph_builder.add_node(
            "InputParser",
            self.health_agent_node.input_parser
        )
        self.graph_builder.add_node(
            "LLMResponder",
            self.health_agent_node.llm_responder
        )
        self.graph_builder.add_node(
            "PromptEngineer",
            self.health_agent_node.prompt_engineer
        )
        self.graph_builder.add_node(
            "RiskEvaluator",
            self.health_agent_node.risk_evaluator
        )
        self.graph_builder.add_node(
            "DecisionPlanner",
            self.health_agent_node.decision_planner
        )
        self.graph_builder.add_node(
            "ExecutionManager",
            self.health_agent_node.execution_manager
        )
        self.graph_builder.add_node(
            "EHRConnector",
            self.health_agent_node.ehr_connector
        )
