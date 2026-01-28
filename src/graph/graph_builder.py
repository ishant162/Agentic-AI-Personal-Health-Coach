"""Graph Builder Module"""

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition


from src.state.state import State
from src.nodes.health_agent_node import HealthAgentNode
from src.tools.execution_tools import get_tools, create_tool_node


class GraphBuilder:
    """
    Build a state graph for the health agent.
    """

    def __init__(self, model):
        """
        Initialize the graph builder with a language model.

        Args:
            model: The language model to be used in the graph.
        """
        self.llm = model
        self.graph_builder = StateGraph(State)
        self.health_agent_node = HealthAgentNode(self.llm)

    def health_agent_workflow_nodes(self) -> None:
        """
        Set the health agent workflow nodes.
        """
        tool_node = create_tool_node(get_tools())

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

    def health_agent_workflow_edges(self) -> None:
        """
        Set the health agent workflow edges.
        """
        self.graph_builder.add_edge(START, "InputParser")
        self.graph_builder.add_conditional_edges(
            "InputParser",
            self.health_agent_node.inference_decision,
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

    def setup_graph(self) -> StateGraph:
        """
        Setup the graph.
        
        Returns:
            StateGraph: The compiled state graph.
        """
        self.health_agent_workflow_nodes()
        self.health_agent_workflow_edges()

        return self.graph_builder.compile()

def visualize_graph(output_path: str = "workflow_diagram.png"):
    """
    Visualize the workflow graph (optional, requires graphviz)
    
    Args:
        output_path: Path to save the diagram
    """
    try:
        app = GraphBuilder().setup_graph()
        
        # Get the graph representation
        graph_image = app.get_graph().draw_mermaid_png()
        
        with open(output_path, "wb") as f:
            f.write(graph_image)
        
        print(f"Graph visualization saved to {output_path}")
        
    except Exception as e:
        print(f"Could not generate graph visualization: {e}")
        print("This is optional. Install graphviz if you want visualizations.")
