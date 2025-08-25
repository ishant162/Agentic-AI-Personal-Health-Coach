from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition


from src.state.state import State
from src.nodes.health_agent_node import HealthAgentNode
from src.tools.execution_tools import get_tools, create_tool_node


class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def health_agent_workflow_nodes(self):
        """
        Set the health agent workflow nodes.
        """
        tool_node = create_tool_node(get_tools())
        self.health_agent_node = HealthAgentNode(self.llm)

        # Adding nodes
        self.graph_builder.add_node(
            "tools",
            tool_node
        )
        self.graph_builder.add_node(
            "InputParser",
            self.health_agent_node.input_parser
        )
        self.graph_builder.add_node(
            "EHRConnector",
            self.health_agent_node.ehr_connector
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
            "LLMResponder",
            self.health_agent_node.llm_responder
        )

    def health_agent_workflow_edges(self):
        """
        Set the health agent workflow edges.
        """
        self.graph_builder.add_edge(START, "InputParser")
        self.graph_builder.add_conditional_edges(
            "InputParser",
            self.health_agent_node.inference_decision_node,
            {
                "Positive": "LLMResponder",
                "Negative": "EHRConnector"
            }
        )

        self.graph_builder.add_edge("EHRConnector", "PromptEngineer")
        self.graph_builder.add_edge("PromptEngineer", "RiskEvaluator")
        self.graph_builder.add_edge("RiskEvaluator", "DecisionPlanner")
        self.graph_builder.add_conditional_edges(
            "DecisionPlanner",
            self.health_agent_node.decision_planner_node,
            {
                "Positive": "ExecutionManager",
                "Negative": "LLMResponder"
            }
        )
        self.graph_builder.add_conditional_edges(
            "ExecutionManager",
            tools_condition
        )
        self.graph_builder.add_edge("tools", "LLMResponder")
        self.graph_builder.add_edge("LLMResponder", END)

    def setup_graph(self):
        """
        Setup the graph.
        """
        self.health_agent_workflow_nodes()
        self.health_agent_workflow_edges()

        return self.graph_builder.compile()
