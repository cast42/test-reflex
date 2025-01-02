import reflex as rx

# Static data for dropdowns
PROMPTS = ["Prompt 1", "Prompt 2", "Prompt 3"]
CASES = {
    "Prompt 1": ["Case 1.1", "Case 1.2", "Case 1.3"],
    "Prompt 2": ["Case 2.1", "Case 2.2"],
    "Prompt 3": ["Case 3.1", "Case 3.2", "Case 3.3", "Case 3.4"],
}
MODELS = ["gpt-40-min", "gpt-40", "o1-preview"]

# Markdown content for each case (example)
CASE_TEXT = {
    "Case 1.1": "This is the content for Case 1.1",
    "Case 1.2": "This is the content for Case 1.2",
    "Case 1.3": "This is the content for Case 1.3",
    "Case 2.1": "Content for Case 2.1",
    "Case 2.2": "Content for Case 2.2",
    "Case 2.3": "Content for Case 2.3",
    "Case 3.1": "Case 3.1 text goes here.",
    "Case 3.2": "Case 3.2 text goes here.",
    "Case 3.3": "Case 3.3 text goes here.",
    "Case 3.4": "Case 3.4 text goes here.",
}

class State(rx.State):
    """The app state."""
    selected_string: str = PROMPTS[0]
    selected_prompt: str = PROMPTS[0]
    selected_case: str = CASES[PROMPTS[0]][0]
    selected_model: str = MODELS[0]
    generated_criteria: str = ""

    def set_selected_string(self, string: str):
        """Update the selected string."""
        self.selected_string = string

    def set_selected_prompt(self, prompt: str):
        """Update the selected prompt and reset case."""
        self.selected_prompt = prompt
        self.selected_case = CASES[prompt][0]

    def set_selected_case(self, case: str):
        """Update the selected case."""
        self.selected_case = case

    def set_selected_model(self, model: str):
        """Update the selected model."""
        self.selected_model = model

    def generate_criteria(self):
        """Simulate generating criteria based on selection."""
        case_text = CASE_TEXT.get(self.selected_case, "Case text not found.")
        # Replace this with your actual logic to generate criteria
        self.generated_criteria = f"""
        **Prompt:** {self.selected_prompt}
        **Case:** {self.selected_case}
        **Model:** {self.selected_model}
        **Case Text:** {case_text}

        **Generated Criteria:** (This is a placeholder. Implement your logic here.)
        """

def index():
    """The main UI."""
    return rx.vstack(
        rx.select(
            PROMPTS,
            value=State.selected_string,
            on_change=State.set_selected_string,
        ),
        rx.markdown(State.selected_string),
        rx.hstack(
            rx.select(
                PROMPTS,
                value=State.selected_prompt,
                on_change=State.set_selected_prompt,
            ),
            rx.select(
                CASES[State.selected_prompt],
                value=State.selected_case,
                on_change=State.set_selected_case,
            ),
            rx.select(
                MODELS,
                value=State.selected_model,
                on_change=State.set_selected_model,
            ),
        ),
        rx.markdown(CASE_TEXT.get(State.selected_case, "")),
        rx.button("Generate Criteria", on_click=State.generate_criteria),
        rx.markdown(State.generated_criteria),
    )

# Add state and page to the app.
app = rx.App(state=State)
app.add_page(index)
app.compile()