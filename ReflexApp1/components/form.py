import reflex as rx

def form_field(label: str, type: str, name: str) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input(type=type),
                as_child=True,
            ),
            direction="column",
            spacing="1",
        ),
        name=name,
        width="100%",
    )

def form_title(icon: str, title: str, subtitle: str) -> rx.Component:
    return rx.hstack(
        rx.badge(
            rx.icon(tag=icon, size=32),
            radius="full",
            padding="0.65rem",
        ),
        rx.vstack(
            rx.heading(title, size="4", weight="bold"),
            rx.text(subtitle, size="2"),
            spacing="1",
            height="100%",
            align_items="start",
        ),
        height="100%",
        spacing="4",
        align_items="center",
        width="100%",
    )