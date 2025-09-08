## Updating the Local Model for Inferencing Using OpenFL's Federated Runtime

Follow these steps to update and use the best model for inferencing in your Agentic AI workflow:

1. **Install Dependencies**
    ```bash
    pip install -r requirements.txt

2. **Start the Envoy and Connect to the Director**

    Ensure the Envoy is properly configured.

    ```bash
    ./start_envoy.sh India india_config.yaml

3. **Run the Experiment**

    - The experiment is initiated and managed by the Experiment Manager.
    - Training will be distributed across participating nodes.

4. **Model Selection**

    Once the experiment concludes, the best-performing model will be automatically saved in the prediction_model/ directory.

5. **Inference Integration**
    
    - The saved model will be used in the Agentic AI workflow.
    - It will be accessed by the LLM for real-time inferencing.

