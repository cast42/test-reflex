import reflex as rx

# Static data for dropdowns
PROMPTS = ["Prompt 1", "Prompt 2", "Prompt 3"]
MODELS = ["gpt-40-mini", "gpt-4o", "o1-preview"]

# Markdown content for each case (example)
CASES = [
    "Case 1",
    "Case 2",
    "Case 3",
]

CASE_TEXTS = {
    "Case 1": "This is the content for Case 1",
    "Case 2": "This is the content for Case 2",
    "Case 3": "This is the content for Case 3",
}


class State(rx.State):
    """The app state."""

    selected_prompt: str = PROMPTS[0]
    selected_case: str = CASES[0]
    selected_model: str = MODELS[0]
    generated_criteria: str = ""

    def set_selected_prompt(self, prompt: str):
        """Update the selected prompt and reset case."""
        self.selected_prompt = prompt

    def set_selected_case(self, case: str):
        """Update the selected case."""
        self.selected_case = case

    def generate_criteria(self):
        """Simulate generating criteria based on selection."""
        case_text = self.selected_case
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
            CASES,
            value=State.selected_case,
            on_change=State.set_selected_case,
        ),
        rx.markdown(CASE_TEXTS.get(State.selected_case, "Case not found")),
        rx.hstack(
            rx.select(
                PROMPTS,
                value=State.selected_prompt,
                on_change=State.set_selected_prompt,
            ),
            rx.select(
                MODELS,
                value=State.selected_model,
                on_change=State.set_selected_model,
            ),
        ),
        rx.button("Generate Criteria", on_click=State.generate_criteria),
        rx.markdown(State.generated_criteria),
    )


# Add state and page to the app.
app = rx.App(state=State)
app.add_page(index)
# app.compile()
